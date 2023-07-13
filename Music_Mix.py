# Made By- Arjun Khanchandani Roll No. 102017005 Group- 3CS1 Mashup Project         

import numpy as np

from pytube import Search
from pytube import YouTube
import moviepy.editor as me

import os
import sys

def download_videos_youtube():

    n = len(sys.argv) # Number of system arguments

    if n != 5:
        print("The number of parameters passed are not accuate, the input format should be python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        quit()

    x = sys.argv[1] # Name of The Singer

    try:
        n = int(sys.argv[2]) # Number of Videos to be downloaded
    except:
        print("Number of videos should be numeric")
        quit()

    try:
        d = int(sys.argv[3]) # Duration of the videos
    except:
        print("Duration of each video should be numeric") # Given Condition
        quit()
    
    output_file = sys.argv[4] # Name of the Output File

    if n < 10:
        print("Number of videos must be greater than 10 (TEN)")     # Given Condition
        quit()

    if d < 20:
        print("Duration of videos must be greater than 20 (TWENTY) seconds")    # Given Condition
        quit()

    if not os.path.exists(x):
        os.mkdir(x)

    query = x + " official music videos" # Query to be searched

    searches = Search(query)

    i = 0

    #print(len(searches.results))
    #print(searches.results)

    searches.results
    searches.get_next_results()     # Get additional results
    #print(len(searches.results))
    #print(searches.results)

    searches.results
    searches.get_next_results()     # Get additional results
    #print(len(searches.results))
    #print(searches.results)

    searches.results
    searches.get_next_results()     # Get additional results
    #print(len(searches.results))
    #print(searches.results)

    for video in searches.results:
        if i < n:

            if(video.length < 960):

                youtubeObject = YouTube(video.watch_url)

                try:
                    youtubeObject = youtubeObject.streams.get_highest_resolution().download(x, filename=f"{i}.mp4") # Videos are downloaded here
                    print(f"Video {i + 1}: {video.title} has been Downloaded")
                    i = i + 1

                except:
                    print("Some Error has Occured")

    for k in range(0, n):
            clip = me.VideoFileClip(f"{x}/{k}.mp4").subclip(0, d)
            clip.audio.write_audiofile(f"{x}/{k}.mp3")


    audio_files = [me.AudioFileClip(f"{x}/{k}.mp3") for k in range(0,n)]
    res = me.concatenate_audioclips(audio_files)
    res.write_audiofile(output_file)



#x = input("Enter the name of the singer you want to search: \n")
#n = int(input("Enter the number of videos to be downloaded: \n"))
#d = input("Enter duration of each video which is downloaded: \n")

download_videos_youtube()
