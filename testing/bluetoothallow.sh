#!/bin/bash

sudo bluetoothctl <<EOF
power on
discoverable on
pairable on
agent NoInputNoOutput
EOF
