import math

# list1 = [3, 4, 2, 1, 3, 3]
# list2 = [4, 3, 5, 3, 9, 3]

def get_distance(num1: int, num2: int):
    return math.fabs(num1 - num2)

def get_occurrence(arr: list, num1: int):
    return arr.count(num1)

def parse_input():
    list1: list = []
    list2: list = []
    with open("part2_input.txt", "r") as file:
        for line in file:
            split_line = line.split()
            list1.append(int(split_line[0].strip()))
            list2.append(int(split_line[1].strip()))
    return list1, list2


if __name__ == '__main__':
    distance : int = 0

    list1, list2 = parse_input()

    #Confirm that the lists are the same length
    assert len(list1) == len(list2)

    # Save the length
    total_length = len(list1)

    for i in range(total_length):
        distance = distance+ (list1[i] * get_occurrence(list2, list1[i]))

    print(distance)
