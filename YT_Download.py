from pytube import YouTube                                    # Here I have imported youtube from pytube Package of python
url = "https://www.youtube.com/watch?v=M0xWXQ0R3SQ&t=12s"     # Here i have stored the URL of those video, which I want to download
video = YouTube(url)                                          # Here i have created one more variable 'video' and then i was called Youtube Method of Pythube package and passed url in it


try:                                                          # Here we are not sure, our youtubes video download code will runs properly or Not | That's why, we used try-catch block
    print("")
    print("")
    print("Title : "+video.title)                             # This print statement displays the name or title of our video, for that we used (.title())
    print("")
    print("")
    
    downloader = video.streams.get_highest_resolution()       # Now we created one more variable 'downloader' to store our video's highest resulation, for that we used, .get_highest_resolution() method
    print("Getting Highest Resulation of Video !")            
    print("")
    print("")
    
    downloader.download()                                     # At the last we used .download() method to download our video.
    print("Video is downloaded successfully")
    print("")
    print("")
    
except:                                                       # Here we ued except block to catch the error, when something wents wrong
    print("Video is not downloaded")                          
