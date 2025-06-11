def handler(event, context):
    print("Event received:", event)
    # Your code here
    return {
        'statusCode': 200,
        'body': 'Hello, World!'
    }