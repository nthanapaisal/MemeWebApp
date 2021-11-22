#from app import app

from flask import Flask
from flask import render_template
import configs.config as keys
import logging
import boto3
from botocore.exceptions import ClientError
import random

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb',
                    aws_access_key_id=keys.ACCESS_KEY_ID,
                    aws_secret_access_key=keys.ACCESS_SECRET_KEY,
                    aws_session_token=keys.AWS_SESSION_TOKEN,
                    region_name='us-east-2')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image')
def display_image():
    image_url = "https://cloud-memes.s3.us-east-2.amazonaws.com/blb.jpg"
    
    return render_template('displayImage.html', user_image = image_url)



@app.route('/get-items', methods=['GET'])
def get_items():

    table = dynamodb.Table('memes')
    num = random.randint(0,table.item_count)
    try:
        response = table.get_item(Key={'pkeys': str(num % table.item_count)})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return render_template('displayImage.html', meme_img = response['Item']['Image'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


