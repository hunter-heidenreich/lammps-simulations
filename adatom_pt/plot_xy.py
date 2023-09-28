# Hunter Heidenreich, 2023
#
# Plots the coordinates of the adatom.

import matplotlib.pyplot as plt

from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    parser.add_argument('--id', type=int, default=1665)
    parser.add_argument('--do_z', action='store_true')
    args = parser.parse_args()

    xs = []
    ys = []
    zs = []
    with open(args.input, 'r') as f:
        for line in f:
            if line.startswith(f'{args.id} '):
                x, y, z = line.split()[2:5]
                x, y, z = float(x), float(y), float(z)
                xs.append(x)
                ys.append(y)
                zs.append(z)

    if args.do_z:
        plt.plot(list(range(len(zs))), zs)
        plt.xlabel('step')
        plt.ylabel('z')
        plt.title(f'z vs. step for adatom {args.id}')
    else:
        plt.scatter(xs, ys, s=1)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'xy coordinates for adatom {args.id}')
    plt.savefig(args.output)

