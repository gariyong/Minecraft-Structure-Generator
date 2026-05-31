# Castle Layout 생성기

def generate_castle_layout(blueprint):

    size_name = blueprint["size"]

    if size_name == "small":
        size = 20

    elif size_name == "medium":
        size = 30

    else:
        size = 40

    TOWER_RADIUS = 3
    layout = {

        "size": size,

        # 탑을 성벽 안쪽으로 이동
        "towers": [

            (TOWER_RADIUS, TOWER_RADIUS),

            (
                size - TOWER_RADIUS,
                TOWER_RADIUS
            ),

            (
                TOWER_RADIUS,
                size - TOWER_RADIUS
            ),

            (
                size - TOWER_RADIUS,
                size - TOWER_RADIUS
            )
        ],

        "keep": (
            size // 2,
            size // 2
        ),

        # 게이트는 아래 중앙
        "gate": (
            size // 2,
            size - TOWER_RADIUS
        )
    }

    return layout