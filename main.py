def on_logo_pressed():
    basic.show_icon(IconNames.CHESSBOARD)
    servos.P0.set_angle(90)
    servos.P1.set_angle(90)
    servos.P2.set_angle(90)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_gesture_shake():
    music.play_melody("E C C5 - C5 G - G ", 500)
    for index in range(4):
        basic.show_leds("""
            # # # # #
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # # # #
        """)
        basic.show_leds("""
            . . . . .
                        # # # # #
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.clear_screen()
        music.play_melody("E C C5 - C5 G - G ", 500)
        music.play_melody("E C C5 - C5 G - G ", 500)
    music.play_melody("E C C5 - C5 G - G ", 500)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
    basic.show_icon(IconNames.CHESSBOARD)
    basic.show_string("Mami")
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("Hoi Samuel")