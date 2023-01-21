from pytube import YouTube


inputFile = open("input.txt", "r")
logFile = open("log.txt", "w")



yt = YouTube(inputFile.readline())


print("Title : " + yt.title)


print("Fetching the all Audio Files", flush = True)
streams = yt.streams.filter(only_audio=True)

for s in streams:
	print(s)




print("Input itag", flush = True)
itag = int(input())

print("Getting The Stream", flush = True)

stream = yt.streams.get_by_itag(itag)

print("Download Started", flush = True)

stream.download()

print("Download Done.")

