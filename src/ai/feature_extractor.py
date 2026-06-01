import cv2


def extract_castle_features(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    gray = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    edges = cv2.Canny(
        gray,
        100,
        200
    )

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # ------------------------
    # 이미지 크기
    # ------------------------

    height, width = gray.shape

    # ------------------------
    # 중앙에 가까운 큰 Contour 찾기
    # ------------------------

    best_contour = None
    best_area = 0

    for contour in contours:

        x, y, w, h = cv2.boundingRect(
            contour
        )

        area = w * h

        cx = x + w / 2

        if (
            width * 0.2
            <
            cx
            <
            width * 0.8
        ):

            if area > best_area:

                best_area = area

                best_contour = contour

    # ------------------------
    # 예외 처리
    # ------------------------

    if best_contour is None:

        best_contour = max(
            contours,
            key=cv2.contourArea
        )

    castle_x, castle_y, castle_w, castle_h = \
        cv2.boundingRect(
            best_contour
        )

    # ------------------------
    # Contour 시각화
    # ------------------------

    contour_image = image.copy()

    cv2.drawContours(
        contour_image,
        contours,
        -1,
        (0, 255, 0),
        2
    )

    cv2.imwrite(
        "castle_contours.png",
        contour_image
    )

    # ------------------------
    # Castle Bounding Box
    # ------------------------

    castle_image = image.copy()

    cv2.rectangle(
        castle_image,
        (castle_x, castle_y),
        (
            castle_x + castle_w,
            castle_y + castle_h
        ),
        (255, 0, 0),
        4
    )

    cv2.imwrite(
        "castle_bbox.png",
        castle_image
    )

    # ------------------------
    # Tower Candidate 탐색
    # ------------------------

    tower_candidates = []

    candidate_image = image.copy()

    for contour in contours:

        x, y, w, h = cv2.boundingRect(
            contour
        )

        area = w * h

        ratio = h / w

        if (
            area > 5000
            and
            ratio > 1.5
        ):

            tower_candidates.append(
                (
                    x,
                    y,
                    w,
                    h
                )
            )

            cv2.rectangle(
                candidate_image,
                (x, y),
                (x + w, y + h),
                (0, 0, 255),
                3
            )

    cv2.imwrite(
        "tower_candidates.png",
        candidate_image
    )

    # ------------------------
    # Feature 계산
    # ------------------------

    castle_width_ratio = (
        castle_w / width
    )

    castle_height_ratio = (
        castle_h / height
    )

    features = {

        "image_width":
            width,

        "image_height":
            height,

        "contour_count":
            len(contours),

        "tower_count":
            len(tower_candidates),

        "castle_width_ratio":
            castle_width_ratio,

        "castle_height_ratio":
            castle_height_ratio
    }

    # ------------------------
    # 출력
    # ------------------------

    print()

    print(
        "Tower Count:",
        len(tower_candidates)
    )

    print()

    print(
        "Castle Bounding Box"
    )

    print(
        castle_x,
        castle_y,
        castle_w,
        castle_h
    )

    print()

    print(
        "Width Ratio:",
        castle_width_ratio
    )

    print(
        "Height Ratio:",
        castle_height_ratio
    )

    return features


if __name__ == "__main__":

    features = extract_castle_features(
        "test_images/castle_test.jpg"
    )

    print()

    print(
        "Castle Features"
    )

    print(
        features
    )