# Import the necessary modules
import os
import subprocess
import telegram_send

# Set the database to be backed up
db_name = 'my_database_name'

# Set the directory where the backup will be saved
backup_dir = '/path/to/backup/directory'

# Set the filename for the backup
backup_file = '{}-backup.zip'.format(db_name)

# Create the backup command
backup_cmd = 'odoo-bin -d {} -o -r admin -w admin --db_host=localhost --db_port=8069 --db_user=odoo --db_password=odoo --addons-path=../odoo/addons -r admin -w admin -b {} -f {}'.format(db_name, backup_dir, backup_file)

# Try to run the backup command
try:
    subprocess.run(backup_cmd, shell=True)
    # Send a notification message
    telegram_send.send(messages=['Odoo backup completed successfully.'])

# Catch any errors that occur
except Exception as e:
    # Send a notification message with the error details
    telegram_send.send(messages=['Odoo backup failed with error: {}'.format(e)])



## Cron job

## 0 * * * * python /path/to/script/odoo_backup.py

