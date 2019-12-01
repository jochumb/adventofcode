import math

def part1(masses):
    return sum(fuel_for_mass(x) for x in masses)

def part2(masses):
    return sum(recursive_fuel_for_mass(x) for x in masses)

def fuel_for_mass(mass):
    return math.floor(mass/3) - 2    

def recursive_fuel_for_mass(mass, acc=0):
    next = fuel_for_mass(mass)
    return acc if next <= 0 else recursive_fuel_for_mass(next, acc+next)


if __name__ == "__main__":
    with open("../input/01") as f:
        masses = [int(x) for x in f.readlines()]
        print('Part 1: {}'.format(part1(masses)))
        print('Part 2: {}'.format(part2(masses)))