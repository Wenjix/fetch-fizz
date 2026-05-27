#!/usr/bin/env python3
"""Run the fetch-fizz team_demo blueprint."""

from dimos import Dimos

from blueprints.team_demo import team_demo


def main() -> None:
    Dimos(n_workers=10).run(team_demo)


if __name__ == "__main__":
    main()
