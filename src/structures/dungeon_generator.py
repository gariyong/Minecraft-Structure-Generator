# ==================================================
# Dungeon Room Generator
# ==================================================

def generate_room(x, y, z):

    blocks = []

    width = 7
    length = 7
    height = 4

    for dx in range(width):

        for dz in range(length):

            for dy in range(height):

                blocks.append(
                    (
                        x + dx,
                        y + dy,
                        z + dz,
                        "deepslate_bricks"
                    )
                )

    return blocks

# ==================================================
# Corridor Generator
# ==================================================

def generate_corridor(
        x1, z1,
        x2, z2
):

    blocks = []

    width = 3

    # 세로 복도
    if x1 == x2:

        for z in range(
            min(z1, z2),
            max(z1, z2) + 1
        ):

            for dx in range(
                -(width // 2),
                width // 2 + 1
            ):

                blocks.append(
                    (
                        x1 + dx,
                        0,
                        z,
                        "cobbled_deepslate"
                    )
                )

    return blocks

# ==================================================
# Dungeon Generator
# ==================================================

def generate_dungeon(layout):

    dungeon_blocks = []

    rooms = layout["rooms"]

    # ------------------------
    # Room 생성
    # ------------------------

    for room_x, room_z in rooms:

        dungeon_blocks.extend(
            generate_room(
                room_x,
                0,
                room_z
            )
        )

    # ------------------------
    # Corridor 생성
    # ------------------------

    dungeon_blocks.extend(
        generate_corridor(
            23,
            20,
            23,
            35
        )
    )

    return dungeon_blocks

if __name__ == "__main__":

    from src.generation.blueprint_generator import generate_blueprint
    from src.generation.layout_generator import generate_dungeon_layout

    blueprint = generate_blueprint(
        "dungeon"
    )

    layout = generate_dungeon_layout(
        blueprint
    )

    dungeon_blocks = generate_dungeon(
        layout
    )

    print()

    print("Dungeon 총 블록 수")

    print(
        len(dungeon_blocks)
    )