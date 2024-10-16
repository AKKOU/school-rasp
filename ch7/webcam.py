import time
import os
import datetime

d1 = time.strftime("%Y_%m_%d-%H_%M_%S")
action = "fswebcam -r 960x720 -d /dev/video0 /home/pi/jpg/" + d1 + ".jpg"
os.system(action)
action1 = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/jpg/" + d1 + ".jpg /"
os.system(action1)