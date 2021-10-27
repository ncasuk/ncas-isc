# matplotlib all tests
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.savefig("demo_1a.png")
plt.show()

print("USE plt.figure() or plt.show()")

plt.plot([0,0.5,1,1.2])
plt.plot([1,2,3,4])
plt.savefig("demo_1b.png")
plt.show()

times = [0, 0.25, 0.5, 0.75]
plt.plot(times, [0,0.5,1,1.2], 'g--', times, [1,2,3,4], 'r')
plt.ylabel('Concentration (%)')
plt.xlabel('Time (s)')
plt.savefig("demo_1c.png")
plt.show()

times = [0, 0.25, 0.5, 0.75]
plt.plot(times, [0,0.5,1,1.2], 'g--', times, [1,2,3,4], 'r')
plt.ylabel('Concentration (%)')
plt.xlabel('Time (s)')
plt.title('Concentration of Chlorine vs Time')
plt.savefig("demo_1d.png")
plt.show()

import matplotlib.patches as mpatches

times = [0, 0.25, 0.5, 0.75]
plt.plot(times, [0,0.5,1,1.2], 'g--', times, [1,2,3,4], 'r')
plt.ylabel('Concentration (%)')
plt.xlabel('Time (s)')
plt.title('Concentration of Chlorine vs Time')
green_patch = mpatches.Patch(color='green', label='Some data')
red_patch = mpatches.Patch(color='red', label='Other data')
plt.legend(handles=[green_patch, red_patch], loc='upper center')
plt.savefig("demo_1e.png")
plt.show()
