# ==================================================
# 구조물 설정값
# ==================================================

TOWER_RADIUS = 3
TOWER_HEIGHT = 10

KEEP_SIZE = 10
KEEP_HEIGHT = 15

WALL_HEIGHT = 5


# ==================================================
# Tower Generator
# ==================================================

def generate_tower(x, y, z, height):

    blocks = []

    radius = TOWER_RADIUS

    for dy in range(height):

        for dx in range(-radius, radius + 1):

            for dz in range(-radius, radius + 1):

                # 원 내부 판정
                if dx * dx + dz * dz <= radius * radius:

                    blocks.append(
                        (
                            x + dx,
                            y + dy,
                            z + dz,
                            "stone_bricks"
                        )
                    )

    return blocks


# ==================================================
# Keep Generator
# ==================================================

def generate_keep(x, y, z, keep_size, keep_height):

    blocks = []

    for dx in range(keep_size):

        for dz in range(keep_size):

            for dy in range(keep_height):

                blocks.append(
                    (
                        x + dx,
                        y + dy,
                        z + dz,
                        "stone_bricks"
                    )
                )

    return blocks


# ==================================================
# Wall Generator
# ==================================================

def generate_wall(
        x1, z1,
        x2, z2,
        wall_height
):

    blocks = []

    # 가로 벽
    if z1 == z2:

        for x in range(
                min(x1, x2),
                max(x1, x2) + 1
        ):

            for y in range(wall_height):

                blocks.append(
                    (
                        x,
                        y,
                        z1,
                        "stone_bricks"
                    )
                )

    # 세로 벽
    elif x1 == x2:

        for z in range(
                min(z1, z2),
                max(z1, z2) + 1
        ):

            for y in range(wall_height):

                blocks.append(
                    (
                        x1,
                        y,
                        z,
                        "stone_bricks"
                    )
                )

    return blocks


# ==================================================
# Castle Generator
# ==================================================

def generate_castle(layout):

    castle_blocks = []

    size = layout["size"]
    tower_height = layout["tower_height"]
    wall_height = layout["wall_height"]
    keep_size = layout["keep_size"]
    keep_height = layout["keep_height"]

    # ------------------------
    # Tower 생성
    # ------------------------

    for tower_x, tower_z in layout["towers"]:

        tower_blocks = generate_tower(
            tower_x,
            0,
            tower_z,
            layout["tower_height"]
        )

        castle_blocks.extend(
            tower_blocks
        )

    # ------------------------
    # Wall 생성
    # ------------------------

    castle_blocks.extend(
        generate_wall(
            TOWER_RADIUS,
            TOWER_RADIUS,
            size - TOWER_RADIUS,
            TOWER_RADIUS,
            wall_height
        )
    )

    castle_blocks.extend(
        generate_wall(
            size - TOWER_RADIUS,
            TOWER_RADIUS,
            size - TOWER_RADIUS,
            size - TOWER_RADIUS,
            wall_height
        )
    )

    castle_blocks.extend(
        generate_wall(
            size - TOWER_RADIUS,
            size - TOWER_RADIUS,
            TOWER_RADIUS,
            size - TOWER_RADIUS,
            wall_height
        )
    )

    castle_blocks.extend(
        generate_wall(
            TOWER_RADIUS,
            size - TOWER_RADIUS,
            TOWER_RADIUS,
            TOWER_RADIUS,
            wall_height
        )
    )

    # Gate 생성
    gate_x, gate_z = layout["gate"]

    gate_width = 5

    castle_blocks = [

        block

        for block in castle_blocks

        if not (

            block[2] == gate_z
            and
            gate_x - gate_width // 2
            <= block[0]
            <= gate_x + gate_width // 2
            and
            block[1] < wall_height

        )

    ]

    # ------------------------
    # Keep 생성
    # ------------------------

    keep_x, keep_z = layout["keep"]

    keep_blocks = generate_keep(
        keep_x - keep_size // 2,
        0,
        keep_z - keep_size // 2,
        keep_size,
        keep_height
    )

    castle_blocks.extend(
        keep_blocks
    )

    return castle_blocks


# ==================================================
# Tower 단면 시각화
# ==================================================

def visualize_tower_slice():

    radius = TOWER_RADIUS

    for z in range(-radius, radius + 1):

        row = ""

        for x in range(-radius, radius + 1):

            if x * x + z * z <= radius * radius:

                row += "#"

            else:

                row += " "

        print(row)


# ==================================================
# 테스트 코드
# ==================================================

if __name__ == "__main__":

    from src.generation.blueprint_generator import generate_blueprint
    from src.generation.layout_generator import generate_castle_layout

    print()
    print("Castle 생성 테스트")

    blueprint = generate_blueprint(
        "castle"
    )

    layout = generate_castle_layout(
        blueprint
    )

    castle_blocks = generate_castle(
        layout
    )

    print()

    print("Castle 총 블록 수")

    print(len(castle_blocks))

    print()

    print("Tower Top View")

    print()

    visualize_tower_slice()