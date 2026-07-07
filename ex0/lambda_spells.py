#! /usr/bin/env python3
def artifact_sorter(artifacts: list[dict[str, any]]) -> list[dict[str, any]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(
            mages: list[dict[str, any]],
            min_power: int) -> list[dict[str, any]]:
    return list(filter(lambda x: x['power'] > min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict[str, any]]) -> dict[str, any]:
    max_power = max(mages, key=lambda x: x['power'])
    min_power = min(mages, key=lambda x: x['power'])
    avg_power = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)

    return {
        'max_power': max_power['power'],
        'min_power': min_power['power'],
        'avg_power': avg_power
    }


