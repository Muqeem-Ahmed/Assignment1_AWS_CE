from flask import Flask, render_template
import requests
import boto3
import os

app = Flask(__name__)

# AWS Configuration - Ensure your IAM Role has S3FullAccess
BUCKET_NAME = 'unievent-media-storage-giki'
s3 = boto3.client('s3')

@app.route('/')
def index():
    # 1. Fetch from Ticketmaster API
    # Replace 'YOUR_TICKETMASTER_API_KEY' with your actual key
    API_KEY = "YOUR_TICKETMASTER_API_KEY"
    API_URL = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={API_KEY}&city=Sydney&size=6"
    
    events = []
    try:
        response = requests.get(API_URL)
        events = response.json().get('_embedded', {}).get('events', [])
        
        # 2. S3 Logic: "The Technical Depth Feature"
        # This takes the poster of the first event and saves it to your bucket
        if events:
            img_url = events[0]['images'][0]['url']
            img_data = requests.get(img_url).content
            s3.put_object(
                Bucket=BUCKET_NAME, 
                Key='featured_event.jpg', 
                Body=img_data,
                ContentType='image/jpeg'
            )
    except Exception as e:
        print(f"Error handling API or S3: {e}")

    return render_template('index.html', events=events)

if __name__ == "__main__":
    # Port 80 is required for the ALB to route traffic without extra config
    app.run(host='0.0.0.0', port=80)
