#! /usr/bin/env python3
def artifact_sorter(artifacts: list[dict[str, any]]) -> list[dict[str, any]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(
            mages: list[dict[str, any]],
            min_power: int) -> list[dict[str, any]]:
    return list(filter(lambda x: x['power'] > min_power, mages))


