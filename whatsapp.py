from selenium import webdriver
import speech_recognition as sr
import playsound
import pyautogui
from gtts import gTTS
import os


num = 1
def speak(output):
    global num
    num += 1
    toSpeak = gTTS(text = output, lang ="en-uS", slow = False)
    file = str(num)+".mp3"
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)

def virtual_listen():

    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        audio = rObject.listen(source, phrase_time_limit = 5)
    try:
        text = rObject.recognize_google(audio, language ='en-US')
        return text
    except:
        return

def working(name):
    print(name)
    dic={called_name_1:contact_name_1,
        called_name_2:contact_name_2,
        called_name_3:contact_name_3}
    if name in dic:
        contact_name=dic[name]
        while(1):
            speak("What should I send")
            msg=virtual_listen()
            if msg == None:
                speak("Try again")
                break
            else:
                user = driver.find_element_by_xpath("//span[@title='{}']".format(contact_name))
                user.click()
                msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
                msg_box.send_keys(msg)
                driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
                speak("whant to send another message")
                answer = virtual_listen()
                if answer == "yes":
                    continue
                else:
                    break

    else:
        speak("No such contact found")

def whatsapp_message():
    while(1):
        audio = virtual_listen()
        if audio!=0:
            if audio == None:
                continue
            if "exit" in str(audio) or "stop" in str(audio) or "nothing" in str(audio) or "turn off" in str(audio):
                speak("Turning off Message mode")
                driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div").click()
                driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[7]").click()
                break

            if "send" in audio or "Send" in audio:
                speak("whom shall i send:")
                audio = virtual_listen()
                if audio!=None:
                        text = audio
                else:
                    speak("Try Again")
                    continue
                text = audio
                working(text.lower())
            else:
                continue
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
speak("scan QR code")
whatsapp_message()
