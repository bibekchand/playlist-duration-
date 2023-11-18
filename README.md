## Introduction
This python script is based on the [Youtube data api](https://developers.google.com/youtube/v3/docs). 
This script in particular returns you with the duration of a playlist.
For accessing the duration of the playlist you require two things.
1. Your own [personal api key](https://console.developers.google.com/)
2. The playlist id which will be available in the url.
## How to use
You can use the script as follows:
1. First you have to import this script in your code:
	`from playlist import youtube`
2. Create an object instance for it and pass in the key and the playlist id in double quote  as such:
	`first = youtube("your-key", "playlist id")
3. Call the method totalduration as such:
	`duration = first.totalduration()`
4. You can also get the video ids of all the videos by calling the method getVideos:
	`videos = first.getVideos()

> [!NOTE]
> This is just a passion project. Google already has a very well coded and documented python client for all of its services [google api client](https://github.com/googleapis/google-api-python-client)
