import csv
import webbrowser

import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
import os  # to remove created audio files

class Factor(object):
    def __init__(self, id, name, status, time):
        self.id = id
        self.name = name
        self.status = status
        self.time = time

    def show(self):
        print("id: " + str(self.id) + "; name: " + str(self.name) + "; status: " + str(self.status) + "; time: " + str(
            self.time))
        return


class Person(Factor):
    def __init__(self, name, location):
        self.disease = None
        self.name = name
        self.location = location


class HomeAppliance(Factor):
    def __init__(self, location, effectLevel):
        self.location = location
        self.effectLevel = effectLevel


class Environment(Factor):
    def __init__(self, temperature, humidity, noiseLevel):
        self.temperature = temperature
        self.humidity = humidity
        self.noiseLevel = noiseLevel

    def getEnvironmentInfo(self):
        print("temperature: " + str(self.temperature) + "; humidity: " + str(self.humidity) + "; noiseLevel: " + str(
            self.noiseLevel))
        return


class VirtualSpace(object):
    def __init__(self, size, location, Persons, appliances, environment):
        self.factors = None
        self.size = size
        self.location = location
        self.Persons = Persons
        self.appliances = appliances
        self.environment = environment

    def show(self):
        print("size: " + str(self.size) + "; location: " + str(self.location) + "; factors: " + str(self.factors))
        return

class Reasoning(object):
    def __init__(self, refSmartHome):
        self.refSmartHome = refSmartHome

    def getEnvironmentInfo(self):
        return self.refSmartHome.environment


    def determineDisease(self, bpress):
        env = self.getEnvironmentInfo()
        seve = "none"
        posdis = []
        if 40 > env.temperature or env.temperature < -20 and env.noiseLevel > 80 and bpress not in range(90, 120):
            dangerFactor = random.randint(7, 10)
        elif env.temperature > 38 or env.temperature < -15 and env.noiseLevel > 70 and bpress not in range(90, 120):
            dangerFactor = random.randint(4, 7)
        elif env.temperature > 35 or env.temperature < -10 and env.noiseLevel > 70 or bpress not in range(90, 120):
            dangerFactor = random.randint(2, 4)
        elif env.temperature > 32 or env.temperature < -5 and env.noiseLevel > 60 or bpress not in range(90, 120):
            dangerFactor = random.randint(0, 2)
        else:
            dangerFactor = random.randint(0, 1)

        if dangerFactor > 8:
            seve = "emergency"
        elif dangerFactor > 6:
            seve = "warning"
        elif dangerFactor > 3:
            seve = "normal"
        elif dangerFactor > 0:
            seve = "low"
        with open('diseases.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if seve == line[1]:
                    posdis.append(line[0])
                    name = ", ".join(posdis)

        dis = Disease(seve, name)
        return dis

    def assignDiseases(self, bpress):
        pers = self.refSmartHome.Persons
        pers.disease = self.determineDisease(bpress)


class Disease(object):
    def __init__(self, severity, name):
        self.name = name
        self.severity = severity


def findPerson(pers_id):
    counter = 0
    with open('persons.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if pers_id == int(line[0]):
                envTemperature = int(line[2])
                humiditiy = int(line[3])
                bloodpressure = int(line[4])
                noiseLevel = int(line[5])
                env1 = Environment(envTemperature, humiditiy, noiseLevel)
                p1 = Person(line[1], line[6])
                homeapp = HomeAppliance(line[6], 100)
                vspace = VirtualSpace(1, line[6], p1, homeapp, env1)
                reasoning1 = Reasoning(vspace)
                reasoning1.assignDiseases(bloodpressure)
                return line[1] + "'s conditions of " + p1.disease.severity + " severity can lead to " + p1.disease.name
                counter = counter + 1
    if counter == 0:
        return "can't find id, make sure to add patient"


def there_exists(terms, voice_data):
    for term in terms:
        if term in voice_data:
            return True


r = sr.Recognizer()  # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down')
        return voice_data.lower()


# get string and make an play an audio file of it
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    os.remove(audio_file)  # remove audio file
    return f" {audio_string}"


def respond(voice_data):
    # 1: greeting
    if there_exists(['hey', 'hi', 'hello', 'greetings', 'sup'], voice_data):
        greetings = [f"hey, how can I help you ", f"hey, what's up? ",
                     f"I'm listening", f"how can I help you? ",
                     f"hello"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        return speak(greet)

    if there_exists(["how are you", "how are you doing"], voice_data):
        return speak(f"I'm very well, thanks for asking ")

    # 2: name
    if there_exists(["what is your name", "what's your name", "tell me your name"], voice_data):
        return speak("my name is Sandy")

    # 3: report
    if there_exists(["report", "reporting", "reports", "status", "data"], voice_data):
        return speak("Okay, i'll look for it. but first, what's the patient's ID?")

    if there_exists(["the id is", "my id is", "id is"], voice_data):
        person_id = voice_data.split("is")[-1].strip()
        return speak(findPerson(int(person_id)))

    # 4: plot
    if there_exists(["plot", "plotting", "graph"], voice_data):
        return speak("Here you go")

    # 5: search google
    if there_exists(["search"], voice_data):
        search_term = voice_data.split("search")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        return speak(f'Here is what I found on google')