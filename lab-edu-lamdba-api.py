import json
import boto3
import random
import json

def lambda_handler(event, context):
    
    member_name = ['Hachi','Koji','Yuki','Miko','Mocha']
    member_status = ['Happy','Sad','Serious','Satisfied','Free']
    
    dynamodb = boto3.resource('dynamodb')
    member_table = dynamodb.Table('lab-edu-dynamodb-name')
    
    name = member_name[random.randint(0,4)]
    status = member_status[random.randint(0, 4)]
    
    member_table.put_item(
       Item={
            'name': name,
            'status': status,
        }
    )
    
    documents = {'name':name,'status':status}
    
    print(documents)
    
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(documents)
    }
