from pathlib import Path
#from flask import Flask
import pytest
#app = Flask(__name__)
#
def test_random_test():
    assert 1==1
     
def test_does_requirements_exist():
    assert Path('requirements.txt').is_file()

def test_does_file_exist():
    assert Path('twittervision-eb2dfdbe7250.json').is_file()
    
def test_does_program_exist():
    assert Path('twitter_vision.py').is_file()
