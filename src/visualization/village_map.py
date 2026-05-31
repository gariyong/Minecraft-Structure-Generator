import matplotlib.pyplot as plt

from src.generation.blueprint_generator import generate_blueprint
from src.generation.layout_generator import generate_village_layout

from src.structures.village_generator import generate_village


# -------------------------
# Village 생성
# -------------------------

blueprint = generate_blueprint(
    "village"
)

layout = generate_village_layout(
    blueprint
)

village_blocks = generate_village(
    layout
)

# -------------------------
# 좌표 추출
# -------------------------

x_list = []
z_list = []

for x, y, z, block_type in village_blocks:

    # 바닥층만 출력
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
    "Village Top View"
)

plt.xlabel("X")
plt.ylabel("Z")

plt.axis("equal")

plt.grid(True)

plt.show()