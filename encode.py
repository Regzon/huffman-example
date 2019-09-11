#!/usr/bin/env python3


def huffman(items):
    while len(items) > 1:
        items = sorted(items, key=lambda x: x[0])
        first, second = items[:2]

        for symbol in first[1]:
            symbol[1] = '0' + symbol[1]

        for symbol in second[1]:
            symbol[1] = '1' + symbol[1]

        new_weight = first[0] + second[0]
        new_item = [new_weight, first[1] + second[1]]

        items = [new_item] + items[2:]

    return items[0][1]


def main():
    labels = input("Enter symbols splitted by space: ").split(' ')

    items = []
    for label in labels:
        weight = int(input("Enter the weight for '{}' symbol: ".format(label)))
        items.append([weight, [[label, '']]])

    items = huffman(items)

    for item in items:
        print(item[0], "=>", item[1])


if __name__ == '__main__':
    main()
