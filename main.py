import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_dict = json.load(file)
    for name, obj in players_dict.items():
        race = obj["race"]
        Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        if obj["guild"]:
            guild = obj["guild"]
            Guild.objects.get_or_create(
                name=guild["name"],
                description=(guild["description"] if guild["description"] else None)
            )

        Player.objects.create(
            nickname=name,
            email=obj["email"],
            bio=obj["bio"],
            race=Race.objects.get(name=race["name"]),
            guild=Guild.objects.get(name=guild["name"])
        )

        skills = obj["race"]["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=f"{race["name"]}")
            )


if __name__ == "__main__":
    main()
