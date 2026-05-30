# torchvision 안에 있는 데이터셋 관련 기능
from torchvision import datasets, transforms

# DataLoader : 배치 단위로 데이터를 가져옴
# random_split : Train / Validation 데이터 분리
from torch.utils.data import DataLoader, random_split


def get_dataloaders(
        dataset_path="dataset",
        batch_size=16,
        train_ratio=0.8
):
    """
    dataset_path : 데이터셋 폴더 경로

    batch_size : 한 번에 학습할 이미지 개수

    train_ratio : Train 데이터 비율
    """

    # Data Augmentation
    # 데이터 수가 적기 때문에 이미지를 변형해서 학습 데이터 다양화

    transform = transforms.Compose([

        # 모든 이미지를 224 x 224 크기로 통일
        transforms.Resize((224, 224)),

        # 좌우 반전
        transforms.RandomHorizontalFlip(),

        # -10도 ~ +10도 회전
        transforms.RandomRotation(10),

        # 밝기/대비/채도 랜덤 변경
        transforms.ColorJitter(
            brightness=0.2,
            contrast=0.2,
            saturation=0.2
        ),

        # PIL 이미지를 Tensor로 변환
        transforms.ToTensor()
    ])

    # ImageFolder
    # 현재 구조
    #
    # dataset/
    # ├── castle
    # ├── village
    # └── dungeon
    #
    # 를 자동으로 읽어서
    #
    # castle  -> 0
    # dungeon -> 1
    # village -> 2
    #
    # 와 같이 라벨을 생성

    dataset = datasets.ImageFolder(
        root=dataset_path,
        transform=transform
    )

    # Train / Validation 분할
    train_size = int(len(dataset) * train_ratio)

    val_size = len(dataset) - train_size

    train_dataset, val_dataset = random_split(
        dataset,
        [train_size, val_size]
    )

    # DataLoader 생성
    # shuffle=True → 학습할 때 데이터 순서를 섞음
    # shuffle=False → 검증은 순서 유지
    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=batch_size,
        shuffle=False
    )

    return train_loader, val_loader, dataset.classes

# 테스트용 코드
if __name__ == "__main__":

    train_loader, val_loader, classes = get_dataloaders()

    print("클래스 목록")
    print(classes)

    print()

    print("Train Batch 수")
    print(len(train_loader))

    print()

    print("Validation Batch 수")
    print(len(val_loader))