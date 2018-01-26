import pandas as pd
import boto3
import uuid

print('Loading function')

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

def main(event, context):
        # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    try:
        s3_client.download_file(bucket, key, '/tmp/movie.json')
        frame = pd.DataFrame()
        tmp_frame = pd.read_json(path_or_buf="/tmp/movie.json")
        frame = frame.append(tmp_frame, ignore_index=True)
        frame.to_csv('/tmp/temp.csv', index=False)

        unique_filename = str(uuid.uuid4())
        session = boto3.session.Session()
        s3 = session.resource('s3')
        bucket.upload_file('/tmp/temp.csv', 'procesados/' + unique_filename + '.csv')

     except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

if __name__ == "__main__":
    main('', '')
