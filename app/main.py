import os
import requests
import boto3
from flask import Flask, render_template

app = Flask(__name__)

# AWS and API Configuration
S3_BUCKET = os.environ.get('BUCKET_NAME', 'your-unievent-s3-bucket')
API_KEY = "YOUR_TICKETMASTER_API_KEY" # Replace with your actual key
s3_client = boto3.client('s3')

def fetch_and_store_events():
    """Fetches events from API and uploads images to S3."""
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={API_KEY}&size=5"
    response = requests.get(url)
    data = response.json()
    
    events_list = []
    if '_embedded' in data:
        for item in data['_embedded']['events']:
            event_id = item['id']
            image_url = item['images'][0]['url']
            
            # Fetch image and upload to S3 [cite: 21]
            img_response = requests.get(image_url)
            s3_client.put_object(
                Bucket=S3_BUCKET, 
                Key=f"posters/{event_id}.jpg", 
                Body=img_response.content,
                ContentType='image/jpeg'
            )
            
            events_list.append({
                'name': item['name'],
                'date': item['dates']['start'].get('localDate', 'TBA'),
                'venue': item['_embedded']['venues'][0]['name'],
                'description': item.get('info', 'No description available.'),
                'image_url': f"https://{S3_BUCKET}.s3.amazonaws.com/posters/{event_id}.jpg"
            })
    return events_list

@app.route('/')
def home():
    events = fetch_and_store_events()
    return render_template('index.html', events=events)

if __name__ == '__main__':
    # Run on port 80 for the Load Balancer to target [cite: 15]
    app.run(host='0.0.0.0', port=80)