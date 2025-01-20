import ffmpeg

def create_video(audio_file, image_files, output_file):
    """
    Combine audio with images to create a video file.
    """
    # Use FFmpeg to create a video from audio and images
    input_audio = ffmpeg.input(audio_file)
    input_images = ffmpeg.input(image_files, pattern_type='glob', framerate=1)
    ffmpeg.concat(input_images, input_audio, v=1, a=1).output(output_file).run()
