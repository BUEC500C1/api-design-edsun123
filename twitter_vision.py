import tweepy
import time
import io
import os
from google.cloud import vision
from google.cloud.vision import types

import io
import os
from google.cloud import vision
from google.cloud.vision import types
import urllib
import urllib.request

print("this is twitter bot");
Consumer_key= 'oneBlZdM0AaWQzuutkVxQJZ3g'
Consumer_secret= 'vsTzdyO3jHgiCQglgX1nqo8VaylxFpn0u93XEseBbALRCR9g5F'
Access_key= '1222946005336936449-bS53klLdH43Bi71nSQyVWPhD6cdrSA'
Access_secret= 'Dybso4U2NA3ibzd6nZtcNrCarvpqsYCFgoGEAAh4lxeAS'

auth=tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_key, Access_secret)
api = tweepy.API(auth)

credential_path = r"twittervision-eb2dfdbe7250.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id)
            
    for mention in reversed(mentions):
    
        media=mention.entities.get('media')[0].get('media_url')
        urllib.request.urlretrieve(media, 'img.jpg')
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        client = vision.ImageAnnotatorClient()

        file_name = os.path.join(os.path.dirname(__file__), 'img.jpg')

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
            
        image = types.Image(content=content)

        response = client.label_detection(image=image)

        labels = response.label_annotations

        str=""

        for label in labels:
            print (label.description)
            str+=" " +  label.description
            
        api.update_status(str, mention.id)
#        if '#twitter_vision' in mention.text.lower():
#            print('found #helloworld!', flush=True)
#            print('responding back...', flush=True)
#            print('@' + mention.user.screen_name + '#HelloWorld back to you!')
#            api.update_status('@' + mention.user.screen_name + '#HelloWorld back to you!', mention.id)
#            api.update_status('@' + str + '#HelloWorld back to you!', mention.id)

def print_objects():
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id)
                
    for mention in reversed(mentions):

        media=mention.entities.get('media')[0].get('media_url')
        urllib.request.urlretrieve(media, 'img.jpg')
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        client = vision.ImageAnnotatorClient()

        file_name = os.path.join(os.path.dirname(__file__), 'img.jpg')

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        objects = client.object_localization(
            image=image).localized_object_annotations

        str=""
        print('Number of objects found: {}'.format(len(objects)))
        for object_ in objects:
            print('\n{} (confidence: {})'.format(object_.name, object_.score))
#            str+="s"
#            '\n{} (confidence: {})'.format(object_.name, object_.score);
            print('Normalized bounding polygon vertices: ')
            for vertex in object_.bounding_poly.normalized_vertices:
                print(' - ({}, {})'.format(vertex.x, vertex.y))

#        api.update_status(str, mention.id)
        
def print_colors():
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id)
                
                
    for mention in reversed(mentions):

        media=mention.entities.get('media')[0].get('media_url')
        urllib.request.urlretrieve(media, 'img.jpg')
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        client = vision.ImageAnnotatorClient()

        file_name = os.path.join(os.path.dirname(__file__), 'img.jpg')

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
            
        image = types.Image(content=content)

        response = client.image_properties(image=image)
        props = response.image_properties_annotation

        str=""

        for color in props.dominant_colors.colors:
            print('frac: {}'.format(color.pixel_fraction))
            print('\tr: {}'.format(color.color.red))
            print('\tg: {}'.format(color.color.green))
            print('\tb: {}'.format(color.color.blue))
            print('\ta: {}'.format(color.color.alpha))

#            str+=" " + label.description
            
#        api.update_status(str, mention.id)

#where you runthe program
while(True):
    reply_to_tweets();
    time.sleep(5)
