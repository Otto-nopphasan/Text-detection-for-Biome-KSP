import cv2
import numpy as np
import pyautogui
import pytesseract as pytesseract
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# ====================================check list=======================================================#

All_biome = ["Poles", "Lowlands", "Midlands", "Highlands", "Peaks", "Dunes", "Degrasse Sea", "Crescent Bay",
             "Crater Bay", "Crater Island", "Slopes", "Shallows", "Shores", "Southern Basin", "Southern Valleys",
             "Northeast Basin", "Northwest Basin", "Mountains", "Mara", "Minor Craters", "Gagarin Crater",
             "Grissom Crater", "Galileio Crater", "Tycho Crater", "Valley", "Ridges", "The Sagen Sea"]

# =======================================info==========================================================#

biome = {"Poles": 0, "Lowlands": 0, "Midlands": 0, "Highlands": 0, "Peaks": 0, "Dunes": 0, "Degrasse Sea": 0, "Crescent Bay": 0,
             "Crater Bay": 0, "Crater Island": 0, "Slopes": 0, "Shallows": 0, "Shores": 0, "Southern Basin": 0, "Southern Valleys": 0,
             "Northeast Basin": 0, "Northwest Basin": 0, "Mountains": 0, "Mara": 0, "Minor Craters": 0, "Gagarin Crater": 0,
             "Grissom Crater": 0, "Galileio Crater": 0, "Tycho Crater": 0, "Valley": 0, "Ridges": 0, "The Sagen Sea": 0}
Have_biome = []
last_biome = ""
false = []

# ==========================================================================================================#

while(True):
    screenshot = ImageGrab.grab()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
    screenshot = cv2.bitwise_not(screenshot)
    cv2.imshow('Result', screenshot)
    text = pytesseract.image_to_string(screenshot)
    text = text.replace("\n", "*-*")
    pos_bio = text.find("Biome")
    pos_bio = pos_bio + 7
    pos_end = len(text)
    pos_tend = text.find("*-*", pos_bio, pos_end)
    cut_text = text[pos_bio : pos_tend]
    if cut_text != last_biome:
        if cut_text in All_biome:
            if not cut_text in Have_biome:
                Have_biome.append(cut_text)
            x = biome[cut_text]+1
            biome[cut_text] = x
            last_biome = cut_text
            print("========================", cut_text, "========================")
        else:
            false.append(cut_text)
    cut_text = ""
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

for i in range(0, len(Have_biome)):
    print(Have_biome[i], " : ", biome[Have_biome[i]])
print(false)