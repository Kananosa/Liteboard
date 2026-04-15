print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.COL1,board.COL2,board.COL3,board.COL4,board.COL5,board.COL6,board.COL7,board.COL8,board.COL9,board.COL10,board.COL11,board.COL12)
keyboard.row_pins = (board.ROW1,board.ROW2,board.ROW3,board.ROW4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers = Layers()
keyboard.modules.append(layers)
keyboard.keymap = [
    [
        KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,   KC.LBRC,    KC.RBRC,
        KC.A,   KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L,   KC.SCLN,    KC.QUOT,    KC.BSLS,
        KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,    KC.DOT,     KC.SLSH 
        KC.LCTL,     KC.LCMD,   KC.LALT,   KC.SPC,      KC.SPC,     KC.SPC,     KC.RALT     
    ]

]

if __name__ == '__main__':
    keyboard.go()