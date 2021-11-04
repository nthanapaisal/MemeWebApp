#from app import app

from flask import Flask
import configs.config as keys
import logging
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb',
                    aws_access_key_id=keys.ACCESS_KEY_ID,
                    aws_secret_access_key=keys.ACCESS_SECRET_KEY,
                    aws_session_token=keys.AWS_SESSION_TOKEN,
                    region_name='us-east-2')

@app.route('/')
def index():
    return '/root page'

@app.route('/get-items')
def get_items():

    table = dynamodb.Table('memes')

    try:
        response = table.get_item(Key={'pkeys': '1'})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']["Image"]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


