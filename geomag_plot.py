## Python methods used to read in and plot data
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

def read_geomag_data():
    # Load rows of text and transpose to get collumns
    mag_data = np.genfromtxt("Geomag.txt", dtype=str).T
    # Convert string times to datetime objects
    day_time = zip(mag_data[0], mag_data[1])
    times = [dt.datetime.strptime(day+'_'+time, "%Y-%m-%d_%H:%M:%S.%f") for day, time in day_time]
    if len(times) == 0:
        times = np.arange(0, len(mag_data[0]))
        times = times/60
    # Get the components we want
    x, y, z, f = mag_data[3], mag_data[4], mag_data[5], mag_data[6]
    return times, x, y, z, f

def plot_geomag_data(comp):
    comp = comp.upper()
    # Get the components using the defined method
    times, x, y, z, f = read_geomag_data()
    # Check if the character passed in is a valid choice
    if comp != 'X' and comp != 'Y' and comp != 'Z' and comp != 'F':
        print('You did not enter a valid choice. Please try again.')
        return
    # Plot the data
    figure = plt.figure(figsize=(15,5))
    plt.title(comp + ' Component Recorded at Boulder on January 9, 2017', fontsize=24)
    plt.xlabel('Time [date]', fontsize=18)
    plt.ylabel('Magnetic Field [nT]', fontsize=18)
    if comp == 'X':
        plt.plot(times, x.astype(float), color='b')
    elif comp == 'Y':
        plt.plot(times, y.astype(float), color='k')
    elif comp == 'Z':
        plt.plot(times, z.astype(float), color='c')
    else:
        plt.plot(times, f.astype(float), color='m')
        plt.title('Total Field Recorded at Boulder on January 9, 2017', fontsize=24)
    plt.show()

plot_geomag_data('f')