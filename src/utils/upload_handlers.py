# utils/upload_handlers.py

import requests
import logging

def setup_logging():
    logging.basicConfig(filename="app.log",
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
 

class UploadHandlers:

    # Boilerplate
    def __init__(self):
        pass
    
    def _upload_to_twitter(self, clip_path):
        """
        Handle uploading processed clip to Twitter.
        """
        twitter_api_endpoint = "https://api.twitter.com/.../..." # needs to be replace with appropriate endpoint

        headers = {
            # Blank until known headers for authentication are done.
            # Need to read docs.
        }

        # Typical way to send a post request and get response check, keeping simple.
        with open(clip_path, 'rb') as video_file:
            response = requests.post(twitter_api_endpoint, headers=headers)
        
        # Handle responses and check for errors.
        if response.status_code == 200:
            logging.info(f'Video upload to Twitter successful for {clip_path}')
        else:
            logging.error(f"Failed to upload to Twitter. Status code: {response.status_code}"
                  "\n Message: {response.text}")
    

    def _upload_to_tiktok(self, clip_path):
        """
        Handle uploading processed clip to TikTok.
        """
        tiktok_api_endpoint = "https://api.tiktok.com/.../..." # needs to be replace with appropriate endpoint

        headers = {
            # Blank until known headers for authentication are done.
            # Need to read docs.
        }

        # Typical way to send a post request and get response check, keeping simple.
        with open(clip_path, 'rb') as video_file:
            response = requests.post(tiktok_api_endpoint, headers=headers)
        
        # Handle responses and check for errors.
        if response.status_code == 200:
            logging.info(f'Video upload to TikTok successful for {clip_path}')
        else:
            logging.error(f"Failed to upload to TikTok. Status code: {response.status_code}"
                  "\n Message: {response.text}")
    

    def upload(self, clip_path):
        """
        Public method to upload clips to both platforms.
        """
        self._upload_to_twitter(clip_path)
        self._upload_to_tiktok(clip_path)