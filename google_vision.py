import io
import os
from google.cloud import vision
from google.cloud.vision import types
import urllib
import urllib.request

urllib.request.urlretrieve('https://f1.media.brightcove.com/8/1078702682/1078702682_6004950245001_6004956161001-vs.jpg?pubId=1078702682&videoId=6004956161001', 'car2.jpg')

client = vision.ImageAnnotatorClient()

file_name = os.path.join(os.path.dirname(__file__), 'car2.jpg')

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    
image = types.Image(content=content)

response = client.label_detection(image=image)

labels = response.label_annotations

print("Labels:")

for label in labels:
    print (label.description)
