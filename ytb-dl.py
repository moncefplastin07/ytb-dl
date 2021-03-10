from pafy import new 
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--url')
parser.add_argument('--type')
args = parser.parse_args()


if args.url:
    url = args.url
else:
    url = input('Video Link: ')
video = new(url)

if args.type:
    mediaType  = args.type
else:
    mediaType = input('Video Or Audio (video|audio): ')


if mediaType.lower() == 'vedio':
    bestVideoQuality = video.getbestvideo()
    bestVideoQuality.download()
elif mediaType.lower() == 'audio':
    bestAudioQuality = video.getbestaudio()
    bestAudioQuality.download()
else:
    print('error')
