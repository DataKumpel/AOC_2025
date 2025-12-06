from enum import Enum, auto


class DbReadMode(Enum):
    ID_RANGES = auto()
    ID_AVAILABLE = auto()


EXAMPLE = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def read_ingredient_db(db_raw: str) -> tuple[list, list]:
    lines = db_raw.split("\n")
    mode = DbReadMode.ID_RANGES
    id_ranges = []
    available_ids = []
    
    for line in lines:
        if line == "":
            mode = DbReadMode.ID_AVAILABLE
            continue

        match mode:
            case DbReadMode.ID_RANGES:
                start, stop = [int(num) for num in line.split("-")]
                id_ranges.append(range(start, stop + 1))
            case DbReadMode.ID_AVAILABLE:
                available_ids.append(int(line))

    return id_ranges, available_ids


def count_fresh_ingredients(db_raw: str) -> int:
    id_ranges, ids_available = read_ingredient_db(db_raw)
    fresh_count = 0
    
    for id in ids_available:
        for id_range in id_ranges:
            if id in id_range:
                fresh_count += 1
                break

    return fresh_count


def collapse_id_ranges(id_ranges: list[range]) -> list[range]:
    collapsed: list[range] = []
    for id_range in id_ranges:
        for index, checked_range in enumerate(collapsed):
            # Case 1: Contained in another range:
            if id_range.start in checked_range and id_range.stop in checked_range:
                print(id_range, "contained in", checked_range)
                break

            # Case 2: Extends both limits:
            if id_range.start < checked_range.start and id_range.stop > checked_range.stop:
                collapsed[index] = id_range
                print(id_range, "extends BOTH limits of", checked_range)
                break

            # Case 3: Extends lower limit:
            if id_range.start < checked_range.start and id_range.stop in checked_range:
                collapsed[index] = range(id_range.start, checked_range.stop)
                print(id_range, "extends LOWER limit of", checked_range)
                break
            
            # Case 4: Extends upper limit:
            if id_range.stop > checked_range.stop and id_range.start in checked_range:
                collapsed[index] = range(checked_range.start, id_range.stop)
                print(id_range, "extends UPPER limit of", checked_range)
                break
            
        else:
            #print(id_range, "is a new seperate range")
            collapsed.append(id_range)

    return collapsed


def fully_collapse_id_ranges(id_ranges: list[range]) -> list[range]:
    while True:
        num_ranges = len(id_ranges)
        id_ranges = collapse_id_ranges(id_ranges)
        if num_ranges - len(id_ranges) == 0:
            break

    return id_ranges


if __name__ == "__main__":
    fresh_ex = count_fresh_ingredients(EXAMPLE)
    print(fresh_ex)
    assert fresh_ex == 3

    with open("inputs/day_05.txt") as file:
        db_raw = file.read()

    fresh_count = count_fresh_ingredients(db_raw)
    print("Fresh ingredients:", fresh_count)

    ##### Part II ##################################################################################
    id_ranges, _ = read_ingredient_db(EXAMPLE)

    id_ranges = fully_collapse_id_ranges(id_ranges)
    print(id_ranges)
    num_correct_ids = sum(len(r) for r in id_ranges)
    print(num_correct_ids)
    assert num_correct_ids == 14

    id_ranges, _ = read_ingredient_db(db_raw)
    id_ranges = fully_collapse_id_ranges(id_ranges)
    num_correct_ids = sum(len(r) for r in id_ranges)

    print("Final ID-Ranges:")
    for id_range in id_ranges:
        print("\t", id_range)
    
    print("Number of correct IDs:", num_correct_ids)
    
