import os
def handler(event, context):
    print("Event received:", event)
    version = os.environ.get('VERSION', '0.0')
    response_body ={
        'message': 'Hello, World!',
        'version': version,
    }
    # Your code here
    return {
        'statusCode': 200,
        'body': response_body
    }