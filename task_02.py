import random

def get_numbers_ticket(*, min: int, max: int, quantity: int) -> list:
    if max - min + 1 < quantity:
        raise ValueError("Unable to obtain a sufficient number of unique values within the specified range.")
    unique_numbers = random.sample(range(min, max + 1), quantity)
    sorted_list = sorted(unique_numbers)
    return sorted_list

lottery_numbers = get_numbers_ticket(min=1, max=49, quantity=6)
print(f"Ваші лотерейні числа:", lottery_numbers)