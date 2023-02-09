import wikipedia
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()


def chat(text):
    result=wikipedia.summary(text, sentences=3)
    if result:
        print(result)
        say(result)

Quit = True
while Quit:
    q = input("Ask question: ")
    if q != "quit":
        chat(q)
    else:
        break
    