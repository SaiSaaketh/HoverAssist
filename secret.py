import cv2
import os 
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    else:
        img_name = "SaiSaaketh_{}.png".format(img_counter)
        img_path=f"F:\\SAISAAKETH'S FOLDER\\Programming\\Python\\Hover Family\\HoverAssist\\face_db\\{img_name}"
        cv2.imwrite(img_path, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
