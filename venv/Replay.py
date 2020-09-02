from pynput.mouse import Button, Controller
import pickle

mouse = Controller()

pickle_file = open("movements.pkl", 'rb')
movements = pickle.load(pickle_file)
pickle_file.close()
for x_y in movements:
    mouse.position = x_y

print(movements)
