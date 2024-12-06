import requests
import json
from datetime import datetime, timedelta
from pathlib import Path
import re
from docx import Document
import numpy as np


class FeishuDocsAPI:
    def obtainTenantAccessToken(self, app_id, app_secret):
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        headers = {
            "Content-Type": "application/json; charset=utf-8",
        }
        data = {
            "app_id": app_id,
            "app_secret": app_secret,
        }
        data_json = json.dumps(data)
        response = requests.request("POST", url, headers=headers, data=data_json)
        response_json = json.loads(response.text)
        return response_json["tenant_access_token"]

    def obtainAllDocumentBlocks(self):
        url = (
            "https://open.feishu.cn/open-apis/docx/v1/documents/"
            + self.document_id
            + "/blocks"
        )
        payload = ""
        access_token = "Bearer " + self.access_token
        headers = {"Authorization": access_token}
        response = requests.request("GET", url, headers=headers, data=payload)
        # print(response.text)
        response_json = json.loads(response.text)
        return response_json

    def preprocessAllDocumentBlocks(self):
        self.all_document_blocks_response = self.obtainAllDocumentBlocks()
        self.all_document_blocks = self.all_document_blocks_response["data"]["items"]
        self.all_block_ids = self.all_document_blocks[0]["children"]
        for block_index, block in enumerate(self.all_document_blocks):
            if (
                block["block_type"] == 3
                and block["heading1"]["elements"][0]["text_run"]["content"]
                == "家长留言区"
            ):
                self.message_heading_block_index = block_index
                print("家长留言区 index: ", self.message_heading_block_index)
                # The message_blocks_list does not contain the message title.
                self.message_blocks_list = self.all_document_blocks[
                    self.message_heading_block_index + 1 :
                ]
                break
        # The first message block index is the NEXT block of the "家长留言区".
        self.message_block_start_index = self.message_heading_block_index + 1
        # The first block is the document title (parent block) which could not be deleted.
        # Only the children blocks could be deleted.
        # The index is calculated based on children blocks.
        self.children_message_block_start_index = self.message_block_start_index - 1

    def __init__(
        self,
        notice_message_heading,
        notice_dir,
        document_id,
        app_id,
        app_secret,
        save_all_document_blocks_response_as_json=True,
    ) -> None:
        self.notice_dir = Path(notice_dir)
        self.notice_path = Path()
        self.notice_message_heading = notice_message_heading
        self.document_id = document_id
        tenant_access_token = self.obtainTenantAccessToken(app_id, app_secret)
        self.access_token = tenant_access_token
        self.all_document_blocks_response = None
        self.all_document_blocks = []
        self.all_block_ids = []
        # The first block is the document title
        self.message_heading_block_index = None
        self.message_block_start_index = None
        self.children_message_block_start_index = None
        self.message_blocks_list = []
        self.preprocessAllDocumentBlocks()
        script_dir = Path(__file__).resolve().parent
        all_document_blocks_response_path = (
            script_dir / "all_document_blocks_response.json"
        )
        if save_all_document_blocks_response_as_json is True:
            with open(all_document_blocks_response_path, "w+", encoding="utf8") as f:
                json.dump(self.all_document_blocks_response, f, ensure_ascii=False)

    def obtainPlainDocumentTextContent(self):
        url = (
            "https://open.feishu.cn/open-apis/docx/v1/documents/"
            + self.document_id
            + "/raw_content"
        )
        payload = ""
        access_token = "Bearer " + self.access_token
        headers = {"Authorization": access_token}
        response = requests.request("GET", url, headers=headers, data=payload)
        # print(response.text)
        response_json = json.loads(response.text)
        return response_json

    def updateBlock(self, block):
        block_id = block["block_id"]
        url = (
            "https://open.feishu.cn/open-apis/docx/v1/documents/"
            + self.document_id
            + "/blocks/"
            + block_id
        )
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        # print(f"formatted_time: {formatted_time}")
        block_element = block["text"]["elements"][0]
        block_element["text_run"]["content"] = (
            formatted_time + "【已通知】" + block_element["text_run"]["content"]
        )
        payload = json.dumps({"update_text_elements": {"elements": [block_element]}})

        access_token = "Bearer " + self.access_token
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json; charset=utf-8",
        }

        response = requests.request("PATCH", url, headers=headers, data=payload)
        if response.status_code == 200:
            response_json_data = response.json()
            response_json_element = response_json_data["data"]["block"]["text"][
                "elements"
            ][0]
            response_json_content = response_json_element["text_run"]["content"]
            print("updated block:", response_json_content)

    def checkNoticeExists(self):
        now = datetime.now()
        current_date = now.date()
        # print(f"current_date: {current_date}")
        notice_filename = str(current_date) + " 通知.docx"
        notice_path = self.notice_dir / Path(notice_filename)
        self.notice_path = Path(notice_path)
        if not notice_path.exists():
            notice_template_year_month = current_date.strftime("%Y-%m")
            notice_template_path = (
                self.notice_dir / f"{notice_template_year_month}-xx 通知.docx"
            )
            if notice_template_path.exists():
                notice_path.write_bytes(notice_template_path.read_bytes())

    def deliverAndReplyMessages(self):
        def is_after_yesterday_1900(text_message_notified_time):
            now = datetime.now()
            yesterday = now - timedelta(days=1)
            yesterday_19_00 = datetime(
                yesterday.year, yesterday.month, yesterday.day, 19, 00
            )
            yesterday_23_59 = datetime(
                yesterday.year, yesterday.month, yesterday.day, 23, 59, 59
            )
            return yesterday_19_00 < text_message_notified_time <= yesterday_23_59

        self.checkNoticeExists()
        pending_message_blocks_list = []
        for message_block_index, message_block in enumerate(
            self.all_document_blocks[self.message_block_start_index :],
            start=self.message_block_start_index,
        ):
            if message_block["block_type"] == 2:
                message_block_element = message_block["text"]["elements"][0]
                if (
                    18 < len(message_block_element["text_run"]["content"])
                    and message_block_element["text_run"]["content"][19:24]
                    == "【已通知】"
                ):
                    text_message_notified_time = datetime.strptime(
                        message_block_element["text_run"]["content"][:19],
                        "%Y-%m-%d %H:%M:%S",
                    )
                    if is_after_yesterday_1900(text_message_notified_time):
                        pending_message_blocks_list.append(message_block)
                        print("A message was left after 20:40 yesterday.")
                        continue
                    else:
                        pass
                elif message_block_element["text_run"]["content"] == "":
                    pass
                else:
                    pending_message_blocks_list.append(message_block)

        if len(pending_message_blocks_list) != 0:
            print("len(pending_message_blocks_list):", len(pending_message_blocks_list))
            notice = Document(self.notice_path)
            target_paragraph_text = self.notice_message_heading

            for paragraph_index, paragraph in enumerate(notice.paragraphs):
                if target_paragraph_text in paragraph.text:
                    for pending_message_block_index, pending_message_block in enumerate(
                        pending_message_blocks_list
                    ):
                        # Deliver messages
                        pending_message_block_element = pending_message_block["text"][
                            "elements"
                        ][0]
                        pending_message_element = pending_message_block_element[
                            "text_run"
                        ]["content"]
                        new_paragraph = notice.add_paragraph(pending_message_element)
                        # notice.paragraphs.insert(paragraph_index + 1, new_paragraph)
                        paragraph._p.addnext(new_paragraph._p)
                        notice.save(self.notice_path)
                        print(
                            f"delivered pending_message_element[{pending_message_block_index}]: {pending_message_element}"
                        )

                        # Reply messages
                        self.updateBlock(pending_message_block)

    def deleteBlocks(self, block_index):
        # The feishu official development document is weird.
        parent_block_id = self.document_id
        url = (
            "https://open.feishu.cn/open-apis/docx/v1/documents/"
            + self.document_id
            + "/blocks/"
            + parent_block_id
            + "/children/batch_delete"
        )
        payload = json.dumps(
            {
                "start_index": block_index,
                "end_index": block_index + 1,
            }
        )
        access_token = "Bearer " + self.access_token
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json; charset=utf-8",
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print("delete blocks response:", response.text)

    def deleteNotifiedMessages(self):
        def deleteBlankAndNotifiedMessageBLocks(deletion_indexes_list):
            # Delete blank and notified text messages.
            blank_message_block_indexes_list = []
            text_message_block_indexes_list = []
            notified_text_message_block_indexes_list = []
            # Delete all images if all text messages are notified.
            image_message_block_indexes_list = []
            for children_message_block_index, message_block in enumerate(
                self.message_blocks_list, start=self.children_message_block_start_index
            ):
                if message_block["block_type"] == 2:
                    message_block_element = message_block["text"]["elements"][0]
                    if message_block_element["text_run"]["content"] == "":
                        # Record all blank message blocks
                        blank_message_block_indexes_list.append(
                            children_message_block_index
                        )
                        print(
                            f"deletion blank block index: {children_message_block_index}"
                        )
                    else:
                        # Record all text message block indexes
                        text_message_block_indexes_list.append(
                            children_message_block_index
                        )
                        # Delete all notified text message blocks
                        if (
                            18 < len(message_block_element["text_run"]["content"])
                            and message_block_element["text_run"]["content"][19:24]
                            == "【已通知】"
                        ):
                            text_message_notified_time = datetime.strptime(
                                message_block_element["text_run"]["content"][:19],
                                "%Y-%m-%d %H:%M:%S",
                            )
                            # print(text_message_notified_time)
                            current_time = datetime.now()
                            time_difference = current_time - text_message_notified_time
                            time_difference_seconds = time_difference.total_seconds()
                            if 24 * 60 * 60 < time_difference_seconds:
                                notified_text_message_block_indexes_list.append(
                                    children_message_block_index
                                )
                                print(
                                    f"deletion text message: {message_block_element["text_run"]["content"]}"
                                )
                elif message_block["block_type"] == 27:
                    image_message_block_indexes_list.append(
                        children_message_block_index
                    )

            # Add blank message block indexes to the deletion list
            deletion_indexes_list += blank_message_block_indexes_list
            # Add notified text message block indexes to the deletion list
            deletion_indexes_list += notified_text_message_block_indexes_list
            # Add deletion image message block indexes to the deletion list
            if len(text_message_block_indexes_list) == len(
                notified_text_message_block_indexes_list
            ):
                deletion_indexes_list += image_message_block_indexes_list
            deletion_indexes_list.sort()
            return deletion_indexes_list

        if len(self.message_blocks_list) != 0:
            deletion_indexes_list = []
            deletion_indexes_list = deleteBlankAndNotifiedMessageBLocks(
                deletion_indexes_list
            )
            # print("origin deletion_indexes_list:", deletion_indexes_list)
            if len(deletion_indexes_list) != 0:
                deletion_indexes_array = np.asarray(deletion_indexes_list)
                # Feishu server executes the deletion step by step
                deletion_indexes_waiting_array = deletion_indexes_array - np.arange(
                    len(deletion_indexes_list)
                )
                deletion_indexes_waiting_list = deletion_indexes_waiting_array.tolist()
                for deletion_waiting_index in deletion_indexes_waiting_list:
                    print("deletion_waiting_index:", deletion_waiting_index)
                    self.deleteBlocks(deletion_waiting_index)
                    # pass


if __name__ == "__main__":
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"now: {formatted_time}")
    script_dir = Path(__file__).resolve().parent
    configuration_path = script_dir / "configuration.txt"
    with open(configuration_path, "r", encoding="utf-8") as file:
        txt_contents = file.read()
    notice_dir = re.findall(r"notice_dir:\s*(.*)", txt_contents)
    notice_message_heading = re.findall(r"notice_message_heading:\s*(.*)", txt_contents)
    document_id = re.findall(r"document_id:\s*(.*)", txt_contents)
    app_id = re.findall(r"app_id:\s*(.*)", txt_contents)
    app_secret = re.findall(r"app_secret:\s*(.*)", txt_contents)

    feishu_docs_api = FeishuDocsAPI(
        notice_message_heading[0],
        notice_dir[0],
        document_id[0],
        app_id[0],
        app_secret[0],
    )

    # with open("./all_document_blocks_response.json", "r", encoding="utf8") as f:
    #     all_document_blocks_response = json.load(f)

    feishu_docs_api.deliverAndReplyMessages()

    feishu_docs_api.deleteNotifiedMessages()
