def handler(event, context):
    print("Event received:", event)
    response_body ={
        'message': 'Hello, World!',
        'version': '1.0.0',
    }
    # Your code here
    return {
        'statusCode': 200,
        'body': response_body
    }