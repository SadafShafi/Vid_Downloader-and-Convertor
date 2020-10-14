import moviepy.editor as mp 
print("starting")  
# Insert Local Video File Path  
pather = "TASH SULTANA - JUNGLE (LIVE BEDROOM RECORDING)-Vn8phH0k5HI.mp4"
clip = mp.VideoFileClip(pather) 
  
# Insert Local Audio File Path 
clip.audio.write_audiofile(r"thas File.mp3") 