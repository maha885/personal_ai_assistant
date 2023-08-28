import openai
import speech_recognition as sr
import win32com.client
import env



def say(text):
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        
        r.adjust_for_ambient_noise(source=source)
        audio=r.listen(source)
        query=r.recognize_google(audio, language='en-IN')
        #print(f"user said :{query}")
        return query

def chat(chats):
    openai.api_key=env.apply_key
    discussion = openai.Completion.create(
        prompt = chats,
        engine='text-davinci-002',
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        
    )
    return discussion["choices"][0]["text"]


if __name__=="__main__":
    say("Hello")
    print("Listening..")
    texts=takeCommand()
    say("I am preparing an answer for you")
    answer=chat(texts)
    say(answer)

    