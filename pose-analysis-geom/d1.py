import cv2, time

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Tidak dapat membuka webcam")

frames, t0 = 0, time.time()
while True:
    ok, frame = cap.read()
    if not ok:
        print("Gagal membaca frame dari webcam")
        break

    frames += 1
    t1 = time.time()
    if t1 - t0 >= 1.0:
        cv2.setWindowTitle("Webcam Preview", f"Webcam Preview - FPS: {frames}")
        frames, t0 = 0, t1

    cv2.imshow("Webcam Preview", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()