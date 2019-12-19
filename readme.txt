-------------12/19/2019-----------------
modified code for testYolo

def testYolo():
	start darknet process in testudp mode

def fileitemDoubleClicked(self, item=None):
	called when a file item is double clicked
	call udpsnd.sh to send filename to the darknet process
	started at testYolo

	to debug, python udpsnd.sh, if a bad filename is sent, darknet
	will fail to open the file, but instead of die we just create
	a small all black image.

status: the canvas is not updating the correct image. only the first one
is shown correctly. fix by add cp cmd in udpsnd.sh so the detected result
is copied from darknet/ folder, 0.1 second delay should be enough for yolo
to finish. yet it is ugly but...


