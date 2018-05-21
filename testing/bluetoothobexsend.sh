#!/usr/bin/expect -f

spawn obexctl
expect ">>"
send "connect 94:65:2D:7D:2D:98\r"
expect ">>"
send "send /home/pi/photobox/testing/test.txt\r"
expect ">>"
send "quit\r" 
