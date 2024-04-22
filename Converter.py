from gtts import gTTS
from PyPDF2 import PdfReader

def pdf_text_converter(pdf_file):
    text = ""
    with open(pdf_file,'rb') as x:
        pdf_reader = PdfReader(x)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = text + page.extract_text()
    return text

def text_audio_converter(text , output_file):
    obj = gTTS(text)
    obj.save(output_file)
    print("Conversion finished. Audio file saved as", output_file)
    
def main():
    pdf_file = input("Enter the path to the PDF file: ")
    audio = "converted_pdf.mp3"

    text = pdf_text_converter(pdf_file)
    text_audio_converter(text ,audio)

if __name__ == "__main__":
    main()