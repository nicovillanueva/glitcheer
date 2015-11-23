#!/usr/bin/env python3

def screw_image(fpath, rounds, output):
    import random
    bound_a = 20
    bound_b = 20
    with open(fpath, 'rb') as f:
        c = list(f.read())
    for _ in range(rounds):
        c[random.randint(bound_a, len(c) - bound_b)] = c[random.randint(bound_a, len(c) - bound_b)]
    with open(output, 'wb') as f:
        f.write(bytes(c))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('image', type=str)
    parser.add_argument('rounds', type=int)
    parser.add_argument('--output', type=str, default='fucked.jpg')
    args = parser.parse_args()
    screw_image(args.image, args.rounds, args.output)
