#!/bin/bash

#Automated Backup Script

#Project Overview: Create a Bash script that automates the process of backing up important files or directories from your computer to a remote server or a cloud storage service (like Google Drive, AWS S3, or an FTP server).

#Core Features:

    #Source & Destination Configuration: Allow the user to specify the directories/files to back up and where to store the backup (local or remote server).
    #Scheduling: Automate the backup to run on a schedule (e.g., daily or weekly) using cron.
    #Compression: Compress the backup into a .tar.gz or .zip archive to save storage space.
    #Encryption (Optional): Encrypt backups using gpg or openssl to ensure data security.
    #Logging: Maintain a log file to track each backup process (successes, errors, and timestamps).
    #Notification: Send a notification (email or desktop) when the backup is complete or if there's an error.

# bash backup.sh source destination

source=$1
destination=$2

# to do : config

date_backup=$(date +'%Y-%m-%d')
tar -cvzf $2_$backup_$date_backup.tar.gz $1

# Log
date >> log_backup.log
