from pytube import YouTube
from pytube import Playlist


def DownloadMP3File(YTObj):
	
	yt = YTObj


	print("Title : " + yt.title)


	print("Fetching the all Audio Files", flush = True)
	streams = yt.streams.filter(only_audio=True)

	for s in streams:
		print(s)

	print("Getting The Stream", flush = True)

	stream = yt.streams.last()

	print("itag = " + str(stream.itag))

	print("Download Started", flush = True)

	stream.download()

	print("Download Done.")
	print("\n")



def PrintPlayListStats(playList):
	print("Playlist Size : " + str(playList.length))
		
def DownloadPlayList(p):
	for video in p.videos:
		DownloadMP3File(video)
		

# Main Code

inputFile = open("link.txt", "r")
logFile = open("log.txt", "w")


p = Playlist(inputFile.readline())


PrintPlayListStats(p)
DownloadPlayList(p)


