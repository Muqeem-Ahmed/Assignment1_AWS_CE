import requests
import boto3
from flask import Flask, render_template

app = Flask(__name__)
s3 = boto3.client('s3')
BUCKET_NAME = 'unievent-media-storage'

# 1. Fetching from External API 
def fetch_university_events():
    api_url = "https://app.ticketmaster.com/discovery/v2/events.json?apikey=YOUR_KEY"
    response = requests.get(api_url).json()
    events = response.get('_embedded', {}).get('events', [])
    
    # 2. Process and Store Media in S3 [cite: 20, 21]
    for event in events:
        image_url = event['images'][0]['url']
        img_data = requests.get(image_url).content
        s3.put_object(Bucket=BUCKET_NAME, Key=f"posters/{event['id']}.jpg", Body=img_data)
        
    return events

@app.route('/')
def index():
    # 3. Display fetched events as "University Events" [cite: 22]
    events = fetch_university_events()
    return render_template('index.html', events=events)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)