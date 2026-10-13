n = 4

guess = input("Total points: ")

input("Formula: one calculation. Press Enter to run ")

input("Formula: two calculations. Press Enter to run ")
total = n * (n + 1) // 2
print("Total =", total, " steps = 1")

input("Loop: adds one student at a time. Press Enter to run ")
total = 0
for student in range(1, n + 1):
    total += student
print("Total =", total, " steps =", n)

input("Double Loop: counts every single point. Press Enter to run ")
total = 0
steps = 0
for student in range(1, n + 1):
    for point in range(1, student + 1):
        total += 1
        steps += 1
print("Total =", total, " steps =", steps, "your guess was:", guess)