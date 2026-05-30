import torch
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

from dataset import get_dataloaders
from model import BuildingClassifier


# 데이터 로드
train_loader, val_loader, classes = get_dataloaders()
print("클래스")
print(classes)

# 모델 생성
model = BuildingClassifier()

# 학습된 모델 불러오기
model.load_state_dict(
    torch.load("best_model.pth")
)

# 평가 모드
model.eval()

# 실제값 / 예측값 저장
true_labels = []
predicted_labels = []

# Validation 데이터 평가
with torch.no_grad():

    for images, labels in val_loader:

        outputs = model(images)

        _, predictions = torch.max(outputs, 1)

        true_labels.extend(labels.numpy())

        predicted_labels.extend(predictions.numpy())

# Confusion Matrix 생성
cm = confusion_matrix(
    true_labels,
    predicted_labels
)

# 시각화
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=classes
)

disp.plot()

plt.title("Building Classification Confusion Matrix")

plt.tight_layout()

plt.savefig("confusion_matrix.png")

plt.show()

print()
print("저장 완료 -> confusion_matrix.png")