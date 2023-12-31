# clip_processing.py

from moviepy.editor import VideoFileClip, CompositeVideoClip
from utils.error_handlers import FileFormatError, UploadError
import logging



class ClipProcessor:
    """Handles post-processing tasks on generated clips."""

    def __init__(self, clip_path):
        self.clip_path = clip_path
        self.clip = VideoFileClip(clip_path)

        def add_watermark(self, watermark_path, position=("right", "bottom")):
            """Add watermark to the clip."""
            watermark = VideoFileClip(watermark_path, has_mask=True)
            w, h = self.clip.size
            watermark = watermark.resize(height=h//10).set_pos(position)
            return CompositeVideoClip([self.clip, watermark])

        def convert_format(self, target_format):
            """
            Convert the clip to the specified format.
            
            Args:
            - target_format (str): The target format (e.g., "mp4", "avi").
            
            Returns:
            - str: Path to the converted clip.
            """
            try:
                logging.info(f"Clip processing begins...")
                output_path = self.clip_path.rsplit('.',1)[0] + f".{target_format}"
                self.clip.write_videofile(output_path, codec=target_format)
            except FileFormatError as e:
                logging.error(f"Error processing clip: {str(e)}")
                print(f"Error occurred: {e}")

            logging.info(f"Clip processing successful.")
            return output_path
        
        def resize(self, resolution):
            """
            Resize the clip to the given resolution.
            
            Args:
            - resolution (tuple): Resolution as (width, height).
            
            Returns:
            - str: Path to the resized clip.
            """
            resized_clip = self.clip.resize(newsize=resolution)
            output_path = self.clip_path.rsplit('.',1)[0] + f"_resized.{self.clip_path.split('.')[-1]}"
            resized_clip.write_videofile(output_path)

            return output_path
        
        def mock_upload(self, platform="mock_platform"):
            """
            Mock function  to simulate uploading clip to platform.
            
            Args:
            - platform (str): The name of the platform to upload.
            
            Returns:
            - str: Mock response after "uploading".
            """
            try:
                logging.info('Uploading clip to {platform}...')
            except UploadError as e:
                logging.error(f"Error uploading to {platform}: {str(e)}")
                print(f"Error occurred: {e}")
            
            logging.info('Upload to {platform} successful.')
            return f"Clip {self.clip_path} successfully uploaded to {platform}."
        
        def close(self):
            """Close clip to free resources."""
            self.clip.close()


# Usage examples
"""
processor = ClipProcessor("path_to_clip.mp4")

# Convert format to AVI
converted_clip_path = processor.convert_format("avi")
print(f"Converted clip saved at: {converted_clip_path}")

# watermarked_clip = processor.add_watermark("path_to_logo.png")
watermarked_clip.write_videofile("path_with_watermark.mp4")

# Resize to 480x320 resolution
resized_clip_path = processor.resize((480, 320))
print(f"Resized clip saved at: {resized_clip_path}")

# Mock upload
upload_response = processor.mock_upload("Twitter")
print(upload_response)

processor.close()

"""