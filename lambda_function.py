import boto3
import csv
import json

s3_client = boto3.client('s3')
sqs_client = boto3.client('sqs')

def lambda_handler(event, context):

    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']
        
        try:
            # extracting CSV file from S3 bucket
            csv_file = s3_client.get_object(Bucket=bucket_name, Key=file_key)
            csv_content = csv_file['Body'].read().decode('utf-8').splitlines()
            
            messages = process_csv_data(csv_content, file_key)
            
            # forwarding messages to SQS
            queue_url = 'https://sqs.eu-north-1.amazonaws.com/975050307828/orderprocessingqueue'
            for message in messages:
                send_message_to_sqs(queue_url, message)
        except Exception as e:
            #exception handling
            error_message = {
                'type': 'error_message',
                'message': "something went wrong!"
            }
            send_message_to_sqs('https://sqs.eu-north-1.amazonaws.com/975050307828/orderprocessingqueue', error_message)

def process_csv_data(csv_content, file_key):
    messages = []
    t_price = 0.0
    unique_order_references = set()
    reader = csv.DictReader(csv_content)

    try:
        for row in reader:
            price = float(row['total_price'])  
            t_price += price
            unique_order_references.add(row['order_reference'])
        
        order_count = len(unique_order_references)
        # creating customer message
        total_price_message = {
            'type': "customer_message",
            'number_of_orders': order_count,
            'total amount spent': t_price
        }
        messages.append(total_price_message)
    except Exception as e:
        # creating error message as 
        messages.append({
            'type': "error_message",
            'message': "something went wrong!"
        })

    return messages

def send_message_to_sqs(queue_url, message):
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message)
    )
    return response
