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


if __name__ == "__main__":
    fresh_ex = count_fresh_ingredients(EXAMPLE)
    print(fresh_ex)
    assert fresh_ex == 3
    
