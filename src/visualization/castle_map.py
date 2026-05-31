import matplotlib.pyplot as plt
from src.generation.blueprint_generator import generate_blueprint
from src.generation.layout_generator import generate_castle_layout

from src.structures.castle_generator import generate_castle


# ----------------------------------
# 성 생성
# ----------------------------------

blueprint = generate_blueprint(
    "castle"
)

layout = generate_castle_layout(
    blueprint
)

castle_blocks = generate_castle(
    layout
)

# ----------------------------------
# 맵 크기 계산
# ----------------------------------

max_x = max(
    block[0]
    for block in castle_blocks
)

max_z = max(
    block[2]
    for block in castle_blocks
)

# ----------------------------------
# 좌표 수집
# ----------------------------------

x_list = []
z_list = []

for x, y, z, block_type in castle_blocks:

    # 바닥층만 시각화
    if y == 0:

        x_list.append(x)
        z_list.append(z)

# ----------------------------------
# 그래프 출력
# ----------------------------------

plt.figure(
    figsize=(8, 8)
)

plt.scatter(
    x_list,
    z_list,
    s=20
)

plt.title(
    "Castle Top View"
)

plt.xlabel("X")
plt.ylabel("Z")

plt.axis("equal")

plt.grid(True)

plt.show()