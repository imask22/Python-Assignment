#should be imported to play the sound
#use pip install gTTS
from gtts import gTTS 
#dict1={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}

try:
	n=int(input("Enter your number : "))
except:
	print("only Number Should be entered")

mytext = str(n)

language = 'en'
  
myobj = gTTS(text=mytext, lang=language ,slow=False) 

#this will be saved in a file  
myobj.save("ask.mp3") 
