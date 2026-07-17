#! /usr/bin/env python3
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(
    mages: list[dict[str, Any]],
    min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda x: x['power'] > min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    max_power = max(mages, key=lambda x: x['power'])
    min_power = min(mages, key=lambda x: x['power'])
    avg_power = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)

    return {
        'max_power': max_power['power'],
        'min_power': min_power['power'],
        'avg_power': avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Water Chalice", "power": 80, "type": "weapon"},
        {"name": "Water Chalice", "power": 87, "type": "weapon"},
        {"name": "Fire Staff", "power": 115, "type": "weapon"},
        {"name": "Crystal Orb", "power": 120, "type": "weapon"},
    ]
    spells = ['meteor', 'fireball', 'tornado', 'freeze']
    mages = [
        {"name": "Phoenix", "power": 89, "element": "fire"},
        {"name": "Alex", "power": 92, "element": "shadow"},
        {"name": "Ember", "power": 65, "element": "lightning"},
        {"name": "Ember", "power": 69, "element": "water"},
        {"name": "Jordan", "power": 76, "element": "light"},
    ]
    sorted_artifact = artifact_sorter(artifacts)
    for i, artifact in enumerate(sorted_artifact[:-1]):
        next_artifact = sorted_artifact[i + 1]
        print(f"{artifact['name']} ({artifact['power']}) comes before "
              f"{next_artifact['name']} ({next_artifact['power']})")
    print()
    power_filtered = power_filter(mages, 70)
    for element in power_filtered:
        print(element)
    print()
    spell_transformed = spell_transformer(spells)
    for spell in spell_transformed:
        print(spell, end=" ")
    print()
    print(mage_stats(mages))
