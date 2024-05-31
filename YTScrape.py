from googleapiclient.discovery import build
build('youtube', 'v3', developerKey='AIzaSyDKwn6jn771LPJ1TGwRXPJqeiiMnM1IW88', cache_discovery=False)

API_KEY = 'AIzaSyDKwn6jn771LPJ1TGwRXPJqeiiMnM1IW88'

VIDEO_ID = 'dQw4w9WgXcQ'

youtube = build('youtube', 'v3', developerKey=API_KEY)

# Retrieve all comments for the video
comments = []
next_page_token = None

while True:
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=VIDEO_ID,
        textFormat='plainText',
        maxResults=100,  # Maximum number of comments to retrieve per request
        pageToken=next_page_token
    ).execute()

    # Add each comment to the comments list
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    # Check if there are more comments to retrieve
    next_page_token = response.get('nextPageToken')
    if not next_page_token:
        break

# Write the comments to a file
with open('comments.txt', 'w', encoding='utf-8') as file:
    for comment in comments:
        file.write(comment + '\n')