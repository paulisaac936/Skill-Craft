import matplotlib.pyplot as plt

years = [2018, 2019, 2020, 2021, 2022]
sales = [200, 240, 230, 260, 300]

plt.plot(years, sales)
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Yearly Sales Trend")

plt.show()