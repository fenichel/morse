# play morse code
import winsound
from time import sleep

UNIT_MS = 500
UNIT_S = .5

DOT = 0
DASH = 1

LETTERS = {
"A" : [DOT, DASH],
"B" : [DASH, DOT, DOT, DOT],
"C" : [DASH, DOT, DASH, DOT],
"D" : [DASH, DOT, DOT],
"E" : [DOT],
"F" : [DOT, DOT, DASH, DOT],
"G" : [DASH, DASH, DOT],
"H" : [DOT, DOT, DOT, DOT],
"I" : [DOT, DOT],
"J" : [DOT, DASH, DASH, DASH],
"K" : [DASH, DOT, DASH],
"L" : [DOT, DASH, DOT, DOT],
"M" : [DASH, DASH],
"N" : [DASH, DOT],
"O" : [DASH, DASH, DASH],
"P" : [DOT, DASH, DASH, DOT],
"Q" : [DASH, DASH, DOT, DASH],
"R" : [DOT, DASH, DOT],
"S" : [DOT, DOT, DOT],
"T" : [DASH],
"U" : [DOT, DOT, DASH],
"V" : [DOT, DOT, DOT, DASH],
"W" : [DOT, DASH, DASH],
"X" : [DASH, DOT, DOT, DASH],
"Y" : [DASH, DOT, DASH, DASH],
"Z" : [DASH, DASH, DOT, DOT],
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
            if sound == DOT:
                dot()
                print(".")
            elif sound == DASH:
                dash()
                print("-")
            short_pause()
        letter_pause()

def play_string(to_play):
    for c in to_play:
        play_letter(c)

while True:
    string_to_play = input("Request input>")
    play_string(string_to_play)
    print(" ")