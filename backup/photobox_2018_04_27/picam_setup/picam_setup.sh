#!/bin/bash

# If you have not enabled camera, enable it with raspi-config then reboot
#sudo raspi-config

# Install dependencies
sudo apt-get update
sudo apt-get install libharfbuzz0b libfontconfig1

# Create directories and symbolic links
cat > make_dirs.sh <<'EOF'
#!/bin/bash
DEST_DIR=~/picam
SHM_DIR=/run/shm

mkdir -p $SHM_DIR/rec
mkdir -p $SHM_DIR/hooks
mkdir -p $SHM_DIR/state
mkdir -p $DEST_DIR/archive

ln -sfn $DEST_DIR/archive $SHM_DIR/rec/archive
ln -sfn $SHM_DIR/rec $DEST_DIR/rec
ln -sfn $SHM_DIR/hooks $DEST_DIR/hooks
ln -sfn $SHM_DIR/state $DEST_DIR/state
EOF

chmod +x make_dirs.sh
./make_dirs.sh

# Optionally, increase microphone volume with alsamixer
read -p "Optionally, increase microphone volume with alsamixer. Press ENTER to continue."
alsamixer

# Install picam binary
wget https://github.com/iizukanao/picam/releases/download/v1.4.6/picam-1.4.6-binary-stretch.tar.xz
tar xvf picam-1.4.6-binary-stretch.tar.xz
cp picam-1.4.6-binary-stretch/picam ~/picam/
