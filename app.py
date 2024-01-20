from flask import Flask, request, jsonify
import boto3
import time

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_image():
    try:
        # get the start time
        st = time.time()

        # Replace these with your actual AWS credentials and region
        # aws_access_key_id = 'YOUR_ACCESS_KEY'
        # aws_secret_access_key = 'YOUR_SECRET_KEY'
        # region_name = 'YOUR_REGION'

        client = boto3.client('textract', region_name='us-west-1', aws_access_key_id='AKIA4MTWLMMZLLJ22FQI',
                              aws_secret_access_key='V6iYnd0hugkYAdLMRXVpzlax2ZPgKM0oqiwOTQLH')

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
    app.run(debug=True)
