# class to perform disk operations

import os
import sys

class DiskOperations:
    def __init__(self):
        return

    def GetFreeSpace():
        # Get available disk space
        st = os.statvfs(".")
        du = st.f_bavail * st.f_frsize  # number of blocks multiplied by block size
        # print ('Space available %s' % du)  #DEBUG
        return du
    
    def KeepDiskSpaceFree(bytes_to_reserve):
    #   Keep free space above given level
        if (DiskOperations.GetFreeSpace() < bytes_to_reserve):
            for filename in sorted(os.listdir(".")):
                if filename.startswith("capture") and filename.endswith(".jpg"):
                    os.remove(filename)
                    print ('Deleted %s to avoid filling disk' % filename)
                    if (DiskOperations.GetFreeSpace() > bytes_to_reserve):
                        return
                    else:
                        print ('Insufficient Disk Space, capture aborted')
                        # print ('Bytes to reserve %s' % bytes_to_reserve)  #DEBUG
                        sys.exit()



