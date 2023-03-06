import numpy as np



def calculate_position(time, starting_velocity, acceleration=-9.80665):
    return starting_velocity*time + 0.5*acceleration*time**2


def calculate_velocities(time, starting_velocity, acceleration=-9.80665):
    return starting_velocity + time*acceleration


def calculate_gravitational_potential_energy(position, mass, acceleration=-9.80665):
    return -mass * acceleration * position


def calculate_kinetic_energy(velocity, mass):
    return 0.5*mass*velocity**2


def parse_command_line():
    import sys
    mass, initial_velocity = float(sys.argv[1]), float(sys.argv[2])
    return mass, initial_velocity


def plot_energies(x_values, y_values):
    import matplotlib.pyplot as plt

    plt.plot(x_values, y_values[0], x_values, y_values[1], x_values, y_values[0] + y_values[1])
    plt.show()

    return


if __name__ == '__main__':
    standard_gravity = 9.80665
    object_mass, initial_velocity = parse_command_line()
    initial_time, final_time = 0, 2*initial_velocity / standard_gravity
    times = np.linspace(initial_time, final_time)
    positions = calculate_position(times, initial_velocity)
    print('t = [', times[0], ', ', times[-1], ']')
    print('y = [', positions[0], ', ', positions[-1], ']')
    potential_energies = calculate_gravitational_potential_energy(positions, object_mass)
    print('P = [', potential_energies, ']')
    velocities = calculate_velocities(times, initial_velocity)
    kinetic_energies = calculate_kinetic_energy(velocities, object_mass)

    plot_energies(times, [potential_energies, kinetic_energies])





