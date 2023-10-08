import win32com.client as wincl
import os   # For Mac.

speaker = wincl.Dispatch("SAPI.SpVoice")

def pronounce_text():
    while True:
        text = input("Enter text to pronounce: ")
        if text == 'exit' or text == 'Exit' or text == 'EXIT':
            speaker.Speak('Exit')
            break
        speaker.Speak(text)

if __name__ == "__main__":
    print('For Exit write exit or Exit or EXIT.')
    pronounce_text()


    #------For Mac---------

    # x = input("Enter : ")
    # command = f"say {x}"
    # os.system(command)
