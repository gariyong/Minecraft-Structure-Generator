# Minecraft Structure Generator

## 프로젝트 소개

컴퓨터 비전 기술을 활용하여 판타지 건축물 이미지를 분석하고, 이를 기반으로 마인크래프트 구조물을 자동 생성하는 프로젝트입니다.

입력 이미지에서 성(Castle)을 인식한 뒤, 객체 탐지 및 특징 추출 과정을 거쳐 구조물 설계도(Blueprint)를 생성하고, 최종적으로 마인크래프트에서 실제 구조물을 생성합니다.

---

## 프로젝트 목표

기존의 이미지 분류 또는 객체 탐지 프로젝트는 객체를 인식하는 단계에서 끝나는 경우가 많습니다.

본 프로젝트는 단순히 성을 인식하는 것에서 끝나지 않고,

* 이미지 분석
* 객체 탐지
* 구조 정보 생성
* 마인크래프트 구조물 생성

까지의 전체 파이프라인을 구현하는 것을 목표로 하였습니다.

---

## 시스템 구조

```text
Fantasy Castle Image
        ↓
CNN Classification
        ↓
YOLO Detection
        ↓
Bounding Box Extraction
        ↓
Blueprint Generation
        ↓
Layout Generation
        ↓
Minecraft Block Data
        ↓
JSON Export
        ↓
PaperMC Plugin
        ↓
Minecraft Structure
```

---

# 실행 결과

## 1. 입력 이미지

![Input Image](images/input_castle.jpg)

성 이미지를 입력으로 사용합니다.

---

## 2. YOLO 객체 탐지

![YOLO Detection](images/yolo_detection.jpg)

YOLOv8을 이용하여 성(Castle)의 위치를 탐지합니다.

---

## 3. Blueprint 생성

탐지된 Bounding Box의 너비 및 높이 비율을 이용하여 구조물의 크기와 주요 파라미터를 생성합니다.

참조 파일:

```text
src/ai/predict_yolo.py
src/generation/blueprint_from_yolo.py
```

예시:

```python
{
    "type": "castle",
    "size": "large",
    "tower_count": 4,
    "tower_height": 27,
    "wall_height": 13,
    "keep_size": 14,
    "keep_height": 33
}
```

---

## 4. Layout 생성

Blueprint를 기반으로 성의 주요 구성 요소의 상대 좌표를 생성합니다.

참조 파일:

```text
src/generation/layout_generator.py
```

생성 요소:

* Tower
* Keep
* Gate
* Wall

---

## 5. Minecraft 구조물 생성

![Minecraft Castle](images/minecraft_castle.png)

생성된 Layout 정보는 11,355개의 블록 데이터로 변환되며 JSON 파일로 저장됩니다.

PaperMC 플러그인은 해당 JSON 파일을 읽어 실제 마인크래프트 월드에 구조물을 생성합니다.

참조 파일:

```text
src/structures/castle_generator.py
StructurePlugin/src/main/java/com/aporia/commands/GenerateCastleCommand.java
```

### 생성 결과

* Total Blocks: 11,355
* Structure Type: Castle
* Generation Method: Procedural Generation

---

# 사용 기술

## Computer Vision

* Python
* OpenCV
* PyTorch
* YOLOv8 (Ultralytics)

## Structure Generation

* Procedural Generation
* Blueprint Generator
* Layout Generator

## Minecraft

* Java
* PaperMC
* Maven
* Gson

---

# 데이터셋

## 클래스

* Castle

## 데이터 수

* Total Images: 87

## 데이터 분할

* Train: 70%
* Validation: 20%
* Test: 10%

---

# 프로젝트 성과

* CNN 기반 이미지 분류 구현
* YOLO 기반 객체 탐지 구현
* 이미지 기반 Blueprint 자동 생성
* Procedural Structure Generation 구현
* JSON 기반 Minecraft 구조물 생성
* PaperMC Plugin 연동
* Image → Minecraft 자동 생성 파이프라인 구축

---

## 전체 파이프라인 결과

| Input Image | YOLO Detection | Minecraft Result |
|------------|---------------|------------------|
| ![](images/input_castle.jpg) | ![](images/yolo_detection.jpg) | ![](images/minecraft_castle.png) |

---

# Future Work

## Computer Vision

* Tower Detection
* Gate Detection
* Wall Detection
* Multi-Class Detection

## Structure Generation

* Village Generation
* Dungeon Generation
* Building Style Diversification

## Minecraft

* Real-Time World Generation
* Automatic Structure Placement
* AI-Based Structure Expansion

---

# 프로젝트 결과

본 프로젝트는 컴퓨터 비전 기술을 활용하여 판타지 이미지를 분석하고, 이를 실제 마인크래프트 구조물로 변환하는 전체 파이프라인을 구현하였습니다.

단순한 객체 탐지에 그치지 않고, 탐지 결과를 게임 내 구조물 생성으로 연결함으로써 Computer Vision과 Procedural Generation의 응용 가능성을 확인할 수 있었습니다.
