import sys
from pathlib import Path

import torch
from PIL import Image
from torchvision import transforms

from src.ai.model import BuildingClassifier


CLASSES = [
    "castle",
    "dungeon",
    "village"
]

# 모델 경로
MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "models"
    / "best_model.pth"
)

# ----------------------------------
# 모델 로드
# ----------------------------------
model = BuildingClassifier()

model.load_state_dict(
    torch.load(
        MODEL_PATH,
        map_location="cpu"
    )
)

model.eval()


# ----------------------------------
# 이미지 예측 함수
# ----------------------------------

def predict_image(image_path):

    transform = transforms.Compose([

        transforms.Resize(
            (224, 224)
        ),

        transforms.ToTensor()
    ])

    image = Image.open(
        image_path
    ).convert("RGB")

    image = transform(
        image
    )

    image = image.unsqueeze(0)

    with torch.no_grad():

        output = model(image)

        probabilities = torch.softmax(
            output,
            dim=1
        )

        confidence, prediction = torch.max(
            probabilities,
            dim=1
        )

    predicted_class = CLASSES[
        prediction.item()
    ]

    return (
        predicted_class,
        confidence.item()
    )


# ----------------------------------
# 단독 실행 테스트
# ----------------------------------

if __name__ == "__main__":

    image_path = sys.argv[1]

    prediction, confidence = predict_image(
        image_path
    )

    print()

    print(
        "Prediction:",
        prediction
    )

    print(
        "Confidence:",
        f"{confidence * 100:.2f}%"
    )