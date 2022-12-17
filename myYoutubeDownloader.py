from pytube import YouTube

def DownloadVideo(link):
    try:
        yt = YouTube(link)
        str = "YOUTUBE VIDEO DESCRIPTION : \n{}\nLENGTH OF VIDEO : {} mins".format(yt.description,(yt.length/60))
        print(str)
        print('\nCaptions :',yt.captions)
        ytstream=yt.streams
        # for entire video
        ytstream.get_highest_resolution().download()
        # for only audio
        # ytstream.get_audio_only().download()     
        print('Downloaded Successfully-- ', yt.title)
    except Exception as ex:
        print('Download failed : {}',ex)

# sample test
# link='https://www.youtube.com/watch?v=bvWRMAU6V-c'
# DownloadVideo(link)

print('Enter youtube url:')
DownloadVideo(input())
