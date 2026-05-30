import torch
import torch.nn as nn


# 건축물 분류 CNN
# 입력:
#   224 x 224 RGB 이미지
#
# 출력:
#   Castle
#   Dungeon
#   Village
#
# 클래스 수 = 3
class BuildingClassifier(nn.Module):

    def __init__(self):
        super().__init__()

        # CNN Block 1
        # 입력
        #   [3, 224, 224]
        #
        # Conv2D
        #   3채널(RGB) -> 16채널
        #
        # 출력
        #   [16, 224, 224]
        #
        # MaxPool
        #
        # 출력
        #   [16, 112, 112]

        self.conv1 = nn.Sequential(

            nn.Conv2d(

                # RGB 이미지
                in_channels=3,

                # 특징맵 16개 생성
                out_channels=16,

                # 3x3 필터 사용
                kernel_size=3,

                # 가장자리가 잘리지 않도록 패딩
                padding=1
            ),

            # 음수 제거
            nn.ReLU(),

            # 이미지 크기 절반으로 축소 224 -> 112
            nn.MaxPool2d(kernel_size=2)
        )

        # CNN Block 2
        #
        # 입력
        #   [16, 112, 112]
        #
        # 출력
        #   [32, 56, 56]

        self.conv2 = nn.Sequential(

            nn.Conv2d(
                in_channels=16,
                out_channels=32,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(kernel_size=2)
        )

        # CNN Block 3
        #
        # 입력
        #   [32, 56, 56]
        #
        # 출력
        #   [64, 28, 28]

        self.conv3 = nn.Sequential(

            nn.Conv2d(
                in_channels=32,
                out_channels=64,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(kernel_size=2)
        )
        # Global Average Pooling
        #현재 특징맵 크기 [64, 28, 28]에서 28x28 전체를 평균내서 각 특징맵당 숫자 하나만 남김
        self.global_pool = nn.AdaptiveAvgPool2d((1, 1))

        # 분류기(Classifier)
        self.classifier = nn.Sequential(

        # [64,1,1] >> [64]
        nn.Flatten(),

        # 작은 은닉층 64개의 특징 >> 32개의 특징
        nn.Linear(64, 32),
        nn.ReLU(),
        
        # 최종 출력
        #
        # Castle
        # Dungeon
        # Village
        #
        nn.Linear(32, 3)
    )

    # Forward Propagation
    # 실제 데이터가 흐르는 경로
    def forward(self, x):

        # CNN Block 1 통과
        x = self.conv1(x)

        # CNN Block 2 통과
        x = self.conv2(x)

        # CNN Block 3 통과
        x = self.conv3(x)

        # 특징맵 압축
        x = self.global_pool(x)

        # 분류기 통과
        x = self.classifier(x)

        return x



if __name__ == "__main__":

    # 모델 생성
    model = BuildingClassifier()

    # 가짜 이미지 생성
    #
    # 형태:
    #
    # [배치크기, 채널, 높이, 너비]
    #
    # [1, 3, 224, 224]
    #
    dummy_input = torch.randn(
        1,
        3,
        224,
        224
    )

    # 모델에 통과
    output = model(dummy_input)

    print("출력 형태")

    print(output.shape)