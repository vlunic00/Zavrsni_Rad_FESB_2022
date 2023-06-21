import csv
import random
random.seed()

def location(x_0, v_0, t):
    return x_0 + v_0*t - (9.8/2)*t**2

with open('dataset.csv', mode='w') as gravity_file:
    gravity_writer = csv.writer(gravity_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    gravity_writer.writerow(['initial_position', 'initial_velocity', 'mass', 'time', 'location'])

    for i in range (0, 10000):
        initial_position = random.randrange(1, 10000)
        initial_velocity = random.randrange(1, 100)
        mass = random.randrange(1, 1000)
        time = random.randrange(1, 100)
        gravity_writer.writerow(
            [initial_position, initial_velocity, mass, time, location(initial_position, initial_velocity, time)])