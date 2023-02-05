from pytube import YouTube

def getQuality(index):
	if index == 0:
		return "144p"
	if index == 1:
		return "244p"
	if index == 2:
		return "360p"
	if index == 3:
		return "480p"
	if index == 4:
		return "720p"
	if index == 5:
		return "1080p"
	if index == 6:
		return "1440p"



def DownloadVideo(videoObj, quality):
	print(f"Title : {videoObj.title}")
	print(f"DownloadQuality : {quality}")
	
	print("Fetching Video Streams", flush = True)
	streams = videoObj.streams


	# print("Finding Stream", flush = True)
	# stream = streams.filter(res=quality, progressive = True).first()
	# print("Stream Found, Download Started", flush = True)
	
	for s in streams:
		print(s)
	
	itag = int(input("Enter itag : "))
	
	stream = streams.get_by_itag(itag);
	print("Download Started", flush = True)
	stream.download();
	print("Download Done.", flush = True)
	



# Main Code

inputFile = open("link.txt", "r")
logFile = open("log.txt", "w")

qualityIndex = int(inputFile.readline())


link = inputFile.readline()

DownloadVideo(YouTube(link), getQuality(qualityIndex))









