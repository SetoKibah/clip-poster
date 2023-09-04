# main.py

# imports
from clip_generation import ClipGenerator
from clip_processing import ClipProcessor
from metadata_collection import MetadataCollector

# Run program
def main():
    # Generate a clip
    generator = ClipGenerator("path_to_video.mp4")
    clip_path = generator.extract_clip(10,20) # Extract clip from 10s to 20s.
    generator.close()

    # Process the clip
    processor = ClipProcessor(clip_path)
    resized_clip_path =processor.resize((480, 320))
    converted_clip_path = processor.convert_format("avi")
    # Mock upload to demonstrate flow
    upload_response = processor.mock_upload("Twitter")
    processor.close()

    # Collect metadata
    collector = MetadataCollector(converted_clip_path)
    metadata = collector.collect_all_metadata()
    collector.close()

if __name__ == "__main__":
    main()