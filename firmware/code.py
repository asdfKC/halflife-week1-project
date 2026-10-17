## ANY BUTTONS THAT ARE PROGRAMMED TO USE THE SUPER KEY WILL ONLY RUN ON LINUX!!!

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
#All these imports are yellowed out because my computer doesn't have the libraries, the documentation says when I get the PICO I need to copy the folders over, which makes sense.

keyboard = KMKKeyboard() 

#pin definitions.
PINS = [
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16,  board.GP17
]

keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

#actions
keyboard.keymap = [[
    # this part is just cringe
    # I EVEN LET YOU PLAY VIDEO GAMES WITH ARROW KEYS!!!!!
    KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LCTRL(KC.X),
    KC.LCTRL(KC.Z), KC.LGUI(KC.L), KC.MUTE, 
    KC.PSCR, KC.MPRV, 
    KC.F11, KC.MPLY,
    KC.VOLD,  KC.MNXT,
    KC.VOLU, KC.LEFT,
    KC.UP, KC.DOWN,
    KC.ENTER, KC.RIGHT    
]]


#last starter

if __name__ == "__main__":
    keyboard.go() #first time not calling main in here :sob:
