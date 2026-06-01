# Castle Layout 생성기

def generate_castle_layout(blueprint):

    size_name = blueprint["size"]

    if size_name == "small":
        size = 20

    elif size_name == "medium":
        size = 30

    else:
        size = 40

    tower_count = blueprint["tower_count"]

    TOWER_RADIUS = 3

    towers = []

    # -------------------
    # 2 Towers
    # -------------------

    if tower_count == 2:

        towers = [

            (
                TOWER_RADIUS,
                TOWER_RADIUS
            ),

            (
                size - TOWER_RADIUS,
                TOWER_RADIUS
            )
        ]

    # -------------------
    # 4 Towers
    # -------------------

    elif tower_count == 4:

        towers = [

            (
                TOWER_RADIUS,
                TOWER_RADIUS
            ),

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
        ]

    # -------------------
    # 6 Towers
    # -------------------

    else:

        towers = [

            (
                TOWER_RADIUS,
                TOWER_RADIUS
            ),

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
            ),

            (
                size // 2,
                TOWER_RADIUS
            ),

            (
                size // 2,
                size - TOWER_RADIUS
            )
        ]

    layout = {

        "size": size,

        "tower_height":
            blueprint["tower_height"],

        "wall_height":
            blueprint["wall_height"],

        "keep_size":
            blueprint["keep_size"],

        "keep_height":
            blueprint["keep_height"],

        "towers": towers,

        "keep": (
            size // 2,
            size // 2
        ),

        "gate": (
            size // 2,
            size - TOWER_RADIUS
        )
    }

    return layout

def generate_village_layout(blueprint):

    size = 40

    layout = {

        "size": size,

        "houses": [

            (10, 10),
            (30, 10),

            (10, 30),
            (30, 30),

            (20, 35)
        ],

        "plaza": (
            size // 2,
            size // 2
        )
    }

    return layout

def generate_dungeon_layout(blueprint):

    size = 40

    layout = {

        "size": size,

        "rooms": [

            # 입구 방
            (20, 35),

            # 중앙 홀
            (20, 20),

            # 좌측 방
            (10, 10),

            # 우측 방
            (30, 10)
        ]
    }

    return layout