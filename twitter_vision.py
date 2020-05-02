import tweepy
import time
import io
import os
from flask import Flask
import pytest
from google.cloud import vision
from google.cloud.vision import types

import io
import os
from google.cloud import vision
from google.cloud.vision import types
import urllib
import urllib.request

def set_credentials(ck, cs, ak, a_s):
    Consumer_key= ck
    Consumer_secret= cs
    Access_key= ak
    Access_secret= a_s

    auth=tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_key, Access_secret)
    global api
    api = tweepy.API(auth)
    
    credential_path = r"twittervision-eb2dfdbe7250.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    
    return 1

def tweet_image_desc(image_name):
    client = vision.ImageAnnotatorClient()
    file_name = os.path.join(os.path.dirname(__file__), image_name)

    with io.open(file_name, 'rb') as image_file:
       content = image_file.read()
       
    image = types.Image(content=content)
    response = client.label_detection(image=image)
    
    labels = response.label_annotations

    str=""
    
    for label in labels:
        print (label.description)
        str+=" " +  label.description
    
    try:
        api.update_status(str)
    except:
        print("The description will probably not be tweeted beacuse you are tweeting a duplicate text, try a different image")
    
    return str
    
def example_test():
    set_credentials('OWAfdRNKgpKB1ELKW8M43PAss', '9aClvN6lGZ2oLbqj17gDi9a79MGE1wZ2oPtBxgxqRqwoHsbaFu', '1222946005336936449-8QGSmsVpVHXTf3YSjz0vdlAZbIxpjG', 'nFIaObT4KyUCxh2I3YyYVtefhTKSIug8zn1eWvRWAOLgK')
    tweet_image_desc('car.jpg')
