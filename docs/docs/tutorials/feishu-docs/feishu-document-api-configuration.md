---
slug: feishu-document-api-configuration
description: 班主任电脑配置【自动】搬运家长留言的指南。
sidebar_position: 4
---

# 配置自动搬运家长留言

## 在班主任电脑上

1. 将文件夹【`banzhuren-notifier`】里面 `cofiguration_template.txt` 重命名为 `configuration.txt`。
2. 打开 `configuration.txt`。
3. 找到并填写如下几个值：

    ```bash
    notice_dir=

    document_id=
    ```

    - `notice_dir` 为班主任电脑中，通知 Word 模板 `2025-01-xx 通知.docx` 所在的【绝对路径】。

        - 您可以打开【我的电脑】，找到通知 Word 模板 `2025-01-xx 通知.docx` 所在的文件夹，直接复制顶上的地址。

        ![获取 notice_dir](/img/copy-notice-dir.png)

    - `document_id` 为您的 `家长留言自动通知文档（马冬梅）` 的唯一标识。

        - 您需要在浏览器中打开文档，在地址栏中获取文档的 `document_id`。

        ![获取 document_id](https://sf3-cn.feishucdn.com/obj/open-platform-opendoc/f8dac29d8ea3f01f5a651e0445193213_W0CZqRcbHM.png)

    填写完成之后大概长这样：

    ```bash
    notice_dir=D:\Users\Desktop\可编辑文件夹

    document_id=Ke6jdf477ohCVVxzANnc56WYnrd
    ```

    :::warning

    暂时请勿修改其他值！

    :::

4. 打开【任务计划程序】。

    - 如果任务栏有搜索框：

        - 在任务栏的搜索框中，键入【任务计划程序】，然后选择【任务计划程序】。

    - 如果任务栏无搜索框：

        - 按住【Win】键，再按【Q】键。
        - 在弹出来的搜索框中，键入【任务计划程序】，然后选择【任务计划程序】。

    - 打开【任务计划程序】之后这个东西大概长这样：

        ![Task Scheduler](/img/task-scheduler.png)

        - 在上面的图片上按鼠标的【右键】，点击【在新标签页中打开图像】，可以全屏查看图片。

5. 点击右边的【创建任务】。
6. 在弹出的窗口中，【常规】下面的【名称】随便填。
7. 点击【触发器】，点击【新建】。

    ![Create a Task](/img/create-a-task.png)

8. 在弹出的【新建触发器】窗口中，设置你希望家长在 `家长留言自动通知文档（马冬梅）` 中通过【评论】写下的留言，什么时候被自动搬运到当天的班主任通知（如 `2025-01-02 通知.docx`）中。

    比如，你希望从每天的 06:30 开始，每隔 30 min 就自动将家长通过【评论】写下的留言，自动搬运到当天的班主任通知中，那就设置成下面图片这样：

    ![Create a Feishu API Trigger](/img/create-a-feishu-api-trigger.png)

    :::warning 建议

    尽量不要设置成和【[自动传递班主任通知——配置自动打开通知](../bat/openning-configuration.md)】中设置的时间冲突，有可能产生意料之外的错误。

    :::

9. **上一步设置的【触发器】可以设置多个！**

    如果您希望在很多个时刻自动搬运家长留言到班主任当天的通知中，就设置很多个对应的【触发器】。

10. 设置完【触发器】之后，点击【操作】，点击【新建】。

    ![Operation](/img/operation.png)

11. 在弹出来的【新建操作】窗口中，点击【浏览】。

    ![Create an Operation](/img/create-an-operation.png)

12. 找到在【班主任电脑】中的文件夹【`banzhuren-notifier`】中的 `run_feishu_server_api` 或者 `run_feishu_server_api.bat` 文件，点击【打开】。

    ![Run Feishu Server API](/img/run-feishu-server-api.png)

13. 一路【确定】回到【任务计划程序】界面。

    ![Task Scheduler](/img/task-scheduler.png)

:::tip 恭喜！

理论上，现在班主任的电脑已经可以【自动】根据设置的时间（如每隔 30 min），将家长通过【评论】写下的留言，搬运到班主任当天的通知 Word 文档中（如 `2025-01-02 通知.docx`）了。

:::

:::info

搬运后的家长留言，会在飞书文档的【家长留言区】下面，留下记录，如：

> 2024-11-30 12:34:56【已通知】请 XXX 打电话给家长。

:::

:::tip

班主任【无需】手动每天新建当天的通知 Word 文档。

只要通知 Word 模板 `2025-01-xx 通知.docx` 存在并且上面步骤的设置没出问题，工具能根据【通知 Word 模板】自动新建当天的通知 Word 文档，再自动搬运家长的留言。

:::

:::tip

班主任是 `家长留言自动通知文档（马冬梅）` 的管理员，班主任可以像家长一样使用【评论】进行留言，班主任也可以直接在【家长留言区】下面直接留言。

两种方式的留言，都会被自动搬运到当天的通知 Word 文档之中。

:::

## 在班主任电脑上（进阶）

### 配置通知 Word 文档的【通知标题】

1. 进入文件夹【`banzhuren-notifier`】。
2. 打开 `configuration.txt`，您会发现：

    ```bash
    notice_message_heading=通知栏
    ```

3. 打开飞书文档 `家长留言自动通知文档（马冬梅）`，您会发现：

    ![Notice Example](/img/notice-example.png)

    :::note

    没错，`configuration.txt` 里面 `notice_message_heading` 的值，和通知 Word 文档里面的【通知标题】是一样的。

    :::

:::warning

如果您不喜欢用“通知栏”这几个字，进行修改的时候，

记得同时改 `configuration.txt` 和 通知 Word 模板 `2025-01-xx 通知.docx`【两个】地方！

:::

### 配置“家长留言自动通知文档”（飞书文档）的【留言标题】

1. 进入文件夹【`banzhuren-notifier`】。
2. 打开 `configuration.txt`，您会发现：

    ```bash
    message_heading_text=家长留言区
    ```

3. 打开飞书文档 `家长留言自动通知文档（马冬梅）`，您会发现：

    ![添加文档应用](/img/add-a-document-application.png)

    :::note

    没错，`configuration.txt` 里面 `message_heading_text` 的值，和飞书文档里面的一级标题【家长留言区】是一样的。

    :::

:::warning

如果您不喜欢用“家长留言区”这几个字，进行修改的时候，

记得同时改 `configuration.txt` 和飞书文档 `家长留言自动通知文档（马冬梅）`【两个】地方！

:::

## 在班主任手机上（进阶）

1. 班主任已经按上述步骤进行配置。
2. **班主任的电脑开着！**
3. 班主任（不在办公室甚至不在学校）使用手机，通过分享给家长们的链接，访问 `家长留言自动通知文档（马冬梅）`。
4. 班主任像家长一样，通过【评论】留下给同学们的通知。工具能自动将班主任的通知留言，抓取到当天的通知 Word 文档之中。
5. 工具根据班主任的配置，自动将当天的通知 Word 文档展示给同学们。
6. 实现超级远距离通知。
