from tkinter import *
import pywhatkit
import pyaudio
import speech_recognition as sr
import pyttsx3
global apple
apple="What do you want to see?"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
y=Tk()
y.title("Type your video to play and press 'Go' or use microphone")
def ex():
    global a
    string = a.get() 
    pywhatkit.playonyt(string)
      
def fr():
    rap=sr.Recognizer()
    speak("Listening...")
    y.title("Listening...")
    with sr.Microphone() as source:
        rap.pause_threshold=0.5
        audio=rap.listen(source)
    try:
        h = rap.recognize_google(audio, language='en-in')
        y.title(h)
        speak("playing"+h)
        pywhatkit.playonyt(h)
        y.title("Type your video to play and press 'Go' or use microphone")
    except:
        speak("Failed to recognize audio")
        y.title("Type your video to play and press 'Go' or use microphone")
a=Entry(y,width=37,bg="white",font=("Comic Sans MS",13))
a.grid(row=1,column=1)    
w=Label(y,text=apple,bg="green",font=("calibri",25,"bold",))
w.grid(row=0,column=1) 
e=Button(y,height=1,width=20,text="Go",bg="blue",fg="white",activebackground="dark blue",command=lambda:ex())
e.grid(row=1,column=2)
e.focus_set()
foo=Button(y,height=1,width=20,text="mic",bg="red",fg="white",activebackground="dark red",command=lambda:fr())
foo.grid(row=1,column=3)
y.configure(background=("green"))
y.mainloop()
