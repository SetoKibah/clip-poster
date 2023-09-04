# metadata_collection.py

from moviepy.editor import VideoFileClip

class MetadataCollector:
    """Handles collection of metadat from video clip."""

    def __init__(self, clip_path):
        self.clip_path = clip_path
        self.clip = VideoFileClip(clip_path)

    def basic_metadata(self):
        """
        Extract basic metadata from clip.
        
        Returns:
        - dict: A dictionary containing basic metadata.
        """
        return {
            'duration': self.clip.duration,
            'fps': self.clip.fps,
            'resolution': self.clip.size,
            'audio_channels': self.clip.audio.channels if self.clip.audio else None,
            'audio_fps': self.clip.audio.fps if self.clip.audio else None,
            'codec': self.clip.codec
        }
    
    def custom_metadata(self, *args, **kwargs):
        """
        Placeholder for custom metadata.
        
        Returns:
        - dict: A dictionary containing custom metadata."""
        return {}
    
    def collect_all_metadata(self):
        """
        Combine basic and custom metadata collection.
        
        Returns:
        - dict: A dictionary containing all metadata.
        """
        metadata = {}
        metadata.update(self.basic_metadata())
        metadata.update(self.custom_metadata())

        return metadata
    
    def close(self):
        """Close the clip to free resources."""
        self.clip.close()

# Usage examples
"""
collector = MetadataCollector("path_to_clip.mp4)
# Collect all metadata.
metadata = collector.collect_all_metadata()

collector.close()
"""