# NOTES CLEANER

# Topics: read(n) | readlines() | Loop Through File

# Filter Lines | Copy Odd Lines

# PART 1 -- Sneak Peek

n = int(input("How many characters to preview? "))

with open("C:\\Users\\sisod\\OneDrive\\Desktop\\Python\\Operations on a File - Part 1\\class-notes.txt", "r", encoding="utf-8") as file:

    print(file.read(n))

print()

# PART 2 -- All Lines as a List

with open("C:\\Users\\sisod\\OneDrive\\Desktop\\Python\\Operations on a File - Part 1\\class-notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("Total lines:", len(lines))

for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())

print()

# PART 3 -- Filter Lines

word = input("Skip lines starting with: ")

with open("C:\\Users\\sisod\\OneDrive\\Desktop\\Python\\Operations on a File - Part 1\\class-notes.txt", "r", encoding="utf-8") as file:

    for line in file:
        if line.startswith(word):
            print("skip ->", line.strip())
        else:
            print("keep ->", line.strip())

print()

# PART 4 -- Copy Odd Lines to New File

with open("C:\\Users\\sisod\\OneDrive\\Desktop\\Python\\Operations on a File - Part 1\\class-notes.txt", "r", encoding="utf-8") as file:

    lines = file.readlines()

with open("C:\\Users\\sisod\\OneDrive\\Desktop\\Python\\Operations on a File - Part 1\\odd-lines.txt", "w", encoding="utf-8") as out:

    for i in range(0, len(lines), 2):

        out.write(lines[i])

print("Odd lines saved to odd-lines.txt")