## Logic 

The script itself is simple. We will use subprocess to run the back up command. 
We will then send the backup to an s3 bucket, and alert by telegram. After that use cron to run it every x time. 


## PIP Requirments 

Here is the packages you will need. 

```python3
import subprocess
import boto3
from telegram import Bot
from telegram.error import TelegramError
import os
```

## HOW TO RUN 

Clone the script and then in the terminal. 

```python3
python3 odoo_curl_backup.py
```
