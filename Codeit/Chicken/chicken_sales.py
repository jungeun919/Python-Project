with open('Codeit/Chicken/chicken.txt', 'r', encoding='utf-8') as f:
    total = 0
    days = 0

    for line in f:
        line = line.strip().split(": ")
        total += int(line[1])
        days += 1
    print(total / days)