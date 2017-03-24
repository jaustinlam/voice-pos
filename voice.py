#!/usr/bin/env python3
import speech_recognition as sr 
from os import path

def return_text():
	AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "amy.wav")

	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)

	BING_KEY = "107048a7dda0490bb5f3d2746ca00e19"
	try:
		return(r.recognize_bing(audio, key=BING_KEY))
	except sr.UnknownValueError:
		return("Sorry we could not understand try again")
	except sr.RequestError as e:
 		return("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

#Key 1:107048a7dda0490bb5f3d2746ca00e19 
