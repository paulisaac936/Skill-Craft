import matplotlib.pyplot as plt

cities = ["Chennai", "Delhi", "Mumbai", "Kolkata"]
population = [7.1, 19.0, 20.4, 14.8]

total = sum(population)

plt.bar(cities, population)
plt.xlabel("Cities")
plt.ylabel("Population (millions)")
plt.title("City-wise Population")

plt.show()