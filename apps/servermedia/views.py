import boto3
from django.http import HttpRequest, HttpResponse
import mimetypes
import os

# Create your views here.

def media(request: HttpRequest, file_path):
    file_path = os.path.join('media', file_path)

    if os.getenv('USE_S3') == 'true':
        s3 = boto3.client(
            's3',
            aws_access_key_id = os.getenv('ACCESS_KEY_ID'),
            aws_secret_access_key = os.getenv('SECRET_ACCESS_KEY'),
            endpoint_url = 'https://s3.us-east-005.backblazeb2.com'
        )

        try:
            response = s3.get_object(Bucket = os.getenv('STORAGE_BUCKET_NAME'), Key = file_path)

            file_data = response['Body'].read()

            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type is None:
                mime_type = 'application/octet-stream'

            return HttpResponse(file_data, content_type = mime_type)
        except s3.exceptions.NoSuchKey:
            return HttpResponse('File Not Found', status = 404)

    if os.path.exists('./'+file_path):
        with open('./'+file_path, 'rb') as file:
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type is None:
                mime_type = 'application/octet-stream'

            return HttpResponse(file.read(), content_type = mime_type)
    
    return HttpResponse('File Not Found', status = 404)
