from pynput.mouse import Button, Controller
import pickle
import time

mouse = Controller()

pickle_file = open("movements.pkl", 'rb')
movements = pickle.load(pickle_file)
pickle_file.close()
previous_movement = movements[0]
previous_time = previous_movement[2]
for x_y_timenow in movements:
    x_y = x_y_timenow[:2]
    time_of_movement = x_y_timenow[2]
    difference = time_of_movement - previous_time
    time.sleep(difference)
    mouse.position = x_y
    previous_time = time_of_movement

print(movements)
