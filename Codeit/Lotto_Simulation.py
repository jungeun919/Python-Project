from random import randint


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers

def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

# def count_matching_numbers(numbers, winning_numbers):
#     count = 0
#     for n in numbers:
#         if n in winning_numbers:
#             count += 1
#     return count

def count_matching_numbers(numbers, winning_numbers):
    match_numbers = list(set(numbers).intersection(winning_numbers))
    return len(match_numbers)

def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus = count_matching_numbers(numbers, winning_numbers[6:])

    print("보너스 제외 맞춘 개수          ", count)
    print("보너스 맞춘 개수               ", bonus)
    
    if count == 6:
        return 1000000000
    elif count == 5 and bonus == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0


print("[Test]")
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35])) # 3
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6])) # 5000
print()

user_numbers = generate_numbers(6)
winning_numbers = draw_winning_numbers()

print("[Lotto]")
print("랜덤 로또 번호 생성            ", user_numbers)
print("로또 당첨번호 + 보너스 번호    ", winning_numbers)
print("겹치는 번호 개수               ", count_matching_numbers(user_numbers, winning_numbers))
print("당첨금액                       ", check(user_numbers, winning_numbers))