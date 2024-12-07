# Banzhuren Notifier

## Environment

All PCs are connected to LAN.

## Usage

1. Download all files.
2. Create a `configuration.txt`.

### Openning the notice automatically

1. Configure the `configuration.txt`.
2. Create an automated task using **Task Scheduler** to run the `run_minimized.bat` three minutes after classes. (The three minutes are redundant for the teacher to finish the class.)
3. Create an automated task using **Task Scheduler** to run the `close_wps.bat` three minutes before classes.

### Centralized and automatic processing of parents' messages

1. Use Feishu docx template [家长留言自动通知文档（模板）](https://qy42rjhota.feishu.cn/docx/O4kada7O3oykOax11xDcGLlDnYf).
2. Configure the `configuration.txt`.
3. Create an automated task using **Task Scheduler** to run the `run_feishu_server_api.bat` about two minutes before running the `run_minimized.bat`.

## Configuration

```bash
# Parameters for `.bat` files
# The name of your PC or the IP address
HOSTNAME:

# The username to log in your PC remotely
USERNAME:

# The password to log in your PC remotely
PASSWORD:

# The shared folder where the notice file (.docx) is
SHARED_FOLDER:

# Parameters for Python
# The shared PATH where the notice file (.docx) is 
# For instance: C:\Users\Desktop\Editable Folder
notice_dir:

# The heading which you want the parents messages to be put below
notice_message_heading:

# Feishu document (production version) id
document_id:

# Feishu document (development version) id
dev_document_id:

# The app_id of the Feishu document app Parents' Messages Processor
app_id:

# The app key of the Feishu document app Parents' Messages Processor
app_secret:
```

## Functions

For instance, today's notice, `2024-11-11 通知.docx`, is supposed to be opened automatically based on the schedule.

In addition, parents' messages left on the Feishu document are supposed to be delivered to today's notice. Besides, an annotation demonstrating that the corresponding message is delivered successfully will be add to the beginning of the message. Messages will be deleted when they were delivered 24 hours ago.

## P.S

If you are a teacher working in Dongguan Experimental Middle School, I am willing to help you set all things up hand in hand.
