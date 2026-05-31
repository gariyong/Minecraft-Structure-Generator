def visualize_castle(layout):

    size = layout["size"] + 1

    grid = []

    for _ in range(size):
        grid.append([" "] * size)

    # Wall
    for x in range(size):

        grid[0][x] = "="
        grid[size - 1][x] = "="

    for z in range(size):

        grid[z][0] = "|"
        grid[z][size - 1] = "|"

    # Gate
    gate_x, gate_z = layout["gate"]

    grid[gate_z][gate_x] = "G"

    # Towers
    for tower_x, tower_z in layout["towers"]:

        grid[tower_z][tower_x] = "T"

    # Keep
    keep_x, keep_z = layout["keep"]

    for dz in range(-2, 3):

        for dx in range(-2, 3):

            x = keep_x + dx
            z = keep_z + dz

            if (
                0 <= x < size
                and
                0 <= z < size
            ):
                grid[z][x] = "K"

    # 출력
    for row in grid:
        print("".join(row))

if __name__ == "__main__":

    from src.generation.blueprint_generator import generate_blueprint
    from src.generation.layout_generator import generate_castle_layout

    blueprint = generate_blueprint(
        "castle"
    )

    layout = generate_castle_layout(
        blueprint
    )

    visualize_castle(layout)