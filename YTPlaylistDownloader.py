import time
import datetime
from pytube import YouTube
from pytube import Playlist

class Timer:
	def __init__(self):
		self.start = 0
		self.end = -1
	def Start(self):
		self.start = time.time();
	def Stop(self):
		end = time.time();
		return (end - self.start);


def getProgress(curVal, totalVal):
	return (curVal / totalVal) * 100

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
 

def DownloadMP3(YTObj):
	
	yt = YTObj
	log(f"Title : {yt.title}")

	log(f"Fetching The Audio Streams")
	
	streams = yt.streams.filter(only_audio=True)
	

	stream = yt.streams.last()
	
	# log("Downloading Stream with itag = " + str(stream.itag))
	
	log(f"FileSize : {round((stream.filesize) / (1024 * 1024), 2)} MB")
	
	log(f"Download Started")
	

	stream.download()

	log("Download Completed.")

def PrintPlayListStats(playList):
	log("Playlist Size : " + str(playList.length))
	
	
	
def DownloadPlaylist(linkStr):
	p = Playlist(linkStr)
	PrintPlayListStats(p)
	
	
	
	count = 0
	totalTrackCount = p.length
	
	for track in p.videos:
		log(f"Track : {count+1}")
		DownloadMP3(track)
		count += 1
		print(f"{round(getProgress(count, totalTrackCount), 2)}% Complete")
		log("\n")
		
	
def mainCode():
	# Main Code
	
	timer = Timer()
	timer.Start()


	
	DownloadPlaylist(inputFile.readline())

	t = timer.Stop()

	log(f"Execution Time : {round(t, 2)} seconds ({getMs(t)} ms)")

	log("Program Terminated Safely.")
	input()




inputFile = open("link.txt", "r")
logFile = open("log.txt", "w")

try:
	mainCode()
except Exception as Argument:
	log(str(Argument))



