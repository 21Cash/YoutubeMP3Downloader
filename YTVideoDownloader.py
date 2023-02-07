import time
import datetime
from pytube import YouTube
from tqdm import tqdm

class Timer:
	def __init__(self):
		self.start = 0
		self.end = -1
	def Start(self):
		self.start = time.time();
	def Stop(self):
		end = time.time();
		return (end - self.start);

class ProgressBar(object):  # Python3+ '(object)' can be omitted
    def __init__(self, max_value, disable=True):
        self.max_value = max_value
        self.disable = disable
        self.p = self.pbar()

    def pbar(self):
        return tqdm(
            total=self.max_value,
            desc='Downloading: ',
            disable=self.disable
        )
       
    def update(self, update_value):
        self.p.update(update_value)
    def setValue(self, val):
    	self.p.n = val
    	self.p.refresh()
    def close(self):
        self.p.close()
       



def getFormattedTime(curTime):
	_str = f"{curTime.day} / {curTime.month} / {curTime.year}, [{curTime.hour} : {curTime.minute} : {curTime.second}]" 
	return _str 

def getCurrentTime():
	return getFormattedTime(datetime.datetime.now())

def getMs(timeInSeconds):
	return int(timeInSeconds * 1000)

def writeLineToLog(str):
	logFile.write(getCurrentTime() + "  :  " + str)
	logFile.write("\n")
	logFile.flush()

def log(str):
	print(str, flush = True)
	logFile.write(getCurrentTime() + "  :  " + str)
	logFile.write("\n")
	logFile.flush()
def writeLog(str):
	logFile.write(getCurrentTime() + "  :  " + str)
	logFile.write("\n")
	logFile.flush()

def progress_callback(stream, chunk , bytes_remaining):
    size = stream.filesize
    progress = (float(abs(bytes_remaining-size)/size))*float(100)
    toSet = (stream.filesize - bytes_remaining) * 0.000001
    curBar.setValue(toSet)
    

def DownloadVideo(s, resString):
	
	yt = YouTube(s, on_progress_callback=progress_callback)
	# yt.register_on_complete_callback(on_complete_callback)
	log(f"Title : {yt.title}")

	log(f"Fetching The Video Streams")
	
	streams = yt.streams.filter(progressive=True, res=resString)
	
	writeLog("Streams: ")
	for s in streams:
		writeLog(f"itag : {s.itag}, res : {s.resolution}, FileSize : {s.filesize_mb} MB")
	print("\n")
	# tag = int(input("Enter itag : "))
	tag = -1
	for s in streams:
		if s.resolution == resString:
			tag = s.itag
			break
	if tag == -1:
		log(f"No Stream Found With Quality : {resString}")
		
	stream = streams.get_by_itag(tag)	
	
	writeLog("Downloading Stream with itag = " + str(stream.itag))
	
	log(f"FileSize : {round((stream.filesize) / (1024 * 1024), 2)} MB")
	
	
	assignProgressBar(stream.filesize_mb)
	print("\n")
	stream.download()
	curBar.setValue(stream.filesize_mb)
	print("\nDownload Complete", flush=True)	

	
def assignProgressBar(maxVal):
	global curBar 
	curBar = ProgressBar(max_value=maxVal, disable=False)
	writeLineToLog("Assigned new Download progress bar")
	
def mainCode():
	# Main Code
	timer = Timer()
	timer.Start()

	linkStr = inputFile.readline()
	resStr = inputFile.readline()	
		
	DownloadVideo(linkStr, resStr)
	
	t = timer.Stop()

	writeLog(f"Execution Time : {round(t, 2)} seconds ({getMs(t)} ms)")

	writeLog("Program Terminated Safely.")
	



	
	
inputFile = open("link.txt", "r")
logFile = open("log.txt", "w")
curBar = None

try:
	mainCode()
except Exception as Argument:
	log(str(Argument))

print("Enter Any Key to exit", flush=True)
input()
