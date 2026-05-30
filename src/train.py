import torch
import torch.nn as nn
import torch.optim as optim

from dataset import get_dataloaders
from model import BuildingClassifier

# 하이퍼파라미터
EPOCHS = 50
LEARNING_RATE = 0.001

# 데이터셋 로드
train_loader, val_loader, classes = get_dataloaders()

print("클래스 목록")
print(classes)
print()

# 모델 생성
model = BuildingClassifier()

# Loss 함수
# 다중 클래스 분류 문제에 적합
criterion = nn.CrossEntropyLoss()

# Optimizer
# Adam 사용, 학습률 : 0.001
optimizer = optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE
)

# 최고 Validation Accuracy 저장용 변수
best_val_accuracy = 0

# 학습 시작
for epoch in range(EPOCHS):

    # TRAIN
    model.train()

    total_loss = 0

    train_correct = 0

    train_total = 0

    for images, labels in train_loader:

        # 이전 gradient 제거
        optimizer.zero_grad()

        # 모델 예측
        outputs = model(images)

        # Loss 계산
        loss = criterion(outputs, labels)

        # 역전파
        loss.backward()

        # 가중치 업데이트
        optimizer.step()

        # Loss 누적
        total_loss += loss.item()

        # 예측 결과
        _, predicted = torch.max(outputs, 1)

        train_total += labels.size(0)

        train_correct += (predicted == labels).sum().item()

    # 평균 Loss 계산
    average_loss = total_loss / len(train_loader)

    # Train Accuracy 계산
    train_accuracy = 100 * train_correct / train_total

    # VALIDATION
    model.eval()
    val_correct = 0
    val_total = 0

    # Validation에서는 역전파 안 함
    with torch.no_grad():

        for images, labels in val_loader:

            outputs = model(images)

            _, predicted = torch.max(outputs, 1)

            val_total += labels.size(0)

            val_correct += (predicted == labels).sum().item()

    val_accuracy = 100 * val_correct / val_total

    # 최고 성능 모델 저장
    if val_accuracy > best_val_accuracy:

        best_val_accuracy = val_accuracy

        torch.save(
            model.state_dict(),
            "best_model.pth"
        )

    # 결과 출력
    print(
        f"Epoch [{epoch+1}/{EPOCHS}] | "
        f"Loss: {average_loss:.4f} | "
        f"Train Acc: {train_accuracy:.2f}% | "
        f"Val Acc: {val_accuracy:.2f}%"
    )

# 최종 결과
print()
print("학습 완료")
print(f"최고 Validation Accuracy: {best_val_accuracy:.2f}%")
print("모델 저장 완료 -> best_model.pth")