def part1(wires):
    paths = [path(wire) for wire in wires]
    intersections = list(set(paths[0]) & set(paths[1]))
    manhattans = [abs(i[0]) + abs(i[1]) for i in intersections]
    return min(manhattans)

def part2(wires):
    paths = [path(wire) for wire in wires]
    intersections = list(set(paths[0]) & set(paths[1]))
    steps = [sum(path.index(i) + 1 for path in paths) for i in intersections]
    return min(steps)

def path(wire):
    return calc_path(wire, (0,0), [])

def calc_path(wire, cur, path):
    if len(wire) == 0:
        return path
    res = section(cur, wire[0])
    return calc_path(wire[1:], res[-1], path + res)
    
def section(cur, direction):
    if direction[0] == "R":
        return [(cur[0] + n, cur[1]) for n in range(1, direction[1]+1)]
    elif direction[0] == "L":
        return [(cur[0] - n, cur[1]) for n in range(1, direction[1]+1)]
    elif direction[0] == "U":
        return [(cur[0], cur[1] + n) for n in range(1, direction[1]+1)]
    elif direction[0] == "D":
        return [(cur[0], cur[1] - n) for n in range(1, direction[1]+1)]

def intersections(wire1, wire2):
    distances = {}
    for intersection in list(set(wire1) & set(wire2)):
        distances[abs(intersection[0]) + abs(intersection[1])] = intersection
    return distances

def parse_directions(wire):
    return [parse_direction(direction) for direction in wire.split(",")]

def parse_direction(direction):
    return direction[0], int(direction[1:])

if __name__ == "__main__":
    with open("../input/03") as f:
        wires = [parse_directions(line) for line in f.readlines()]
        print('Part 1: {}'.format(part1(list(wires))))
        print('Part 2: {}'.format(part2(list(wires))))