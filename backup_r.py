# Import the necessary modules
import os
import subprocess

# Set the database to be backed up
db_name = 'my_database_name'

# Set the directory where the backup will be saved
backup_dir = '/path/to/backup/directory'

# Set the filename for the backup
backup_file = '{}-backup.zip'.format(db_name)

# Create the backup command
backup_cmd = 'odoo-bin -d {} -o -r admin -w admin --db_host=localhost --db_port=8069 --db_user=odoo --db_password=odoo --addons-path=../odoo/addons -r admin -w admin -b {} -f {}'.format(db_name, backup_dir, backup_file)

# Run the backup command
subprocess.run(backup_cmd, shell=True)


## Cron job

## 0 * * * * python /path/to/script/odoo_backup.py

