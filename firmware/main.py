print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.col_pins = (board.COL1, board.COL2, board.COL3, board.COL4, board.COL5, board.COL6,
                     board.COL7, board.COL8, board.COL9, board.COL10, board.COL11, board.COL12)
keyboard.row_pins = (board.ROW1, board.ROW2, board.ROW3, board.ROW4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers = Layers()
keyboard.modules.append(layers)

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP34, board.GP45, board.GP46),)
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]
keyboard.modules.append(encoder_handler)

______ = KC.TRNS

keyboard.keymap = [
    [
        KC.TAB,  KC.TAB,  KC.Q,    KC.W,     KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        KC.CAPS, KC.CAPS, KC.A,    KC.S,     KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.ENT,
        KC.LSFT, KC.LSFT, KC.Z,    KC.X,     KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.RSFT, KC.RSFT, KC.RSFT,
        KC.LCTL, KC.LCMD, KC.LALT, KC.MO(1), KC.SPC,  KC.SPC,  KC.SPC,  KC.SPC,  KC.RALT, KC.BSPC, KC.BSPC, KC.BSPC,
    ],
    [
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQUAL,
        KC.LBRC, KC.RBRC, KC.SCLN, KC.QUOT, KC.BSLS, KC.COMM, KC.DOT,  KC.SLSH, KC.UNDS, KC.PLUS, KC.NO,   KC.NO,
        KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
    ],
    [
        KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.NO,
        ______,  ______,  ______,  ______,  ______,  ______,  ______,  ______,  ______,  ______,  ______,  ______,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
    ],
]

if __name__ == '__main__':
    keyboard.go()