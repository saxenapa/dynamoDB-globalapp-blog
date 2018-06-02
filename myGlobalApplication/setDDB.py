import boto3
import json
import decimal
import os
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

REGION_NAME = os.environ['REGION']
TABLE_NAME = os.environ['TABLE']
KeyColumn = os.environ['KeyCol']

dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):

    myKey = event['key']
    myValue = event['value']

    try:
        response = table.put_item(
            Item={
                KeyColumn : myKey,
                'Value' : myValue
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response, REGION_NAME
