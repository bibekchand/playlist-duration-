## Introduction
This python script is based on the [Youtube data api](https://developers.google.com/youtube/v3/docs). 
This script in particular returns you with the duration of a playlist.
For accessing the duration of the playlist you require two things.
1. Your own [personal api key](https://console.developers.google.com/)
2. The playlist id which will be available in the url.
## How to use
You can use the script as follows:
1. First install the package using:
        <br> `pip install -i https://test.pypi.org/simple/ playlistwrapper==0.0.4` </br>
2. Now, you have to import the package  in your code:
        <br>`from playlistwrapper.playlist import youtube`</br>
3. Create an object instance for it and pass in the key and the playlist id in double quote  as such:
	<br>`first = youtube("your-key", "playlist id")`</br>
4. Call the method totalduration as such:
	<br>`duration = first.totalduration()`</br>
5. You can also get the video ids of all the videos by calling the method getVideos:
	<br>`videos = first.getVideos()`</br>

> [!NOTE]
> This is just a passion project. Google already has a very well coded and documented python client for all of its services [google api client](https://github.com/googleapis/google-api-python-client)
