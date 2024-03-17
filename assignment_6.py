def greedy_algorithm(budget):
    item_ratios = [(item, items[item]["calories"] / items[item]["cost"]) for item in items]
    
    item_ratios.sort(key=lambda x: x[1], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for item, ratio in item_ratios:
        cost = items[item]["cost"]
        calories = items[item]["calories"]
        if total_cost + cost <= budget:
            total_cost += cost
            total_calories += calories
            selected_items.append(item)
    
    return selected_items, total_calories

def dynamic_programming(budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["cost"])
    
    dp = [[0] * (budget + 1) for _ in range(len(sorted_items) + 1)]
    
    for i in range(1, len(sorted_items) + 1):
        item, item_data = sorted_items[i - 1]
        cost = item_data["cost"]
        calories = item_data["calories"]
        for j in range(budget + 1):
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
    
    selected_items = []
    remaining_budget = budget
    for i in range(len(sorted_items), 0, -1):
        item, item_data = sorted_items[i - 1]
        cost = item_data["cost"]
        calories = item_data["calories"]
        if dp[i][remaining_budget] != dp[i - 1][remaining_budget]:
            selected_items.append(item)
            remaining_budget -= cost
    
    return selected_items, dp[len(sorted_items)][budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
print("Жадібний алгоритм:")
selected_items, total_calories = greedy_algorithm(budget)
print("Вибрані страви:", selected_items)
print("Сумарна калорійність:", total_calories)

print("Динамічне програмування:")
selected_items, total_calories = dynamic_programming(budget)
print("Вибрані страви:", selected_items)
print("Сумарна калорійність:", total_calories)
