#!/usr/bin/env python

import subprocess
import boto3
from telegram import Bot
from telegram.error import TelegramError
import os

# Set the URL of the Odoo instance to backup
odoo_url = "http://localhost:8069"

# Set the filepath for the backup file
backup_filepath = "/path/to/backup/file.dump"

# In the same directory
# backup_filepath = os.path.join(os.path.dirname(__file__), "file.dump")


# Set the name of the S3 bucket where the backup will be uploaded
s3_bucket_name = "YOUR_BUCKET_NAME"

# Set the API token for the Telegram bot
telegram_api_token = "YOUR_API_TOKEN"

# Set the chat ID for the Telegram chat where notifications will be sent
telegram_chat_id = "YOUR_CHAT_ID"

# Use curl to create a backup of the Odoo instance
subprocess.run(["curl", "-X", "POST", '-F', 'master_pwd=yourpassword', '-F', 'name=dbname', '-F', 'backup_format=zip', '-o', backup_filepath, 'http://localhost:8069/web/database/backup'])


# Check the exit code of the curl command to make sure the backup was successful
if subprocess.run(["curl", "-X", "POST", '-F', 'master_pwd=yourpassword', '-F', 'name=dbname' '-F', 'backup_format=zip', '-o', backup_filepath, 'http://localhost:8069/web/database/backup']).returncode == 0:
    # Upload the backup file to S3
    s3 = boto3.client("s3")
    with open(backup_filepath, "rb") as data:
        s3.upload_fileobj(data, s3_bucket_name, backup_filepath)
        print("Odoo backup uploaded to S3 successfully!")

        # Send a success message using the Telegram bot
        try:
            bot = Bot(telegram_api_token)
            bot.send_message(telegram_chat_id, "Odoo backup created and uploaded to S3 successfully!")
        except TelegramError as e:
            print(e)
else:
    # Send a failure message using the Telegram bot
    try:
        bot = Bot(telegram_api_token)
        bot.send_message(telegram_chat_id, "Odoo backup failed")
    except TelegramError as e:
        print(e)
