import argparse

import baby_name_generator

QUIT = 'q'


def main():
    parser = _cliparser()
    args = parser.parse_args()

    bng = baby_name_generator.BabyNameGenerator(args.use_weights)
    bng.loadFirsts(args.first)
    bng.loadMiddles(args.middle)
    bng.loadLasts(args.last)

    while not input() == QUIT:
        bng.generateName()


def _cliparser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-f',
        '--first',
        required=True,
        help='File for first names OR the first name to use.',
    )
    parser.add_argument(
        '-l',
        '--last',
        required=True,
        help='File for last names OR the last name to use.',
    )
    parser.add_argument(
        '-m',
        '--middle',
        required=True,
        help='File for middle names OR the middle name to use.',
    )
    parser.add_argument(
        '-u',
        '--use_weights',
        action='store_true',
        default=False,
        help='Whether to use weights associated with inputs or use names uniformly.',
    )

    return parser


if __name__ == '__main__':
    main()