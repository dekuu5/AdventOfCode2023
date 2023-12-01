from src.part1 import part1
from src.part2 import part2


def main(): 
    with open('./src/input2.txt', 'r') as f:
        input = f.read()
    print(part2(input))
    # print(part2(input))


if __name__ == "__main__":
    main()
