import matplotlib.pyplot as plt

categories = ["Male", "Female"]
count = [520, 480]

total = count[0] + count[1]
percentage = [(c / total) * 100 for c in count]

plt.bar(categories, percentage)
plt.xlabel("Gender")
plt.ylabel("Percentage")
plt.title("Gender Distribution (%)")

plt.show()