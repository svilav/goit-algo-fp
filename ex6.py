items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    current_budget = budget
    selected_items = []

    for item, details in sorted_items:
        if details['cost'] <= current_budget:
            selected_items.append(item)
            total_calories += details['calories']
            current_budget -= details['cost']

    return selected_items, total_calories

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)

    for item, details in items.items():
        cost = details['cost']
        calories = details['calories']
        for b in range(budget, cost - 1, -1):
            dp[b] = max(dp[b], dp[b - cost] + calories)

    return dp[budget]

# Приклад використання
budget = 100
print("Greedy Algorithm Result:", greedy_algorithm(items, budget))
print("Dynamic Programming Result:", dynamic_programming(items, budget))
