from pynput.mouse import Listener
import pickle
movements = []

def on_move(x, y):
    movements.append([x,y])

def on_click(x, y, button, pressed):
    print(movements)
    f = open('movements.pkl', 'wb')
    pickle.dump(movements, f)
    f.close()
    exit()

    if not pressed:

        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))

# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()