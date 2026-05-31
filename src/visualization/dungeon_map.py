import matplotlib.pyplot as plt

from src.generation.blueprint_generator import generate_blueprint
from src.generation.layout_generator import generate_dungeon_layout

from src.structures.dungeon_generator import generate_dungeon


# -------------------------
# Dungeon 생성
# -------------------------

blueprint = generate_blueprint(
    "dungeon"
)

layout = generate_dungeon_layout(
    blueprint
)

dungeon_blocks = generate_dungeon(
    layout
)

# -------------------------
# 좌표 추출
# -------------------------

x_list = []
z_list = []

for x, y, z, block_type in dungeon_blocks:

    if y == 0:

        x_list.append(x)
        z_list.append(z)

# -------------------------
# 시각화
# -------------------------

plt.figure(
    figsize=(8, 8)
)

plt.scatter(
    x_list,
    z_list,
    s=30
)

plt.title(
    "Dungeon Top View"
)

plt.xlabel("X")
plt.ylabel("Z")

plt.axis("equal")

plt.grid(True)

plt.show()