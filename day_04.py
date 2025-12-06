

EXAMPLE = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


Grid = list[list[str]]


def map_to_grid(input_map: str) -> Grid:
    rows = input_map.split()
    return [list(row) for row in rows]


def check_neighbors(pos_x: int, pos_y: int, grid: Grid) -> bool:
    size_y = len(grid) - 1
    size_x = len(grid[0]) - 1

    upper_row = grid[pos_y - 1] if pos_y > 0 else None
    same_row = grid[pos_y]
    lower_row = grid[pos_y + 1] if pos_y < size_y else None

    neighbors = []

    if upper_row:
        upper_left = upper_row[pos_x - 1] if pos_x > 0 else ""
        upper_middle = upper_row[pos_x]
        upper_right = upper_row[pos_x + 1] if pos_x < size_x else ""
        neighbors.extend([upper_left, upper_middle, upper_right])

    left = same_row[pos_x - 1] if pos_x > 0 else ""
    right = same_row[pos_x + 1] if pos_x < size_x else ""
    neighbors.extend([left, right])

    if lower_row:
        lower_left = lower_row[pos_x - 1] if pos_x > 0 else ""
        lower_middle = lower_row[pos_x]
        lower_right = lower_row[pos_x + 1] if pos_x < size_x else ""
        neighbors.extend([lower_left, lower_middle, lower_right])

    return neighbors.count("@") < 4


def count_accessible_paper_rolls(grid: Grid):
    count = 0
    positions = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != "@":
                continue
            
            if check_neighbors(x, y, grid):
                count += 1
                positions.append((x, y))

    return count, positions


def mark_positions_on_grid(positions, grid):
    for pos in positions:
        grid[pos[1]][pos[0]] = "x"


def print_grid(grid):
    grid_str = "\n".join(["".join(row) for row in grid])
    print(grid_str)


if __name__ == "__main__":
    example_grid = map_to_grid(EXAMPLE)
    accessible_paper_rolls, positions = count_accessible_paper_rolls(example_grid)
    mark_positions_on_grid(positions, example_grid)
    print_grid(example_grid)
    print(accessible_paper_rolls)
    
    assert accessible_paper_rolls == 13

    with open("inputs/day_04.txt") as file:
        map_data = file.read()

    grid = map_to_grid(map_data)
    accessible_paper_rolls, positions = count_accessible_paper_rolls(grid)
    print("Accessible paper rolls:", accessible_paper_rolls)

