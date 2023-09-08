# utils/helpers.py

import os
from moviepy.editor import VideoFileClip

def get_file_extension(file_path):
    return os.path.splitext(file_path)[-1].lower()

def generate_output_name(input_path, suffix, extension=None):
    base_name = os.path.basename(input_path).resplit('.', 1)[0]
    if not extension:
        extension = get_file_extension(input_path)
    return f"{base_name}_{suffix}.{extension}"

def validate_video_format(file_path):
    valid_formats = ['.mp4', '.avi', '.mov', '.mkv']
    return get_file_extension(file_path) in valid_formats

def validate_file_exists(file_path):
    return os.path.isfile(file_path)

def get_platform_video_spec(platform):
    # Example form, will narrow down specs
    specs = {
        'twitter': {'max_duration': 60, 'preferred_resolution': (1280, 720)},
        'tiktok': {'max_duration': 60, 'preferred_resolution': (1080, 1920)}
    }

    return specs.get(platform.lower())

def clip_duration(file_path):
    with VideoFileClip(file_path) as clip:
        return clip.duration
    
def get_watermark_position(clip_width, clip_height,
                            watermark_width, watermark_height, margin=10):
    return (clip_width - watermark_width - margin, clip_height - watermark_height - margin)
