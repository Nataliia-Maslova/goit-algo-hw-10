import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Змінні
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Обмеження
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
model += 1 * lemonade <= 50, "Sugar"
model += 1 * lemonade <= 30, "Lemon_Juice"
model += 2 * fruit_juice <= 40, "Fruit_Puree"

# Мета: збільшити загальну кількість продуктів
model += lemonade + fruit_juice, "Total_Production"

# Вирішення задачі
model.solve()

# Виведення результатів
print("Кількість виробленого Лимонаду:", lemonade.varValue)
print("Кількість виробленого Фруктового соку:", fruit_juice.varValue)
