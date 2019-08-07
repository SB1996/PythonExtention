import numpy as np
import matplotlib.pyplot as plt

Xaxis = [10,20,30,40,50]
Yaxis = [1,2,3,4,5]

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

plt.plot(Xaxis,Yaxis,'k')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("Graph",loc= "left",fontdict = font,pad= 100)
plt.suptitle("-----------  Simple Grapg  -----------")
plt.show()