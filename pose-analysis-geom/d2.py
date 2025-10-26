import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Tidak dapat membuka webcam")

detector = PoseDetector(
    staticMode=False,
    modelComplexity=1,
    smoothLandmarks=True,
    enableSegmentation=False,
    smoothSegmentation=True,
    detectionCon=0.5,
    trackCon=0.5
    )

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmlist, bboxInfo = detector.findPosition(img, draw=True)

    if lmlist:
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        
        length, img, info = detector.findDistance(
            lmlist[11][0:2],
            lmlist[15][0:2],
            img=img,
            color=(255, 0, 0),
            scale=10
        )

        angle, img = detector.findAngle(
            lmlist[11][0:2],
            lmlist[13][0:2],
            lmlist[15][0:2],
            img=img,
            color=(0, 0, 255),
            scale=10
        )

        isCloseAngle50 = detector.angleCheck(
            myAngle=angle,
            targetAngle=50,
            offset=10
        )

        print(f"Jarak: {length}, Sudut: {angle}, Dekat dengan 50 derajat: {isCloseAngle50}")

    cv2.imshow("Webcam Pose Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()