# =======================================
#  Plotting Diagrams
# =======================================

import matplotlib.pyplot as plt
import numpy as np
# get_ipython().run_line_magic('matplotlib', 'inline')
temp = np.loadtxt('Data\temperature.txt')
plt.plot(temp, 'r--')
plt.show()

# =======================================

x = np.arange(len(temp))
plt.scatter(x, temp)
plt.show()

# =======================================
#  Figure Title and Axis Labels
# =======================================

plt.plot(temp)
plt.title("Temperature in Singapore each month from 1980 January to 2000 October")
plt.xlabel("Num of months passed from 1980 January")
plt.ylabel("Temperature in degrees celcius")
plt.show()

# =======================================
#  Multiple
# =======================================

new_temp = np.loadtxt('temperature2.txt')
plt.plot(new_temp, "g--")

# =======================================
# Object Oriented
# fig = plt.figure()
# ax1 = fig.add.subplot(2, 1, 1)
# ax2 = fig.add.subplot(2, 1, 2)
# ax1.plot(temp, ':')
# ax1.set_ylabel("Average")
# ax1.set_title("Kelburn 1980 - 2000")
# ax2.plot(new_temp, "-.")
# ax2.set_ylabel("Maximum")
# ax2.set_xlabel("Paraparaumu Aero 2000-2018")
# Matlab Static
fig = plt.figure()
plt.subplot(2, 1, 1)
plt.plot(temp)
plt.title("1980 - 2000 Kelburn")
plt.ylabel("Average")
plt.plot(new_temp)
plt.title("2000 - 2018 Paraparaumu")
plt.ylabel("Maximum")
plt.show()

# =======================================
#  Saving Figures
# =======================================

plt.plot(new_temp)
plt.savefig("temp2.png")
fig.savefig("temperature2.jpeg")
