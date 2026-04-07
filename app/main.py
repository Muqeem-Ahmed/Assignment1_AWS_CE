from flask import Flask, render_template
import requests
import boto3

app = Flask(__name__)
s3 = boto3.client('s3')
BUCKET_NAME = 'unievent-media-storage-giki'

@app.route('/')
def index():
    # 1. Fetch from Ticketmaster API
    api_url = "https://app.ticketmaster.com/discovery/v2/events.json?apikey=YOUR_API_KEY&city=Sydney"
    response = requests.get(api_url).json()
    events = response.get('_embedded', {}).get('events', [])

    # 2. Logic to upload first image to S3 (Simplified for brevity)
    # In a real app, you'd check if it exists first
    if events:
        image_url = events[0]['images'][0]['url']
        img_data = requests.get(image_url).content
        s3.put_object(Bucket=BUCKET_NAME, Key='latest_event.jpg', Body=img_data)

    return render_template('index.html', events=events)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
