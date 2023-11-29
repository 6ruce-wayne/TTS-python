import pyttsx3
import argparse
engine = pyttsx3.init()
parser = argparse.ArgumentParser()
parser.add_argument("file", help="text file",type=str) 
args = parser.parse_args()
f = open(args.file, encoding="utf8")
data = f.read()


TH_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI"
text = "ทดสอบ 1 2 3 4"
engine.setProperty('volume', 0.9)  # Volume 0-1
engine.setProperty('rate', 120)  #148

engine.setProperty('voice', TH_voice_id)
engine.say(data)

engine.runAndWait()
print (args)
f.close()