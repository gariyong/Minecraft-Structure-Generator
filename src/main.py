from src.ai.predict import predict_image

from src.generation.blueprint_generator import generate_blueprint

from src.generation.layout_generator import (
    generate_castle_layout,
    generate_village_layout,
    generate_dungeon_layout
)

from src.structures.castle_generator import generate_castle
from src.structures.village_generator import generate_village
from src.structures.dungeon_generator import generate_dungeon

from src.export.json_export import (
    export_blocks_to_json
)


# ----------------------------------
# 입력 이미지
# ----------------------------------

image_path = "test_images/castle_test.jpg"

# ----------------------------------
# CNN 예측
# ----------------------------------

prediction, confidence = predict_image(
    image_path
)

print()
print("Prediction :", prediction)
print(
    "Confidence :",
    f"{confidence * 100:.2f}%"
)

# ----------------------------------
# Blueprint 생성
# ----------------------------------

blueprint = generate_blueprint(
    prediction
)

# ----------------------------------
# Generator 선택
# ----------------------------------

if prediction == "castle":

    layout = generate_castle_layout(
        blueprint
    )

    blocks = generate_castle(
        layout
    )

elif prediction == "village":

    layout = generate_village_layout(
        blueprint
    )

    blocks = generate_village(
        layout
    )

elif prediction == "dungeon":

    layout = generate_dungeon_layout(
        blueprint
    )

    blocks = generate_dungeon(
        layout
    )

else:

    raise ValueError(
        f"알 수 없는 타입: {prediction}"
    )

# ----------------------------------
# 결과
# ----------------------------------

print()

print(
    "생성된 블록 수 :",
    len(blocks)
)

export_blocks_to_json(
    blocks,
    "generated_structure.json"
)