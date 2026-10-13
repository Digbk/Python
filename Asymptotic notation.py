n = 10

guess = input("Double Loop at n = 10 checks n × n pairs. How many? ")

input("Formula: one calculation, done. Press Enter to run ")
steps = 1
print(" steps =", steps, " -> O(1) constant time -> steps never change")

input("Loop: one step per item. Press Enter to run")
steps = 0
for i in range(n):
  steps += 1
print( " steps =", steps, " -> O(n) linear time")

input("Double Loop: checks every pair. Press Enter to run")
steps = 0
for i in range(n):
  for j in range(n):
    steps += 1
print( " steps =", steps, " your guess:", guess, " -> O(n^2) quadratic time")

input("Two more notation. Press enter")
print("Big Omega -> best case lower bound")
print("Big Theta -> average case")