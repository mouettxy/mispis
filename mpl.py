import matplotlib.pyplot as plt

plt.plot(range(1, 20), [i * i for i in range(1, 20)], 'ro')
plt.savefig('example.png')
plt.show()