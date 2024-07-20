from gtts import gTTS #pip install gtts and include it here
import os #import os operating sysytem

text = open('voice.txt','r').read() #open the voice.txt in readmode

language ='en' #Language english

output = gTTS(text=text,lang='en',slow=False) #gtts convert text to speech
output.save('output.mp3') #speech is saved in output.mp3

os.system("start output.mp3") #starts sysytem's default media player to play output.mp3
