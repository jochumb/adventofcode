input = "172930-683082"

def part1(range):
    range_list = list(range)
    filtered_increasing = list(filter(is_increasing, range_list))
    filtered_double = list(filter(has_double, filtered_increasing))
    return len(filtered_double)

def part2(range):
    range_list = list(range)
    filtered_increasing = list(filter(is_increasing, range_list))
    filtered_double = list(filter(has_exactly_two, filtered_increasing))
    return len(filtered_double)

def has_double(number):
    return len(set(int(x) for x in str(number))) < 6

def is_increasing(number):
    digits = [int(x) for x in str(number)]
    sorted = list(digits)
    sorted.sort()
    return digits == sorted

def has_exactly_two(number):
    digits = [int(x) for x in str(number)]
    return [digits.count(x) for x in digits].count(2) > 0

if __name__ == "__main__":
    split = list(map(lambda x: int(x), input.split("-")))
    range = range(split[0], split[1]+1)
    print('Part 1: {}'.format(part1(range)))
    print('Part 2: {}'.format(part2(range)))