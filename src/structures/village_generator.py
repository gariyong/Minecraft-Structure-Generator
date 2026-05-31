def generate_house(x, y, z):

    blocks = []

    width = 5
    length = 5
    height = 4

    for dx in range(width):

        for dz in range(length):

            for dy in range(height):

                blocks.append(
                    (
                        x + dx,
                        y + dy,
                        z + dz,
                        "oak_planks"
                    )
                )

    return blocks

def generate_plaza(x, y, z):

    blocks = []

    radius = 4

    for dx in range(-radius, radius + 1):

        for dz in range(-radius, radius + 1):

            blocks.append(
                (
                    x + dx,
                    y,
                    z + dz,
                    "cobblestone"
                )
            )

    return blocks

def generate_village(layout):

    village_blocks = []

    for house_x, house_z in layout["houses"]:

        village_blocks.extend(
            generate_house(
                house_x,
                0,
                house_z
            )
        )

    plaza_x, plaza_z = layout["plaza"]

    village_blocks.extend(
        generate_plaza(
            plaza_x,
            0,
            plaza_z
        )
    )

    return village_blocks

if __name__ == "__main__":

    from src.generation.blueprint_generator import generate_blueprint
    from src.generation.layout_generator import generate_village_layout

    blueprint = generate_blueprint(
        "village"
    )

    layout = generate_village_layout(
        blueprint
    )

    village_blocks = generate_village(
        layout
    )

    print()

    print("Village 총 블록 수")

    print(
        len(village_blocks)
    )