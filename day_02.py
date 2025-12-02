import sys

EXAMPLE = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def get_id_ranges_from_str(id_ranges_raw: str) -> list[str]:
    return id_ranges_raw.split(",")

def extract_id_bounds_from_range(id_range: str) -> tuple[int, int]:
    bounds = id_range.split("-")
    lower_bound = int(bounds[0])
    upper_bound = int(bounds[1])
    return lower_bound, upper_bound

def get_invalid_ids_in_range(lower_bound: int, 
                             upper_bound: int,
                             advanced=False) -> list[int]:
    invalid_ids = []
    id_range_str = f"{lower_bound}-{upper_bound}"
    
    for id in range(lower_bound, upper_bound + 1):
        perc = (id - lower_bound) / (upper_bound - lower_bound)
        print(f"Scanning IDs [{id_range_str:^30}]{"(ADVANCED)" if advanced else ""}{perc:.>50.2%}", end="\r")
        
        id_str = str(id)
        if not advanced:
            if len(str(id)) % 2 == 1:
                # Skip ids with an uneven number of digits...
                continue            
            
            id_front = int(id_str[:len(id_str)//2])
            id_back = int(id_str[len(id_str)//2:])

            if id_front == id_back:
                invalid_ids.append(id)
        else:
           for length in range(1, len(id_str) // 2 + 1):
               if len(id_str) % length != 0:
                   continue
               
               if id in invalid_ids:
                   break
               
               rep_times = len(id_str) // length
               if id_str[:length] * rep_times == id_str:
                   invalid_ids.append(id) 

    # Clear line:
    print(" " * 120, end="\r")
    print(f"Scanning IDs [{id_range_str:^30}] ...done!")
    #print(f"[DEBUG] Found IDS: {invalid_ids}")

    return invalid_ids

def calc_invalid_ids_checksum(id_ranges_str: str, advanced=False) -> int:
    invalid_ids = []
    id_ranges = get_id_ranges_from_str(id_ranges_str)
    for id_range in id_ranges:
        bounds = extract_id_bounds_from_range(id_range)
        invalid_ids.extend(get_invalid_ids_in_range(*bounds, advanced))
    chcksum = sum(invalid_ids)
    print(f"CHECKSUM: {chcksum}")
    return chcksum

if __name__ == "__main__":
    advanced = "-a" in sys.argv
        
    check = calc_invalid_ids_checksum(EXAMPLE, advanced)

    if advanced:
        assert check == 4174379265

    with open("inputs/day_02.txt") as file:
        calc_invalid_ids_checksum(file.read(), advanced)
