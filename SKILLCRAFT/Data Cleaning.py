import matplotlib.pyplot as plt

marks = [78, 85, -1, 92, 0, 88, -5]
cleaned_marks = []

for m in marks:
    if m > 0:
        cleaned_marks.append(m)

plt.hist(cleaned_marks, bins=5)
plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Marks Distribution")

plt.show()