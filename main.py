def on_button_pressed_a():
    basic.show_number(steps)
    basic.pause(3000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global start_melody
    start_melody += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

start_melody = 0
steps = 0
steps = 0