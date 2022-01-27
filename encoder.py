import face_recognition as fr
import os
import pickle
import cv2
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

db_path = "F:\\SAISAAKETH'S FOLDER\\Programming\\Python\\Hover Family\\HOVERASSIST\\face_db\\"
faces = os.listdir(db_path)
known_face_encodings = []
n = 1
for face in faces:
    im = fr.load_image_file(db_path + face)
    #encode the first face in the image
    encoding = fr.face_encodings(im)[0]
    known_face_encodings.append(encoding)
    print("%1d of %2d is done"%(n,len(faces)))
    n+=1       
#create a pickle file
file = open('Model.pickle','wb')
#dump encoding in pickle file
pickle.dump(known_face_encodings,file)
file.close()
