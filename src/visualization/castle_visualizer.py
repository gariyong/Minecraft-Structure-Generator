from src.generation.blueprint_generator import generate_blueprint
from src.generation.layout_generator import generate_castle_layout


# ==========================================
# Layout 기반 시각화
# ==========================================

blueprint = generate_blueprint(
    "castle"
)

layout = generate_castle_layout(
    blueprint
)

size = layout["size"]

grid = []

for _ in range(size + 1):
    grid.append([" "] * (size + 1))

# ------------------------
# Wall
# ------------------------

for x in range(size + 1):

    grid[0][x] = "="
    grid[size][x] = "="

for z in range(size + 1):

    grid[z][0] = "|"
    grid[z][size] = "|"

# ------------------------
# Gate
# ------------------------

gate_x, gate_z = layout["gate"]

for x in range(
    gate_x - 2,
    gate_x + 3
):
    grid[gate_z][x] = " "

# ------------------------
# Towers
# ------------------------

for tower_x, tower_z in layout["towers"]:

    for dz in range(-2, 3):

        for dx in range(-2, 3):

            x = tower_x + dx
            z = tower_z + dz

            if (
                0 <= x <= size
                and
                0 <= z <= size
            ):
                grid[z][x] = "T"

# ------------------------
# Keep
# ------------------------

keep_x, keep_z = layout["keep"]

for dz in range(-5, 5):

    for dx in range(-5, 5):

        x = keep_x + dx
        z = keep_z + dz

        if (
            0 <= x <= size
            and
            0 <= z <= size
        ):
            grid[z][x] = "K"

# ------------------------
# 출력
# ------------------------

for row in grid:
    print("".join(row))