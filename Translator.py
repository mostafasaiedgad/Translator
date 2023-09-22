import tkinter as tk
from tkinter import ttk
from tkinter import *
from libretranslatepy import LibreTranslateAPI
from gtts import gTTS
import pygame

it = LibreTranslateAPI("https://translate.argosopentech.com/")
language_data = it.languages()

def language_names():
    list_of_names = []
    for i in language_data:
        list_of_names.append(i.get('name'))
    return list_of_names

language_names = language_names()

def language_codes():
    dict_of_codes = {i['name'] : i['code'] for i in language_data}
    return dict_of_codes

language_codes = language_codes()

window = Tk()
window.geometry('400x520+340+100')
window.title('Translator')
icon = PhotoImage(file=r"D:\MSA\Python Projects\Translator\photos\translate.png")
window.iconphoto(False, icon)
window.resizable(False, False)

class Window_translator:

    def __init__(self):
        self.window_translator = Toplevel()
        self.window_translator.geometry('400x520+340+100')
        self.window_translator.title('Translator')
        self.window_translator.iconphoto(False, icon)
        self.window_translator.resizable(False, False)

        self.text_1 = Label(self.window_translator, text='Translate anything!', bg='cadetblue3', fg='black', font=2)
        self.text_1.pack(fill='x')

        self.text_2 = Label(self.window_translator, text='From :', fg='black', font=('Bell MT', 15))
        self.text_2.place(x=15, y=80)

        self.from_language = ttk.Combobox(self.window_translator, width=19, values=language_names)
        self.from_language.place(x=85, y=85)
        self.from_language.set('choose the language')
        
        self.text_3 = Label(self.window_translator, text='To :', fg='black', font=('Bell MT', 15))
        self.text_3.place(x=15, y=250)

        self.to_language = ttk.Combobox(self.window_translator, width=19, values=language_names)
        self.to_language.place(x=85, y=255)
        self.to_language.set('choose the language')

        self.input_text_1 = Text(self.window_translator, height=7, width=40)
        self.input_text_1.place(x=15, y=120)

        self.input_text_2 = Text(self.window_translator, height=7, width=40)
        self.input_text_2.place(x=15, y=290)

        self.translate_button = Button(self.window_translator, text='Translate', width=12, 
        font=('Bell MT', 12), bg='cadetblue3', command=self.translate)
        self.translate_button.place(x=135, y=420)

        self.clear = Button(self.window_translator, text='Clear', width=12, 
        font=('Bell MT', 12), bg='cadetblue3', command=self.clear)
        self.clear.place(x=135, y=460)

        self.sound_1 = Button(self.window_translator, text='▶', width=4, 
        font=('Bell MT', 12), bg='cadetblue3', command=self.play_sound_1)
        self.sound_1.place(x=240, y=80)

        self.sound_2 = Button(self.window_translator, text='▶', width=4, 
        font=('Bell MT', 12), bg='cadetblue3', command=self.play_sound_2)
        self.sound_2.place(x=240, y=250)

    def translate(self):
        translated_text = it.translate(self.input_text_1.get('1.0', END),
        language_codes[self.from_language.get()], language_codes[self.to_language.get()])
        self.input_text_2.insert('1.0', translated_text)

    def clear(self):
        self.input_text_1.delete('1.0', END)
        self.input_text_2.delete('1.0', END)

    def play_sound_1(self):
        mytext = self.input_text_1.get('1.0', END)
        path = fr'D:\MSA\Python Projects\Translator\sounds\{mytext[:4]}.mp3'
        tts = gTTS(mytext, lang=language_codes[self.from_language.get()])
        tts.save(path)
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue


    def play_sound_2(self):
        mytext = self.input_text_2.get('1.0', END)
        path = fr'D:\MSA\Python Projects\Translator\sounds\{mytext[:4]}.mp3'
        tts = gTTS(mytext, lang=language_codes[self.from_language.get()])
        tts.save(path)
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

text_1 = Label(text='Get ready to\nexperience the best translation app!', bg='cadetblue3', fg='black', font=2)
text_1.pack(fill='x')

image = PhotoImage(file=r"D:\MSA\Python Projects\Translator\photos\translate.png")
resized_image = image.subsample(3)
label = tk.Label(window, image=resized_image)
window_width = window.winfo_width()
window_height = window.winfo_height()
label.place(x=105, y=150)

text_2 = Label(text='From MSA', fg='black', font=('Elephant', 25))
text_2.place(x=105, y=450)

def open_window_translator():
    Window_translator()

window.after(3000, open_window_translator)

window.mainloop()

