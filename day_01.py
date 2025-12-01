

DIAL_START = 50
MIN_NUMBER = 0
MAX_NUMBER = 99
ZERO_CLICKS = 0
EXAMPLE="""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def turn_left(start: int, amount: int) -> int:
    global ZERO_CLICKS
    while amount > 0:
        amount -= 1
        start -= 1

        if start == 0:
            ZERO_CLICKS += 1
        
        if start < 0:
            start = MAX_NUMBER

    return start


def turn_right(start: int, amount: int) -> int:
    global ZERO_CLICKS
    while amount > 0:
        amount -= 1
        start += 1
        
        if start > MAX_NUMBER:
            start = MIN_NUMBER
            ZERO_CLICKS += 1

    return start


def turn(start: int, command: str) -> int:
    if command.startswith("L"):
        return turn_left(start, int(command.strip("L")))
    if command.startswith("R"):
        return turn_right(start, int(command.strip("R")))
    raise TypeError(f"Unknown command: {command!r}")


def process_commands(commands: list[str]):
    start = DIAL_START
    zero_counts = 0
    for command in commands:
        start = turn(start, command)
        if start == 0:
            zero_counts += 1
        print(f"The dial is rotated {command!r} to point at {start}.")

    print(f"The password is: {zero_counts}")


if __name__ == "__main__":
    process_commands(EXAMPLE.split())
    print(f"Password (0x434C49434B): {ZERO_CLICKS}")
    #exit()

    with open("inputs/day_01_p1.txt") as file:
        commands = file.read().split()

    # Reset ZERO_CLICKS:
    ZERO_CLICKS = 0
    process_commands(commands)
    print(f"Password (0x434C49434B): {ZERO_CLICKS}")
