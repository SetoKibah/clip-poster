# main.py

# imports
from clip_generation import ClipGenerator
from clip_processing import ClipProcessor
from metadata_collection import MetadataCollector
import logging

def setup_logging():
    logging.basicConfig(filename="app.log",
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    

# Run program
def main():

    # Generate a clip
    try:
        logging.info('Generating clip...')
        generator = ClipGenerator("path_to_video.mp4")
        clip_path = generator.extract_clip(10,20) # Extract clip from 10s to 20s.
        generator.close()
        logging.info('Clip extraction complete.')
    except Exception as e:
        logging.error("Error occurred extracting clip from video.")
    

    # Process the clip
    try:
        logging.info('Processing clip...')
        processor = ClipProcessor(clip_path)
        resized_clip_path =processor.resize((480, 320))
        converted_clip_path = processor.convert_format("avi")
        # Mock upload to demonstrate flow
        upload_response = processor.mock_upload("Twitter")
        processor.close()
        logging.info('Clip processing complete.')
    except Exception as e:
        logging.error(f"Error occurred processing clip: {str(e)}")

    # Collect metadata
    try:
        logging.info("Collecting metadata")
        collector = MetadataCollector(converted_clip_path)
        metadata = collector.collect_all_metadata()
        collector.close()
        logging.info("Metadata collection complete.")
    except Exception as e:
        logging.error(f"Error occurred collecting Metadata: {str(e)}")

if __name__ == "__main__":
    main()