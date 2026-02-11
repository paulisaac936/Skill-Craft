import matplotlib.pyplot as plt

ages = [5, 12, 17, 22, 28, 35, 45, 52, 68]

group_0_20 = 0
group_21_40 = 0
group_41_plus = 0

for a in ages:
    if a <= 20:
        group_0_20 += 1
    elif a <= 40:
        group_21_40 += 1
    else:
        group_41_plus += 1

groups = ["0-20", "21-40", "41+"]
counts = [group_0_20, group_21_40, group_41_plus]

plt.bar(groups, counts)
plt.xlabel("Age Groups")
plt.ylabel("People Count")
plt.title("Age Group Distribution")

plt.show()