import random

num_simulations = 1000000

sum_counts = {
    2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0
}

for _ in range(num_simulations):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    total = dice1 + dice2
    
    sum_counts[total] += 1

probabilities = {}
for total, count in sum_counts.items():
    probability = count / num_simulations
    probabilities[total] = probability

print("Сума | Імовірність")
for total in sorted(probabilities.keys()):
    print(f"{total}\t{probabilities[total]:.2%}")
