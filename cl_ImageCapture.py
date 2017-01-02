# Class to conmtrol the use of the camera to cpature images
#

import subprocess
import io
from datetime import datetime
from PIL import Image


class ImageCapture:
    def __init__(self):
        # initialise function, needs to asign variables passed into the class and handle basic functions
        # this function is called everytime a class is initialised
        self.sample_width = sample_width
        self.sample_height = sample_height
        return

    def CaptureTestImage(sample_width, sample_height):
        # Capture a small image
        #TODO Need to put a 'try/except' loop around the capturing as the camera might not be working 
        command = "raspistill -w %s -h %s -t 0 -e bmp -n -o -" % (sample_width, sample_height)
        image_data = io.BytesIO()
        image_data.write(subprocess.check_output(command, shell=True))
        image_data.seek(0)
        im = Image.open(image_data)
        buffer = im.load()
        image_data.close()
       # print (buffer) # DEBUG
        return buffer
    

    def SaveImage(width, height):
        # Save a full size image to disk
        time = datetime.now()
        filename = "capture-%04d%02d%02d-%02d%02d%02d.jpg" % (time.year, time.month, time.day, time.hour, time.minute, time.second)
        subprocess.call("raspistill -w %s -h %s -t 0 -e jpg -n -q 15 -o %s" % (width, height, filename), shell=True)
        print ('Captured %s' % filename)

    
