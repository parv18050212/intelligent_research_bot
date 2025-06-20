import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def get_bedrock_client():
    return boto3.client(
        service_name="bedrock-runtime",
        region_name=os.getenv("AWS_REGION")
    )

def get_embedding(text):
    client = get_bedrock_client()

    body = {
        "inputText": text
    }

    response = client.invoke_model(
        modelId="amazon.titan-embed-text-v1",  # Or any available embedding model
        body=str(body),
        contentType="application/json"
    )

    result = response['body'].read()
    embedding = eval(result)['embedding']  # Or json.loads if needed

    return embedding
