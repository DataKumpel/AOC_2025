from itertools import combinations


EXAMPLE = """987654321111111
811111111111119
234234234234278
818181911112111"""


def get_largest_joltage_in_bank(bank: str, num_batteries: int) -> int:
    max_joltage = 0
    # old implementation:
    #for i in range(len(bank)):
    #    for j in range(i + 1, len(bank)):
    #        number = int(f"{bank[i]}{bank[j]}")
    #        if number > max_joltage:
    #            max_joltage = number

    for combi in combinations(bank, num_batteries):
        joltage = int("".join(combi))
        if joltage > max_joltage:
            max_joltage = joltage
    
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
