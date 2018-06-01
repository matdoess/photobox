#!/bin/bash

rsync -av --progress --exclude=/lost+found/ /home/pi/photobox/pics/ /home/pi/photobox_storage_backup/
