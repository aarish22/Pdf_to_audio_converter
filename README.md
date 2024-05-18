# 📄 PDF to Audio Converter

## About the Project

This project is a Python-based application that converts the text content of PDF files into audio files using the Google Text-to-Speech (gTTS) library. It allows users to specify the range of pages to convert, choose the output file name, and select the language for the text-to-speech conversion.

## Features

- **Page Range Selection**: Convert a specific range of pages from the PDF.
- **Custom Output File Name**: Specify the name of the output audio file.
- **Language Selection**: Choose the language for the text-to-speech conversion.
- **Error Handling**: Robust error handling for file operations and conversion processes.

## Technologies Used

- **Python**: The core programming language used for the project.
- **gTTS**: Google Text-to-Speech library for converting text to audio.
- **PyPDF2**: Library for reading and extracting text from PDF files.

## How It Works

1. **Input PDF File**: The user is prompted to enter the path to the PDF file.
2. **Specify Page Range**: The user can specify the starting and ending page numbers for conversion.
3. **Output File Name**: The user can specify the name of the output audio file.
4. **Language Selection**: The user can choose the language for the audio conversion.
5. **Convert and Save**: The text from the specified pages of the PDF is converted to speech and saved as an audio file.

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/pdf-to-audio-converter.git
    cd pdf-to-audio-converter
    ```

2. **Install Dependencies**:
    Ensure you have the required libraries installed. If not, install them using:
    ```bash
    pip install gtts PyPDF2
    ```

3. **Run the Script**:
    ```bash
    python pdf_to_audio.py
    ```

4. **Follow the Prompts**:
    - Enter the path to the PDF file.
    - Enter the starting page number (optional, press Enter to start from the beginning).
    - Enter the ending page number (optional, press Enter to convert till the end).
    - Enter the output audio file name (with .mp3 extension).
    - Enter the language for the audio conversion (default is 'en' for English).

## Example

```plaintext
Enter the path to the PDF file: /path/to/your/file.pdf
Enter the starting page number (0-indexed, press Enter to start from the beginning): 0
Enter the ending page number (press Enter to convert till the end): 5
Enter the output audio file name (with .mp3 extension): output.mp3
Enter the language for the audio conversion (default is 'en' for English): en
Download Started...
Conversion finished. Audio file saved as output.mp3
