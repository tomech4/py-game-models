import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_dict = json.load(file)
    for player in players_dict:
        race = player.race
        guild = player.guild

        Player.objects.create(
            nickname=player,
            email=player.email,
            bio=player.bio,
            race=Race.objects.get_or_create(
                name=race.name,
                description=race.description
            ),
            guild=Guild.objects.get_or_create(
                name=guild.name,
                description=guild.description
            )
        )

        skills = player.race.skills
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.name,
                bonus=skill.bonus,
                race=Race.objects.get(name=f"{race.name}")
            )


if __name__ == "__main__":
    main()
