#utils/video_utils.py

from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.io.ffmpeg_tools import ffmpeg_tools
from moviepy.video.fx import all as vfx

class VideoProcessor():
    """Utility class for handling video processing."""

    def __init__(self, video_path):
        self.video_path = video_path
        self.clip = VideoFileClip(self.video_path)
        self.width = self.clip.size[0]
        self.height = self.clip.size[1]
        self.duration = self.clip.duration

    def resize(self, resolution="720p"):
        """Resize video to the given resolution"""
        resolutions = {
            "480p": (640, 480),
            "720p": (1280, 720),
            "1080p": (1920, 1080)
        }
        
        target_resolution = resolutions.get(resolution, (1280, 720))
        resized_clip = self.clip.resize(height=target_resolution[1])
        output_path = self.video_path.rsplit('.', 1)[0] + f"_resized_{resolution}.mp4"
        resized_clip.write_videofile(output_path)
        return output_path

    def convert_format(self, target_format = "mp4"):
        """Convert video to specified format"""
        output_path = self.video_path.rsplit('.', 1)[0] + f".{target_format}"
        self.clip.write_videofile(output_path, codec=target_format)
        return output_path
        
    def add_watermark(self, watermark_path, position=("bottom", "right"), margin=10):
        """Overlay a watermark/logo on the video."""
        watermark = VideoFileClip(watermark_path, has_mask=True)

        if position[0] == "top":
            vertical_pos = margin
        else: # Default to bottom
            vertical_pos = self.height - watermark.size[1] - margin
        
        if position[1] == "left":
            horizontal_pos = margin
        else: # Default to right
            horizontal_pos = self.width - watermark.size[0] - margin
        
        watermarked_clip = self.clip.fx(vfx.watermark, watermark, pos=(horizontal_pos, vertical_pos))
        output_path = self.video_path.rsplit('.', 1)[0] + "_watermarked.mp4"
        watermarked_clip.write_videofile(output_path)
        return output_path
    
    def close(self):
        self.clip.close()