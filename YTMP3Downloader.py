import time
import datetime
from pytube import YouTube

class Timer:
	def __init__(self):
		self.start = 0
		self.end = -1
	def Start(self):
		self.start = time.time();
	def Stop(self):
		end = time.time();
		return (end - self.start);




def getFormattedTime(curTime):
	_str = f"{curTime.day} / {curTime.month} / {curTime.year}, [{curTime.hour} : {curTime.minute} : {curTime.second}]" 
	return _str 

def getCurrentTime():
	return getFormattedTime(datetime.datetime.now())

def getMs(timeInSeconds):
	return int(timeInSeconds * 1000)


def log(str):
	print(str, flush = True)
	logFile.write(getCurrentTime() + "  :  " + str)
	logFile.write("\n")
	logFile.flush();
 

def DownloadMP3(s):
	
	yt = YouTube(s)
	log(f"Title : {yt.title}")

	log(f"Fetching The Audio Streams")
	
	streams = yt.streams.filter(only_audio=True)
	
	log("\n");
	log("Streams: ")
	for s in streams:
		log(str(s))
	log("\n")

	stream = yt.streams.last()
	
	log("Downloading Stream with itag = " + str(stream.itag))
	
	log(f"FileSize : {round((stream.filesize) / (1024 * 1024), 2)} MB")
	
	log(f"Download Started, itag = {stream.itag}")
	

	stream.download()

	log("Download Completed.")


def mainCode():
		# Main Code
	timer = Timer()
	timer.Start()


	
	DownloadMP3(inputFile.readline())

	t = timer.Stop()

	log(f"Execution Time : {round(t, 2)} second ({getMs(t)} ms)")

	log("Program Terminated Safely.")
	input()




inputFile = open("link.txt", "r")
logFile = open("log.txt", "w")

try:
	mainCode()
except Exception as Argument:
	log(str(Argument))



