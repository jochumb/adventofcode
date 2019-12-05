def part1(intcode):
    intcode[1] = 12
    intcode[2] = 2
    return runcode(intcode)[0]

def part2(intcode):
    for noun in range(100):
        for verb in range(100):
            intcode[1] = noun
            intcode[2] = verb
            if runcode(intcode)[0] == 19690720:
                return 100 * noun + verb
    return 0

def runcode(intcode, i=0):
    action = intcode[i]
    c = list(intcode)
    if action == 1:
        c[c[i+3]] = c[c[i+1]] + c[c[i+2]]
        return runcode(c, i+4)
    elif action == 2:
        c[c[i+3]] = c[c[i+1]] * c[c[i+2]]
        return runcode(c, i+4)
    elif action == 99:
        return c
    else:
        return [0]


if __name__ == "__main__":
    with open("../input/02") as f:
        intcode = [int(x) for x in f.readline().split(",")]
        print('Part 1: {}'.format(part1(list(intcode))))
        print('Part 2: {}'.format(part2(list(intcode))))