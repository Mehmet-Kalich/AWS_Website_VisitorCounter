import json, boto3

client = boto3.client('dynamodb')
TableName = 'cloud-resume'

def lambda_handler(event, context):
    
    data = client.get_item(
        TableName='cloud-resume',
        Key = {
            'stat': {'S': 'view-count'}
        }
    )
    
    prevViewCount = data['Item']['Quantity']['N']
    
    
    return {
            'statusCode': 200,
            'body': data,
            "headers": 
            {
            "Access-Control-Allow-Origin" : "*"
            }
        }