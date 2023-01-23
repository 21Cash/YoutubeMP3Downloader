from pytube import YouTube

def log(str):
	logFile.write(str)
	logFile.write("\n")
	logFile.flush();

def DownloadMP3(s):
	yt = YouTube(s)


	print("Title : " + yt.title)
	log(f"Title : {yt.title}")

	print("Fetching the all Audio Files", flush = True)
	log(f"Getting The Audio Stream")
	streams = yt.streams.filter(only_audio=True)
	
	log("Streams Found")
	log("STREAMS: ")
	for s in streams:
		log(str(s))
		print(s)

	print("Getting The Stream", flush = True)

	stream = yt.streams.last()

	print("itag = " + str(stream.itag))
	
	log(f"Download Started, itag = {stream.itag}")
	
	print("Download Started", flush = True)

	stream.download()

	print("Download Done.")
	log("Download Completed.")


# Main Code

inputFile = open("link.txt", "r")
logFile = open("log.txt", "w")
DownloadMP3(inputFile.readline())

log("Program Terminated Safely.")






