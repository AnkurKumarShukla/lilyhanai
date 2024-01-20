from flask import Flask, request, jsonify
import boto3
import time
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def process_image():
    try:
        # get the start time
        st = time.time()

        # Read AWS credentials from environment variables
        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

        client = boto3.client('textract', region_name='us-west-1', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key)

        # Assuming the image is sent as a POST request
        img = request.files['image'].read()

        response = client.detect_document_text(Document={'Bytes': img})

        text = ""
        for item in response["Blocks"]:
            if item["BlockType"] == "LINE":
                print(item["Text"])
                text = text + " " + item["Text"]

        # You may want to return the extracted text in the response
        et = time.time()
        processing_time = et - st

        return jsonify({"text": text, "processing_time": processing_time})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
