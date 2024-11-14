# Banzhuren Notifier

## Environment

All PCs are connected to LAN.

## Usage

1. Download all files.
2. Create a `configuration.txt`.
3. Configure the `configuration.txt`.
4. Create an automated task using Task Scheduler to run the `run-minimized.bat` three minutes after classes. (The three minutes are redundant for the teacher to finish the class.)
5. Create an automated task using Task Scheduler to run the `close-wps.bat` three minutes before classes.

## Configuration

```bash
# The name of your PC
hostname:

# The username to log in your PC remotely
username:

# The password to log in your PC remotely
password:

# The shared folder where the notice file is
sharedFolder:
```

## Function

For instance, today's notice, `2024-11-11 通知.docx`, is supposed to be opened automatically based on the schedule.
