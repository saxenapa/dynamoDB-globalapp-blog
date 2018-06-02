import boto3
import json
import decimal
import os
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

REGION_NAME = os.environ['REGION']  
TABLE_NAME = os.environ['TABLE']
KeyColumn = os.environ['KeyCol']
        
dynamodb = boto3.resource("dynamodb", region_name=REGION_NAME)
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):

    myKey = event['key']

    try:
        response = table.get_item(
            Key={
                KeyColumn : myKey
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        item = {0:0}
    else:
        item = response['Item']

        return item, REGION_NAME
