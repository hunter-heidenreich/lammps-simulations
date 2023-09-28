# Hunter Heidenreich, 2023
#
# Plots the energy of a simulation over time.

import matplotlib.pyplot as plt

from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    parser.add_argument('--skip', type=int, default=1)

    args = parser.parse_args()

    ts = []
    kes = []
    pes = []
    tes = []
    Ts = []

    with open(args.input, 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue

            line = line.strip()
            if len(line) == 0:
                continue

            # TimeStep v_k v_e v_t v_T
            t, v_k, v_e, v_t, v_T = list(map(float, line.split()))
            ts.append(t)
            kes.append(v_k)
            pes.append(v_e)
            tes.append(v_t)
            Ts.append(v_T)

    # prune data
    ts = ts[args.skip:]
    kes = kes[args.skip:]
    pes = pes[args.skip:]
    tes = tes[args.skip:]
    Ts = Ts[args.skip:]

    # plot
    fig, axs = plt.subplots(2, 2, figsize=(8 * 2, 6 * 2))

    axs[0, 0].plot(ts, kes)
    axs[0, 0].set_xlabel('TimeStep')
    axs[0, 0].set_ylabel('Kinetic Energy')
    axs[0, 0].set_title('Kinetic Energy')

    axs[0, 1].plot(ts, pes)
    axs[0, 1].set_xlabel('TimeStep')
    axs[0, 1].set_ylabel('Potential Energy')
    axs[0, 1].set_title('Potential Energy')

    axs[1, 0].plot(ts, tes)
    axs[1, 0].set_xlabel('TimeStep')
    axs[1, 0].set_ylabel('Total Energy')
    axs[1, 0].set_title('Total Energy')

    axs[1, 1].plot(ts, Ts)
    axs[1, 1].set_xlabel('TimeStep')
    axs[1, 1].set_ylabel('Temperature')
    axs[1, 1].set_title('Temperature')

    plt.tight_layout()
    plt.savefig(args.output)
    plt.close()
