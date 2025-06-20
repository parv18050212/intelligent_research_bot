import os
import json
import boto3
from dotenv import load_dotenv

load_dotenv()

bedrock = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION", "ap-south-1"))

def json_bytes(data):
    return bytes(json.dumps(data), "utf-8")

def ask_bedrock(prompt):
    model_id = os.getenv("BEDROCK_MODEL", "amazon.titan-text-express-v1")

    if "titan" in model_id:
        # ✅ Format for Amazon Titan
        body = {
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 300,
                "temperature": 0.7,
                "topP": 0.9,
                "stopSequences": []
            }
        }
    else:
        # ✅ Fallback for Claude-like models (optional)
        body = {
            "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
            "max_tokens_to_sample": 300,
            "temperature": 0.7,
            "stop_sequences": ["\n\nHuman:"]
        }

    response = bedrock.invoke_model(
        modelId=model_id,
        body=json_bytes(body),
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(response["body"].read())

    # ✅ Titan has 'results'; Claude has 'completion'
    if "results" in result:
        return result["results"][0]["outputText"]
    elif "completion" in result:
        return result["completion"]
    else:
        return "No response from model."
