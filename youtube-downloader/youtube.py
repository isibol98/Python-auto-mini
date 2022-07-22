#!/usr/bin/env python3
import youtube_dl

ydl_options = {}
link = input("Link: ")
with youtube_dl.YoutubeDL(ydl_options) as ydl:
    ydl.download([link])