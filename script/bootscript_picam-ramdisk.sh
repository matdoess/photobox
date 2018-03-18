#!/bin/bash


# RAMDISK Ordner & Verknüpfungen anlegen
DEST_DIR=/home/pi/picam
SHM_DIR=/run/shm
VIDEO_DIR=/home/pi/photobox/pics/videos

mkdir -p $SHM_DIR/rec
mkdir -p $SHM_DIR/hooks
mkdir -p $SHM_DIR/state
mkdir -p $VIDEO_DIR

ln -sfn $VIDEO_DIR $SHM_DIR/rec/archive
ln -sfn $SHM_DIR/rec $DEST_DIR/rec
ln -sfn $SHM_DIR/hooks $DEST_DIR/hooks
ln -sfn $SHM_DIR/state $DEST_DIR/state
