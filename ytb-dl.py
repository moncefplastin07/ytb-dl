from pafy import new 
from os import path, environ, chdir, getcwd
import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url')
parser.add_argument('-t', '--type')
parser.add_argument('-d', '--downloaddir')
parser.add_argument('-c', '--config', action='store_true')
args = parser.parse_args()
APP_PATH = path.join(environ.get("USERPROFILE"), ".ytb-dl")
CONFIG_FILE_PATH = path.join(APP_PATH, "config.json")
config_file = open(CONFIG_FILE_PATH,)
  
# returns JSON object as 
# a dictionary
config = json.load(config_file)
if args.config and args.downloaddir:
    with open(CONFIG_FILE_PATH, "w") as outfile:
        config["download_dir"] = args.downloaddir
        json.dump(config, outfile)
        exit()

# Closing file
config_file.close()


chdir(args.downloaddir or (config.get("download_dir")) or './')


if args.url:
    url = args.url
else:
    url = input('Video Link: ')
video = new(url)

if args.type:
    mediaType  = args.type
else:
    mediaType = input('Video Or Audio (video|audio): ')


if mediaType.lower() == 'video':
    bestMediaQuality = video.getbestvideo()
elif mediaType.lower() == 'audio':
    bestMediaQuality = video.getbestaudio()
else:
    print('error this meida type note supported')
    exit()
print(f"File Name: {video.title} ({format(bestMediaQuality.get_filesize() / 1024 / 1024, '0.2f')} MB) ")
print(f"Download path: {path.join(getcwd(),video.title)}")
bestMediaQuality.download()