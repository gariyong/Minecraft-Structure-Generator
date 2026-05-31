import json


def export_blocks_to_json(
        blocks,
        output_path
):

    data = []

    for x, y, z, block_type in blocks:

        data.append(
            {
                "x": x,
                "y": y,
                "z": z,
                "block": block_type
            }
        )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    print()

    print(
        "JSON 저장 완료 :",
        output_path
    )