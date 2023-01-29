import cv2 as cv2
import numpy as np

def bev(frame):
    # Corners of Top Left , Bottom Left, Top Right, Bottom Right 카메라 FOV 에 맞춰서 정하면 될듯
    tl = (500, 350)
    bl = (0, 1080)
    tr = (1380, 350)
    br = (1920, 1080)

    # 내가 정한 Corner 포인트들 빨간 점으로 표시
    cv2.circle(frame, tl, 5, (0, 0, 255), -1)
    cv2.circle(frame, bl, 5, (0, 0, 255), -1)
    cv2.circle(frame, tr, 5, (0, 0, 255), -1)
    cv2.circle(frame, br, 5, (0, 0, 255), -1)

    # Apply Geometrical Transformation
    pts1 = np.float32([tl, bl, tr, br])
    pts2 = np.float32([[0, 0], [0, 1080], [1920, 0], [1920, 1080]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    print("Bird-eye-view Matrix: \n", matrix)
    t_frame = cv2.warpPerspective(frame, matrix, (1920, 1080))

    return t_frame


if __name__ == "__main__":
    # test image
    # image = cv2.imread('./test_images/24_19-48-02.png')

    # video
    ch0 = cv2.VideoCapture(0)
    ch0.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    ch0.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    while True:
        _, frame = ch0.read()

        transformed_frame = bev(frame)
        cv2.imshow("Frame", frame)
        cv2.imshow("Transformed_frame Bird Eye View", transformed_frame)

        if cv2.waitKey(1) == 27:
            break