import matplotlib.pyplot as plt

ages = [12, 18, 25, 30, 45, 60, 72]
filtered_ages = []

for a in ages:
    if a >= 18:
        filtered_ages.append(a)

plt.hist(filtered_ages, bins=5)
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Adult Age Distribution")

plt.show()