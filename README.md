# Hello! thank you for using SDR!

## How to download and import your data

### Getting Your Data

Unfortunally spotifys API dosent actually lets you see the mintues and # of plays of your songs and artists, __SO YOU HAVE TO DOWNLOAD__ your spotify data

__Download Link:https://www.spotify.com/us/account/privacy/__

NOTICE!(when u download your spotify data none of your sensitive information is downloaded, even if it is this code is only looks at the StreamingHistory_music_0.json file so no worries!

Please select the download account data at the bottom, it says 5 days but it took me 3 days to get the email.

It will download a .zip file and you have to extract. You will see __A LOT__ of .json files but you should be looking for the StreamingHistory_music files. For some reason spotify usually splits it into 2 files __usually something like the example below__. (there could be more but when i extracted my data i got 2)

1. StreamingHistory_music_0.json
2. StreamingHistory_music_1.json

__PLEASE TAKE THESE 2 FILES (or how ever many u have) AND COPY THEM INTO A NEW FOLDER__

### Merging the StreamingHistory JSON Files

(if you dont have mutiple files you can skip ahead)

in order for this program to read the code properly your going to have merge the files, its pretty self explantitory but here are the steps

1. Make a new text document in the new folder you created
2. Go into the StreamingHistory_music_0 and copy all of it (Ctrl A/Crtl C)
3. Put the copied StreamingHistory_music_0 into the new text document
4. then at the very bottom type in a marker, it needs to be something you can find easy (dont make it anything included in the spotify json files) (i literlly just put skibidi)

   this should be the end of the code
 ```
  {
    "endTime" : "2024-08-02 22:44",
    "artistName" : "Mac DeMarco",
    "trackName" : "Young Coconut",
    "msPlayed" : 118990
  }
]
skibidi

 ```
6. then go into StreamingHistory_music_1 file and copy all of it (Ctrl A/Crtl C)
7. go into the new text file and make sure your at the very end and paste it (Ctrl V)
8. then use the search feature (Ctrl F) to search for your marker (for me its skibidi) if you made the marker unique it should teleport you to the where you merged the 2
9. now the merged area should look like this

 ```
    {
    "endTime" : "2024-08-02 22:44",
    "artistName" : "Mac DeMarco",
    "trackName" : "Young Coconut",
    "msPlayed" : 118990
  }
]
skibidi
[
  {
    "endTime" : "2024-08-02 22:45",
    "artistName" : "Mac DeMarco",
    "trackName" : "20190723",
    "msPlayed" : 72470
  },

 ```
10. we need to remove that middle part because thats invalid formatting so change it to this

   ```
    {
    "endTime" : "2024-08-02 22:44",
    "artistName" : "Mac DeMarco",
    "trackName" : "Young Coconut",
    "msPlayed" : 118990
  },
  {
    "endTime" : "2024-08-02 22:45",
    "artistName" : "Mac DeMarco",
    "trackName" : "20190723",
    "msPlayed" : 72470
  },

 ```
11. __DONT FORGET THE COMMA__
12. once the files are merged you can save the new txt document

    ### Using the SDR

    your going to need the file path of the new merged .json file so right click on the file and press __copy as path__, then go open up SDR and right click on the terminal to paste in the file path. Press enter and choose if u want your top5 or all! (WARNING: if you choose all then it will show you ALLLL your music history for the past year, if if you listend to a song for 1 second it will still pop up, so thats why i added you top 5)

    (the SDR is sorted by minutes)

