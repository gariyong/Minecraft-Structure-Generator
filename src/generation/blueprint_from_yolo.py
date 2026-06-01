def create_blueprint_from_yolo(
        width_ratio,
        height_ratio
):

    # 성 크기 결정

    if width_ratio > 0.7:

        size = "large"

    elif width_ratio > 0.4:

        size = "medium"

    else:

        size = "small"

    # 탑 높이

    tower_height = int(
        8 +
        height_ratio * 20
    )

    # 중앙 건물

    keep_height = int(
        10 +
        height_ratio * 25
    )

    blueprint = {

        "type": "castle",

        "size": size,

        "tower_count": 4,

        "tower_height":
            tower_height,

        "wall_height":
            int(
                tower_height * 0.5
            ),

        "keep_size":
            int(
                8 +
                width_ratio * 8
            ),

        "keep_height":
            keep_height,

        "wall": True,

        "gate": True
    }

    return blueprint