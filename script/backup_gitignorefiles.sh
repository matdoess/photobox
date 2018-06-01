#!/bin/bash

rsync -av --progress --exclude-from=/home/pi/photobox/script/backup_gitignorefiles.list /home/pi/photobox /home/pi/photobox_storage_backup/
