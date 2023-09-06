# clip_generation.py
# Possible use for creating clips from a raw video,
# may not be used in final product depending on clip
# generation method.

from moviepy.editor import VideoFileClip
import os
import logging


class ClipGenerator:
    """Handles generation of clips from video source provided."""

    def __init__(self, video_path):
        self.video_path = video_path
        self.video= VideoFileClip(video_path)
    
    def extract_clip(self, start_time, end_time, output_path=None):
        """
        Extract a clip from the video between start_time and end_time.
        
        Args:
        - start_time (float): Start time in seconds.
        - end_time (float): End time in seconds.
        - output_path (str, optional): Path to save the extracted clip. Defaults to None.
        
        Returns:
        - str: Path to the extracted clip.
        """
        logging.info('Extracting clip from {self.video_path}...')
        try:
            clip = self.video.subclip(start_time, end_time)

            # Define output path if not provided.
            if not output_path:
                file_name = os.path.basename(self.video_path)
                base, ext = os.path.splitext(file_name)
                output_path = f"{base}_clip_{start_time}_{end_time}{ext}"
        except Exception as e:
            logging.error(f"Error occurred extracting clip from {self.video_path}: {str(e)}")
        
        logging.info('Clip extraction successful.')
        clip.write_videofile(output_path)

        return output_path

    def close(self):
        """Close the video file to free resources."""
        self.video.close()


# Example Usage

"""
generator = ClipGenerator("path_to_video.mp4")

# Extract a clip from 10s to 20s of the video
clip_path = generator.extract_clip(10, 20)

print(f"Clip saved at: {clip_path}")

generator.close()
"""