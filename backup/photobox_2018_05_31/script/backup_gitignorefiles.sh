#!/bin/bash

rsync -av --progress --exclude-from=backup_gitignorefiles.list /home/pi/photobox /home/pi/photobox_storage_backup/
