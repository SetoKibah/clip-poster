# imports
from utils import CustomError, some_helper_function, VideoProcessor


# Run program
def main():
    
    # Using utils example
    processor = VideoProcessor("path_to_video")
    processor.resize("1080p")

if __name__ == "__main__":
    main()