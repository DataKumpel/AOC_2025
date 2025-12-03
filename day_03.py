import numpy as np

EXAMPLE = """987654321111111
811111111111119
234234234234278
818181911112111"""


def get_largest_joltage_in_bank(bank: str, num_batteries: int) -> int:
    max_joltage = 0
    bank = [int(n) for n in bank]

    indices = []
    for i in range(num_batteries):
        start = (indices[-1] + 1) if indices else 0
        end = (i - num_batteries + 1) or None
        indices.append(np.argmax(bank[start:end]) + start)

    max_joltage = sum(10 ** pos * int(bank[index]) for pos, index in enumerate(reversed(indices)))
    
    print(f"BANK: {bank} => MAX {max_joltage:>2} joltage")
    return max_joltage

def get_maximum_joltage(banks: list[str], num_batteries=2) -> int:
    return sum(get_largest_joltage_in_bank(bank, num_batteries) for bank in banks)

if __name__ == "__main__":
    max_joltage = get_maximum_joltage(EXAMPLE.split())
    print(f"MAX JOLTAGE: {max_joltage} joltage")
    assert max_joltage == 357

    with open("inputs/day_03.txt") as file:
        banks = file.read().split()

    max_joltage = get_maximum_joltage(banks)
    print(f"MAX JOLTAGE: {max_joltage} joltage")

    # Part II: now 12 batteries!
    max_joltage = get_maximum_joltage(EXAMPLE.split(), 12)
    print(f"MAX JOLTAGE: {max_joltage} joltage")
    assert max_joltage == 3121910778619

    max_joltage = get_maximum_joltage(banks, 12)
    print(f"MAX JOLTAGE: {max_joltage} joltage")
