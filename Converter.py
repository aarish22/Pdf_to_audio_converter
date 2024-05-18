from gtts import gTTS
from PyPDF2 import PdfReader

def pdf_text_converter(pdf_file, start_page=None, end_page=None):
    text = ""
    try:
        with open(pdf_file, 'rb') as file:
            pdf_reader = PdfReader(file)
            total_pages = len(pdf_reader.pages)

            # Validate and adjust page range
            if start_page is None or start_page < 0:
                start_page = 0
            if end_page is None or end_page > total_pages:
                end_page = total_pages

            for page_num in range(start_page, end_page):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"An error occurred while reading the PDF file: {e}")
        return None

def text_audio_converter(text, output_file, language='en'):
    try:
        obj = gTTS(text, lang=language)
        obj.save(output_file)
        print("Conversion finished. Audio file saved as", output_file)
    except Exception as e:
        print(f"An error occurred during the text-to-speech conversion: {e}")

def main():
    pdf_file = input("Enter the path to the PDF file: ")
    start_page = int(input("Enter the starting page number (0-indexed, press Enter to start from the beginning): ") or 0)
    end_page = input("Enter the ending page number (press Enter to convert till the end): ")
    end_page = int(end_page) if end_page else None

    output_file = input("Enter the output audio file name (with .mp3 extension): ")
    language = input("Enter the language for the audio conversion (default is 'en' for English): ") or 'en'

    text = pdf_text_converter(pdf_file, start_page, end_page)
    if text:
        text_audio_converter(text, output_file, language)

if __name__ == "__main__":
    main()
