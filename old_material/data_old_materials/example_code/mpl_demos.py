# matplotlib all tests
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()

plt.plot([0,0.5,1,1.2])
plt.plot([1,2,3,4])
plt.show()

times = [0, 0.25, 0.5, 0.75]
plt.plot(times, [0,0.5,1,1.2], 'g--', times, [1,2,3,4], 'r')
plt.ylabel('Concentration (%)')
plt.xlabel('Time (s)')
plt.show()

times = [0, 0.25, 0.5, 0.75]
plt.plot(times, [0,0.5,1,1.2], 'g--', times, [1,2,3,4], 'r')
plt.ylabel('Concentration (%)')
plt.xlabel('Time (s)')
plt.title('Concentration of Chlorine vs Time')
plt.show()