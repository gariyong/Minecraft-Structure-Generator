from ultralytics import YOLO
from src.generation.blueprint_from_yolo \
    import create_blueprint_from_yolo
from src.structures.castle_generator \
    import generate_castle
from src.generation.layout_generator \
    import generate_castle_layout

model = YOLO(
    "runs/detect/train-2/weights/best.pt"
)

results = model.predict(
    source="test_images/castle_test.jpg",
    save=True,
    conf=0.3
)

for result in results:

    for box in result.boxes:

        x1, y1, x2, y2 = \
            box.xyxy[0].tolist()

        print()

        print("Bounding Box")

        print(
            x1,
            y1,
            x2,
            y2
        )

        width = x2 - x1
        height = y2 - y1

        print()

        print("Width :", width)
        print("Height:", height)

image_width = 736
image_height = 1308

width_ratio = (
    width / image_width
)

height_ratio = (
    height / image_height
)

blueprint = create_blueprint_from_yolo(
    width_ratio,
    height_ratio
)

print()
print("Generated Blueprint")
print(blueprint)

layout = generate_castle_layout(
    blueprint
)

print()
print("Generated Layout")
print(layout)

blocks = generate_castle(
    layout
)

print()
print("Generated Blocks")
print(len(blocks))

import json

json_blocks = []

for x, y, z, block in blocks:

    json_blocks.append({

        "x": x,
        "y": y,
        "z": z,
        "block": block

    })

with open(
    "generated_castle.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        json_blocks,
        f,
        indent=4
    )

print()
print(
    "JSON Saved:",
    len(json_blocks)
)