from datetime import datetime
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from grove_gsr_sensor import GroveGSRSensor
import time
import sys
import os.path
from grove_gsr_sensor import GroveGSRSensor
from csv import writer

style.use('fivethirtyeight')
fig = plt.figure()
axl = fig.add_subplot(1, 1, 1)

sensor = GroveGSRSensor(int(0))
x = []
gsr = []

participant = input("Enter a Participant Number:")
    
if os.path.isfile('data/Participant '+participant+' data.csv'):
    print ("This file already exists - please choose a new participant number")
    sys.exit(1)
        
print ("Creating file")

with open('data/Participant '+participant+' data.csv','w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['GSR'])

def get_bio_data():
    bio_data = []
    gsr2 = sensor.GSR
    dt = datetime.now()
    
    gsr.append(gsr2)
    bio_data.append(gsr2)
    x.append(dt)
    bio_data.append(dt)
        
    return bio_data

def animate(i):
    data = get_bio_data()
    log_data()
    axl.clear()
    axl.plot(x, gsr)
    axl.legend(["GSR"])
    plt.title('GSR over Time')
    plt.ylabel('GSR (Resistance)')
    print('GSR value: {0}'.format(sensor.GSR))

def log_data():
    data = ('{0}'.format(sensor.GSR))
        
    with open('data/Participant '+participant+' data.csv','a', newline='') as f:
        data_writer = writer(f)
        data_writer.writerow([data])
        time.sleep(.3)

ani = animation.FuncAnimation(fig, animate, interval=2)
plt.show()
