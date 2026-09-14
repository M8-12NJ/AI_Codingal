import cv2

for i in range(5):
    print(f"\nTesting camera {i}")

    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Not available")
        continue

    ret, frame = cap.read()
    print("Opened:", cap.isOpened())
    print("Read:", ret)

    if ret:
        cv2.imshow(f"Camera {i}", frame)
        print("Press any key to continue to the next camera...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    cap.release()