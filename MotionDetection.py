# Main window for the motion detection

'''
While watching for motion it pipes a thumbnail image from raspistill at around 1fps to analyse (it keeps everything in memory to avoid wearing out the SD card). Once motion is detected it calls raspistill again to write a high-res jpeg to disk.

It also checks free disk space and if under a set limit it starts to delete the oldest images to make sure there is always enough free space for new images.

While running on my rev1 B it consumes around 12% CPU / 4% ram and manages to capture a full size image once ever 2-3 secs.
'''

# import classes
from cl_DiskOperations import *
from cl_ImageCapture import *


import subprocess
from datetime import datetime
from datetime import timedelta


# Motion detection settings:
# threshold - how much a pixel has to change by to be marked as "changed"
# sensitivity - how many changed pixels before capturing an image
# Force an image to be captured every force_capture_time seconds
threshold = 10
sensitivity = 20
force_capture_time = 60 * 60 # Once an hour, in seconds

# sample image sizes
sample_width = 100
sample_height = 75

# Image settings
save_width = 1280
save_height = 960

# file settings
disk_space_to_reserve = 40 * 1024 * 1024 # Keep 40 mb free on disk




# Get first image
image1 = ImageCapture.CaptureTestImage(sample_width, sample_height)

# Reset last capture time
last_capture = datetime.now()

while (True):

  # Get comparison image
  image2 = ImageCapture.CaptureTestImage(sample_width, sample_height)

  # Count changed pixels
  changed_pixels = 0
##  for x in range(0, sample_width):
##    for y in range(0, sample_height):
##    # Just check green channel as it's the highest quality channel
##      pixdiff = abs(image1[x,y][1] - image2[x,y][1])    
##      if pixdiff > threshold:
##        changed_pixels += 1
##    # will loop round whole image before exiting. could exit when enough pixels have changed

  x = 0
  y = 0
  while x < 100 and y < 75:
    pixdiff = abs(image1[x,y][1] - image2[x,y][1])    
    if pixdiff > threshold:
      changed_pixels += 1
    x += 1
    if x == 100:
      y += 1
      x = 0
##      print ("x is 100", x, ":", y)  #DEBUG
    if changed_pixels > sensitivity:
##      print ("above threshold", x, ":", y)  #DEBUG
      break
##    print ("counter", x, ":", y)  #DEBUG
    

# Force a capture every force_time_capture duration
  if datetime.now() - last_capture > timedelta(seconds = force_capture_time):
    changed_pixels = sensitivity + 1

# Save an image if pixels changed
  if changed_pixels > sensitivity:
    last_capture = datetime.now()
    DiskOperations.KeepDiskSpaceFree(disk_space_to_reserve)
    ImageCapture.SaveImage(save_width, save_height)

  # Swap comparison buffers
  image1 = image2
 
