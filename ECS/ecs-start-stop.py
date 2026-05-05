import boto3

def lambda_handler(event, context):
    services = [
        {'cluster': 'your-cluster-name', 'service': 'your-service-name'},
        {'cluster': 'your-cluster-name', 'service': 'your-service-name'},
        {'cluster': 'your-cluster-name', 'service': 'your-service-name'}
    ]
    
    ecs = boto3.client('ecs')
    
    if event['action'] == 'stop':
        # Stop each ECS service
        for service in services:
            response = ecs.update_service(
                cluster=service['cluster'],
                service=service['service'],
                desiredCount=0
            )
        message = 'All ECS services stopped successfully!'
    elif event['action'] == 'start':

        for service in services:
            response = ecs.update_service(
                cluster=service['cluster'],
                service=service['service'],
                desiredCount=1
            )
        message = 'All ECS services started successfully!'
    else:
        message = 'Invalid action specified. Please specify either \'stop\' or \'start\'.'
    
    print(response)
    
    return {
        'statusCode': 200,
        'body': message
    }