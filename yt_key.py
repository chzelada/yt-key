# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 06:44:45 2016

@author: chzelada
"""

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import argparse

DEVELOPER_KEY = "AIzaSyAry5zcUcVfYCOsx-Q2qLVTuteLKDMlmd4"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def yt_search(results,query):
    youtube = build(YOUTUBE_API_SERVICE_NAME, 
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
    q=query,
    part="id,snippet",
    maxResults=results
    ).execute()
    
    videos = []
    
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s " % (search_result["snippet"]["title"]))
    return videos
    
def yt_search(results,query,rc):
    youtube = build(YOUTUBE_API_SERVICE_NAME, 
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
    q=query,
    part="id,snippet",
    maxResults=results,
    regionCode=rc
    ).execute()
    
    videos = []
    
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s " % (search_result["snippet"]["title"]))
    return videos
    

    

            