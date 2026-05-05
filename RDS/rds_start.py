import boto3

rds = boto3.client('rds')

def lambda_handler(event, context):
    db_instances = ['your-database-id']

    for db in db_instances:
        try:
            rds.start_db_instance(DBInstanceIdentifier=db)
            print(f"Starting {db}")
        except Exception as e:
            print(f"Error starting {db}: {e}")