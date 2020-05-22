#backend for langtcha
import speech_recognition as speech
from translate import Translator
from googletrans import Translator
import json
import requests
import urllib3
from random import randrange
import os
from random_word import RandomWords
import list
import shutil

print(len(list.dictionary))

def listen():
    rec = speech.Recognizer()
    with speech.Microphone() as source:
        audio = rec.listen(source)
        said = ""
        try:
            said = rec.recognize_google(audio, language="ja-JP")
            print (said)
            if said == None:
                print("Error")
        except Exception as e:
            print(str(e))
    
    return said

def google(text):
    translator = Translator()
    print(translator.detect(text))
    print(translator.translate(text, dest='en').text)
    return (translator.translate(text, dest='en').text)

def retrieve(translated,file):
    response = requests.get("https://pixabay.com/api/?key=16672497-36598ac6453f29550c10428fe&q="+translated+"&image_type=photo&pretty=false")
    print(response)
    jData = json.loads(response.content)
    url = (jData["hits"][randrange(2)]["webformatURL"])
    print(url)
    resp = requests.get(url, stream=True)
    local_file = open(str(file)+'.jpg', 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    del resp

def random_word():
    query1 = list.dictionary[randrange(25487)]
    print(query1)
    try:
        retrieve(query1,"Incorrect_2")
    except:
        pass
    query2 = list.dictionary[randrange(25487)]
    print(query2)
    try:
        retrieve(query2,"Incorrect_3")
    except:
        pass



text=listen()
translated=google(text)
retrieve(translated,"Correct_1")
random_word()
