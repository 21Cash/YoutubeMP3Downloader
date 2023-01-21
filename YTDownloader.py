from pytube import YouTube


inputFile = open("input.txt", "r")
logFile = open("log.txt", "w")



yt = YouTube(inputFile.readline())


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

