import pyttsx3
import pygame
def speak(text):
        engine= pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
def play_sound(file_path):
       pygame.mixer.init#intiliazing the mixer module whihc is used for loading and playing sound
       pygame.mixer.music.load(file_path)#to specify the file_path to the mixer
       pygame.mixer.music.play()#to start playing the audio
      
       while pygame.mixer.music.get_busy():
           pygame.time.Clock().tick(10)



       
       
if __name__=='__main__':
    print("welcome to robospeaker 2.0,created by kashish")
    while True:
             x=input("enter what you want to say: ")
             if x == "q":
                 print("bye bye friend")
             break
    speak(x)
    audio_file= "hello friend"
    play_sound(audio_file)
    