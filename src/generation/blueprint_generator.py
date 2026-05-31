import random


def generate_blueprint(building_type):

    if building_type == "castle":

        return {
            "type": "castle",
            "size": "large",
            "tower_count": random.choice(
                [2, 4, 6]
            ),
            "wall": True,
            "gate": True
        }

    elif building_type == "village":

        return {
            "type": "village",
            "house_count": random.randint(
                8,
                20
            ),
            "square": True
        }

    elif building_type == "dungeon":

        return {
            "type": "dungeon",
            "floors": random.randint(
                1,
                5
            ),
            "ruins": True
        }

    return None

if __name__ == "__main__":
    print(
    generate_blueprint(
        "castle"
    )
)