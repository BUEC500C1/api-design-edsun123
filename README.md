# api-design-edsun123
api-design-edsun123 created by GitHub Classroom


## Description
This api will print out the image description of a image file as input as argument and tweet it given the appropriate keys

## File Organization

* Car.jpg and img.jpg are example images used for the example program

* twittervision-eb2dfdbe7250.json is used for setting the crednetials

* misc contains all miscellaneous files not needed for operation

* requirements.txt contains the packages needed to install

* test_twitter_vision.py tests the functions for github actions

* twitter_vision.py  contains the main functions you want to run

## Usage / how to use the functions
I've created three functions inside : set_credentials(), tweet_image_desc(), example_test()

You must set credentials in order to use the twitter and google vision api. This needs your consumer key, consumer_secret, access keys and access_secret as inputs. 

To get the text description of the images, put the image jpg name inside the current directory as the main file twitter_vision.py. This is will grab the image and pass it into the google vision api. Given the credentials of the twitter handle you want to use, it will post the tweet of image description. It will run into an error if you try to tweet the same image description. This is twitter api's way of preventing spamming. Moreoever, it will print out the string of the imae desciption.

For testing purposes, you can  run example_test() that will pass in the credentials for my tweet handle and pass car.jpg that I have already saved in the current directory. 

