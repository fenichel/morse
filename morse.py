# play morse code
import winsound
from time import sleep

UNIT_MS = 500
UNIT_S = .5

DOT = "."
DASH = "-"

LETTERS = {
"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--..",
}

def dash():
    winsound.Beep(1000, UNIT_MS * 3)

def dot():
    winsound.Beep(1000, UNIT_MS)

def short_pause():
    sleep(UNIT_S)

def letter_pause():
    sleep(UNIT_S * 3)

def word_pause():
    sleep(UNIT_S * 7)

def play_letter(letter):
    print(letter)
    if letter == " ":
        word_pause()
    else:
        letter = letter.upper()
        encoding = LETTERS[letter]
        for sound in encoding:
            print(sound)
            if sound == DOT:
                dot()
            elif sound == DASH:
                dash()
            short_pause()
        letter_pause()

def play_string(to_play):
    for c in to_play:
        play_letter(c)

def print_string_in_morse(to_print):
    for c in to_print:
        if c == " ":
            print(" ")
        else:
            print(LETTERS[c.upper()])

while True:
    string_to_play = input("Request input>")
    play_string(string_to_play)
    print(" ")