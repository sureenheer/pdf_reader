from gtts import gTTS
import PyPDF2
import pygame
import io

def play_text(text):
    tts = gTTS(text, lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.music.load(fp, 'mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def read_pdf(filepath):
    pygame.mixer.init()
    with open(filepath, 'rb') as pdf:
        pdfReader = PyPDF2.PdfReader(pdf)
        text = ''
        for page_num in range(len(pdfReader.pages)):
            page = pdfReader.pages[page_num]
            text += page.extract_text()
        if text:
            play_text(text)
    pdf.close()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()