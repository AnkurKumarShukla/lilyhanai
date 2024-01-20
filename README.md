# Flask Textract API

This is a simple Flask application that provides an API endpoint for processing images using Amazon Textract. The API receives an image file through a POST request, extracts text using Amazon Textract, and returns the extracted text along with the processing time.

## Prerequisites

Before running the application, make sure you have the following:

1. AWS account with Textract service enabled.
2. AWS Access Key ID and Secret Access Key with appropriate permissions set in your environment variables.
3. Python installed on your system.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/flask-textract-api.git
   ```

2. Navigate to the project directory:

```bash
cd flask-textract-api
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a .env file in the project root directory and add the following environment variables:

```bash
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
```
Replace your_access_key_id and your_secret_access_key with your AWS Access Key ID and Secret Access Key.

## Usage

Run the Flask application:

```bash
python app.py
```
The application will be accessible at [http://localhost:5000](http://localhost:5000) by default.

## API Endpoint

- **Endpoint:** `/`
- **Method:** `POST`
- **Request Body:**
  - Form parameter: `image` (image file)

#### Example using `curl`

```bash
curl -X POST -F "image=@path/to/your/image.jpg" http://localhost:5000/
```

## Response
```json
{
  "processing_time": 1.472205400466919,
  "text": " Human Resources Développement des Development Canada ressources humaines Canada SOCIAL NUMÉRO INSURANCE D'ASSURANCE NUMBER SOCIALE 000 000 000 NAME HERE"
}
```

## Deployment
This application is configured to run on a local development server (host='0.0.0.0'). For production deployment, consider using a production-ready server like Gunicorn or deploying it on a platform like AWS Elastic Beanstalk.


## Contributing
Feel free to contribute to this project by creating issues or submitting pull requests.
