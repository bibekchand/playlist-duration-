import requests
import json
import pprint
import string

class youtube:
    def __init__(self, key, playlistid) -> string:
        self.key = key
        self.playlistid = playlistid
        self.durationlist = []
        

    #returns a list of videos
    def getvideos(self):
        url = "https://www.googleapis.com/youtube/v3/playlistItems"
        params = {'part': 'contentDetails', 'playlistId': self.playlistid,
                  'maxResults': 50,
                  'key': self.key}
        req = requests.get(url, params=params)
        
        #this part gets all the videos from the playlist
        vid_id = []  # this has all the video ids
        content = req.json()
        for item in content['items']:
            vid_id.append(item['contentDetails']['videoId'])
            
        #this gets all the duration from all the videos and puts in the duration list 
        url2 = "https://www.googleapis.com/youtube/v3/videos"
        params2 = {'part': 'contentDetails',
               'id': vid_id, 'key': self.key, 'maxResults': 50}
        
        r2 = requests.get(url2, params=params2)
        content2 = r2.json()
        for item in content2['items']:
            self.durationlist.append(item['contentDetails']['duration'])
        return self.durationlist
            
            
            
    ##this function calculates and returns the total time
    def totalduration(self):
        minval = 0
        secval = 0
        for tyem in self.durationlist:
            for index in range(0, len(tyem)):
                if (tyem[index] != 'P' and tyem[index] != 'T' and tyem[index] != 'S'):
                    newin = tyem[index]
                    if tyem[index] != 'M':
                        minval += int(tyem[index])
                        continue
                    
                    else:
                        try:
                            newraise = ord(tyem[index+2])
                            if (ord(tyem[index+2]) >= 47 and ord(tyem[index+2]) <= 57):
                                secval += int(tyem[index+1]) * 10 + int(tyem[index+2])
                                break
                            else:
                                secval += int(tyem[index+1])
                                break
                        except IndexError:
                            break
                else:
                    continue

        return (minval*60+secval)
