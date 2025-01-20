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

## Additional Considerations

- **Legal Compliance**: Ensure that crawling and repurposing content from ogrforum.com complies with their terms of service and copyright laws.
- **Resource Management**: Running local models and processing media files can be resource-intensive; ensure your hardware meets the necessary requirements.
- **Error Handling**: Implement robust error handling within n8n to manage potential issues during crawling, data processing, or uploading.
