from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from gtts import gTTS
import googletrans
from googletrans import Translator
import pyttsx3
import tkinter as tk
global trans_text
import pytesseract
import pywhatkit as kit
import pyaudio
import speech_recognition as sr
import PyPDF2
root = Tk()
root.geometry("612x433")

root.title("welcome!")
label = Label(root, text=" WELCOME ALL",font="segue 15 bold").pack()
l1 = Label()


def clicked():
    r1 = Tk()
    r1.title("Google Translator")
    r1.geometry("1080x700")
    r1.resizable(False, False)
    r1.configure(background="white")
    language = googletrans.LANGUAGES
    languageV = list(language.values())
    lang1 = language.keys()
    combo1 = ttk.Combobox(r1, values=languageV, font="Roboto 14", state="r")
    combo1.place(x=90, y=20)
    combo1.set("ENGLISH")
    label1 = Label(r1, text="ENGLISH", font="segue 15 bold", bg="white", width=14, bd=5, relief=GROOVE)
    label1.place(x=90, y=70)
    combo2 = ttk.Combobox(r1, values=languageV, font="Roboto 14", state="r")
    combo2.place(x=650, y=20)
    combo2.set("Select Language")
    label2 = Label(r1, text="ENGLISH", font="segue 15 bold", bg="white", width=14, bd=5, relief=GROOVE)
    label2.place(x=650, y=70)

    def label_change():
        c = combo1.get()
        c1 = combo2.get()
        label1.configure(text=c)
        label2.configure(text=c1)
        root.after(1000, label_change)

    def translate_now():
        t1 = Translator()
        trans_text = t1.translate(text1.get(1.0, END), src=combo1.get(), dest=combo2.get())
        trans_text = trans_text.text
        text2.delete(1.0, END)
        text2.insert(END, trans_text)

    def text_to_speech():
        myText = text2.get(1.0, END)
        my_dict = {'af': 'afrikaans', 'sq': 'albanian', 'ar': 'arabic', 'hy': 'armenian', 'bn': 'aengali',
                   'bs': 'bosnian', 'ca': 'catalan', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch',
                   'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish',
                   'fr': 'french', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'hi': 'hindi', 'hu': 'hungarian',
                   'is': 'icelandic', 'id': 'indonesian', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese',
                   'kn': 'kannada', 'km': 'khmer', 'ko': 'korean', 'la': 'latin', 'lv': 'latvian', 'mk': 'macedonian',
                   'ml': 'malayalam', 'mr':
                       'marathi', 'my': 'myanmar (Burmese)', 'ne': 'nepali', 'no': 'norwegian', 'pl': 'polish',
                   'pt': 'portuguese', 'ro': 'romanian', 'ru': 'russian', 'sr': 'serbian', 'si': 'sinhala',
                   'sk': 'slovak', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'ta': 'tamil',
                   'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'vi': 'vietnamese',
                   'cy': 'welsh', 'zh-cn': 'chinese (Mandarin/China)', 'zh-tw': 'chinese (Mandarin/Taiwan)',
                   'en-us': 'english (US)', 'en-ca': 'english (Canada)', 'en-uk': 'english (UK)',
                   'en-gb': 'english (UK)', 'en-au': 'english (Australia)', 'en-gh': 'english (Ghana)',
                   'en-in': 'english (India)', 'en-ie': 'english (Ireland)', 'en-nz': 'english (New Zealand)',
                   'en-ng': 'english (Nigeria)', 'en-ph': 'english (Philippines)', 'en-za': 'english (South Africa)',
                   'en-tz': 'english (Tanzania)', 'fr-ca': 'french (Canada)', 'fr-fr': 'french (France)',
                   'pt-br': 'portuguese (Brazil)', 'pt-pt': 'portuguese (Portugal)', 'es-es': 'spanish (Spain)',
                   'es-us': 'spanish (United States)'}
        language = combo2.get()

        key_list = list(my_dict.keys())
        val_list = list(my_dict.values())
        position = val_list.index(language)
        l = key_list[position]
        output = gTTS(text=myText, lang=l, slow=False)
        output.save("output.mp3")
        os.system("output.mp3")
    def usingVoice():
        r=sr.Recognizer()
        count=1

        while(count==1):
            with sr.Microphone() as source:
                try:
                    count=0
                    engine = pyttsx3.init()
                    engine.say("What is the input language !")
                    engine.runAndWait()
                    r.pause_threshold = 1
                    audio = r.listen(source)
                    voice_data = r.recognize_google(audio)
                    set1 = voice_data.lower()
                    combo1.set(set1)
                    r.pause_threshold = 1
                    engine.say("What is the Output language !")
                    engine.runAndWait()
                    audio = r.listen(source)
                    voice_data = r.recognize_google(audio)
                    set2 = voice_data.lower()
                    combo2.set(set2)
                    engine.say("What is the  Text !")
                    engine.runAndWait()
                    r.pause_threshold = 1
                    audio = r.listen(source)
                    voice_data = r.recognize_google(audio)
                    text1.delete(1.0, END)
                    text1.insert(END, voice_data)
                    engine.say("Here is your translated text!")
                    translate_now()
                    text_to_speech()
                except:
                    engine.say("Sorry couldn't get you!!Try again from the starting!!")
                    count = 1

    f = Frame(r1, bg="Black", bd=5)
    f.place(x=10, y=118, width=440, height=210)
    text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
    text1.place(x=0, y=0, width=430, height=200)

    scrollbar1 = Scrollbar(f)
    scrollbar1.pack(side="right", fill='y')

    scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=scrollbar1.set)

    f1 = Frame(r1, bg="Black", bd=5)
    f1.place(x=620, y=118, width=440, height=210)
    text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
    text2.place(x=0, y=0, width=430, height=200)

    scrollbar2 = Scrollbar(f1)
    scrollbar2.pack(side="right", fill='y')

    scrollbar2.configure(command=text2.yview)
    text2.configure(yscrollcommand=scrollbar2.set)

    translate = Button(r1, text="Translate", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1,
                       width=10, height=2, bg="black", fg="white", command=translate_now)
    translate.place(x=700, y=350)
    bt_speech = Button(r1, text="Text to speech", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1,
                       width=30, height=2, bg="black", fg="white", command=text_to_speech)
    bt_speech.place(x=70, y=500)
    bt_speech1 = Button(r1, text="USING VOICE", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1,
                       width=30, height=2, bg="black", fg="white", command = usingVoice)
    bt_speech1.place(x=70, y=350)



    label_change()
    r1.mainloop()


def speech():
    r2 = Tk()

    def in_speech():
        engine = pyttsx3.init()
        engine.say(text1.get(1.0, END))
        engine.runAndWait()


    def pdf():
        filepath = filedialog.askopenfilename()
        a = PyPDF2.PdfFileReader(filepath)
        str_pdf = ""
        for i in range(a.getNumPages()):
            str_pdf += a.getPage(i).extractText()
        output1 = gTTS(text=str_pdf, lang='en', slow=False)
        output1.save("output1.mp3")
        os.system("output1.mp3")

    r2.title("TEXT TO SPEECH")
    r2.geometry("1080x500")
    r2.resizable(False, False)
    r2.configure(background="white")
    la1 = Label(r2, text="Text", font="segue 15 bold", bg="white", width=18, bd=5, relief=GROOVE)
    la1.place(x=10, y=50)
    f = Frame(r2, bg="Black", bd=5)
    f.place(x=10, y=118, width=440, height=210)
    text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
    text1.place(x=0, y=0, width=430, height=200)

    scrollbar1 = Scrollbar(f)
    scrollbar1.pack(side="right", fill='y')

    scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=scrollbar1.set)
    bt56 = Button(r2, text="Text to speech", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1,
                  width=20, height=3, command= in_speech)
    bt56.place(x=700, y=100)
    bt_pdf= Button(r2, text="Pdf", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1,
                  width=20, height=3,command=pdf)
    bt_pdf.place(x=700, y=300)
    r2.mainloop()



def text_Hand_Written():
    r4 = Tk()
    r4.title("TEXT TO HAND WRITTEN")
    r4.geometry("500x500")
    r4.resizable(False, False)
    r4.configure(background="white")
    label1 = Label(r4, text="Text to hand written", font="segue 15 bold", bg="white", width=18, bd=5, relief=GROOVE)
    label1.place(x=100, y=50)
    f = Frame(r4, bg="Black", bd=5)
    f.place(x=10, y=118, width=440, height=210)
    text1 = Text(f, font="Roboto 15", bg="white", relief=GROOVE, wrap=WORD)
    text1.place(x=0, y=0, width=430, height=200)

    scrollbar1 = Scrollbar(f)
    scrollbar1.pack(side="right", fill='y')

    scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=scrollbar1.set)
    def open():
        filepath = filedialog.askopenfilename()
        os.chdir(r'C:\Users\Sneha\Documents\mini project')
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        img1 = Image.open(filepath, 'r')
        text = pytesseract.image_to_string(img1)
        kit.text_to_handwriting(text, rgb=[0, 0, 250])
        print("Process completed")
    def input_text():
        text = text1.get(1.0, END)
        os.chdir(r'C:\Users\Sneha\Documents\mini project')
        kit.text_to_handwriting(text, rgb=[0, 0, 250])



    bt_text = Button(r4, text="UPLOAD", width=30, height=1, command=open)
    bt_text.place(x=70, y=400)
    bt_text1 = Button(r4, text="Download", width=30, height=1, command=input_text)
    bt_text1.place(x=70, y=450)

    r4.mainloop()


bt1 = Button(root, text="Translate", font="segue 15 bold", bg="white",width=30, command=clicked)
bt2 = Button(root, text="Text to speech",font="segue 15 bold", bg="white", width=30, command=speech)

bt4 = Button(root, text="Text to Hand written", font="segue 15 bold", bg="white", width=30, command=text_Hand_Written)
l1.pack()
bt1.pack(side=TOP, pady=3)
bt2.pack(side=TOP, pady=6)

bt4.pack(side=TOP, pady=12)
root.mainloop()
