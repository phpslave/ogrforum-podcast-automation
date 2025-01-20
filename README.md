# OGRForum Podcast Automation

## Overview

This project automates the workflow of extracting data from [ogrforum.com](https://ogrforum.com), processing it into a podcast format, and uploading it to YouTube. The workflow includes:

1. **Data Extraction**: Crawling forum topics, posts, user metadata, post times, and links to source materials (e.g., images) using GPT-Crawler.
2. **Data Storage**: Storing the extracted data in a local vector database (Qdrant) after preprocessing and chunking.
3. **Transcript Generation**: Creating two-person conversational transcripts suitable for a podcast using a local LLM.
4. **Audio Synthesis**: Converting transcripts into audio files using Parler-TTS.
5. **Video Creation**: Combining audio with images to create video files using FFmpeg.
6. **YouTube Upload**: Automating the upload of videos to YouTube as part of the ogrforum.com series using the YouTube Data API.

## Tools and Technologies

- **n8n**: Open-source workflow automation tool to orchestrate the process.
- **GPT-Crawler**: Node.js-based tool for crawling websites to generate knowledge files.
- **Qdrant**: Open-source vector database for storing and managing extracted data.
- **Local LLM (e.g., Llama)**: Locally hosted language model for generating podcast transcripts.
- **Parler-TTS**: Open-source text-to-speech model for audio synthesis.
- **FFmpeg**: Multimedia framework for combining audio with images to create video files.
- **YouTube Data API**: For automating the uploading of videos to the YouTube channel.

## Workflow Steps

1. **Data Extraction with GPT-Crawler**:
   - **Objective**: Crawl ogrforum.com to extract topics, posts, user metadata, post times, and links to source materials.
   - **Implementation**:
     - Configure GPT-Crawler to start at the forum's base URL and define patterns to match relevant pages.
     - Set up selectors to extract the desired data fields.
     - Ensure compliance with the website's `robots.txt` and terms of service.

2. **Data Storage in Qdrant**:
   - **Objective**: Store the extracted data in a vector database for efficient retrieval and processing.
   - **Implementation**:
     - Preprocess and chunk the data appropriately.
     - Insert the data into Qdrant, enabling vector-based searches and similarity queries.

3. **Transcript Generation with Local LLM**:
   - **Objective**: Generate a two-person conversational transcript suitable for a podcast.
   - **Implementation**:
     - Deploy a local language model (e.g., Llama) to process the stored data.
     - Craft prompts that instruct the model to create engaging dialogues based on the forum content.

4. **Audio Creation with Parler-TTS**:
   - **Objective**: Convert the generated transcripts into audio files using pre-trained voice models.
   - **Implementation**:
     - Utilize Parler-TTS to synthesize speech for each speaker in the transcript.
     - Ensure the voices are distinct and natural-sounding to enhance listener engagement.

5. **Video Compilation with FFmpeg**:
   - **Objective**: Combine the audio files with relevant images to create a video suitable for YouTube.
   - **Implementation**:
     - Use FFmpeg to merge the audio with either a static image or a slideshow of images related to the podcast content.

6. **Automated Upload to YouTube**:
   - **Objective**: Upload the generated video to YouTube as part of the ogrforum.com series.
   - **Implementation**:
     - Integrate the YouTube Data API within n8n to automate the upload process.
     - Include metadata such as title, description, tags, and playlist assignment to organize the content effectively.

## Running the Workflow

To run the entire workflow, follow these steps:

### Prerequisites

1. **Install Required Software**:
   - Ensure you have `n8n`, `Qdrant`, `FFmpeg`, and any other necessary tools installed on your system.
   - Set up a local LLM (e.g., Llama) and Parler-TTS for transcript generation and audio synthesis.

2. **Configuration**:
   - Update the `gpt_crawler/config.json` file with the correct base URL and patterns for data extraction.
   - Ensure compliance settings are correct to respect `robots.txt` and terms of service.

3. **Environment Variables**:
   - Set up any required API keys and environment variables for the YouTube Data API and other services.
   - Example: `export YOUTUBE_API_KEY=your_api_key_here`

### Workflow Execution Order

1. **Data Extraction**:
   - Run the `data_extraction.json` workflow in n8n to start the GPT-Crawler and extract data from the forum.

2. **Data Storage**:
   - Execute the `data_storage.json` workflow to store the extracted data in Qdrant.

3. **Transcript Generation**:
   - Run the `transcript_generation.json` workflow to generate conversational transcripts using the local LLM.

4. **Audio Synthesis**:
   - Execute the `audio_synthesis.json` workflow to convert transcripts into audio files with Parler-TTS.

5. **Video Creation**:
   - Run the `video_creation.json` workflow to combine audio with images and create video files using FFmpeg.

6. **YouTube Upload**:
   - Execute the `youtube_upload.json` workflow to upload the generated videos to YouTube.

### Additional Information

- **Error Handling**: Ensure that each step in the workflow has proper error handling to manage any issues that arise.
- **Resource Management**: Monitor system resources during execution, as some processes can be resource-intensive.
- **Legal Compliance**: Verify that all content usage complies with legal requirements and terms of service.

By following these steps, you can automate the process of creating and uploading podcast episodes from forum data.
