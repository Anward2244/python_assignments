import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [10, 14, 12, 18, 20]

# plt.plot(x,y)

# x_scatter = [2, 4, 6, 8, 10]
# y_scatter = [5, 15, 8, 20, 14]
# plt.bar(x_scatter, y_scatter)

# plt.show()


import matplotlib.pyplot as plt

# Population percentage Pie Chart
countries = ["India", "China", "USA", "Indonesia", "Pakistan", "Others"]

shares = [17.78, 17.20, 4.22, 3.47, 3.10, 54.23]

plt.tight_layout()
plt.pie(shares, labels=countries, autopct='%1.1f%%')
plt.title("Population Percentage")
plt.axis('equal')
plt.show()