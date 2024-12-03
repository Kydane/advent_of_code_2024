import math


def parse_input():
    list1: list = []
    with open("part2_input.txt", "r") as file:
        for line in file:
            split_line = line.split()
            sub_list = []
            [sub_list.append(int(x.strip())) for x in split_line]
            list1.append(sub_list)
    return list1

def is_safe(arr: list):
    assert len(arr) > 1
    # First check if increasing or decreasing
    result = arr[0] - arr[1]
    is_increasing = True if result > 0 else False
    for i in range(len(arr)):
        if len(arr) == i+1:
            continue
        diff = arr[i] - arr[i+1]
        if math.fabs(diff) > 3 or math.fabs(diff) < 1:
            return False

        if is_increasing:
            if diff < 0:
                return False
        else:
            if diff > 0:
                return False
    return True


def is_safe_iterated(sub_list):
    safe_arr = []
    for i in range(len(sub_list)):
        safe_arr.append(is_safe(sub_list[:i] + sub_list[i + 1:]))
    if safe_arr.count(True) > 0:
        return True
    else:
        print(str(safe_arr))
        return False


if __name__ == '__main__':
    list1 = parse_input()
    total_safe = 0
    for sub_list in list1:
        already_safe = is_safe(sub_list)
        if already_safe:
            total_safe += 1
            continue
        else:
            safe_with_one_removed = is_safe_iterated(sub_list)
            if safe_with_one_removed:
                total_safe += 1
        if not already_safe or safe_with_one_removed:
            print(str(sub_list))
            print()
    print(total_safe)


