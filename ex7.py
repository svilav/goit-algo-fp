import random
import matplotlib.pyplot as plt

# Кількість симуляцій
num_simulations = 1000000

# Ініціалізація словника для підрахунку частоти кожної суми
sum_counts = {i: 0 for i in range(2, 13)}

# Симуляція кидків кубиків
for _ in range(num_simulations):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice_sum = die1 + die2
    sum_counts[dice_sum] += 1

# Обчислення ймовірностей
sum_probabilities = {k: (v / num_simulations) * 100 for k, v in sum_counts.items()}

# Виведення результатів у вигляді таблиці
print("Сума\tІмовірність")
for sum_, prob in sum_probabilities.items():
    print(f"{sum_}\t{prob:.2f}%")

# Побудова графіку
sums = list(sum_probabilities.keys())
probs = list(sum_probabilities.values())

plt.bar(sums, probs, tick_label=sums)
plt.xlabel('Сума')
plt.ylabel('Імовірність (%)')
plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
plt.show()
