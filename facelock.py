import face_recognition as fr
import pickle
import cv2
import os
import sys
import main
video_capture = cv2.VideoCapture(0)
face_is_match = False
face_encodings = []
known_face_encodings = pickle.load(open('SaiSaaketh.pickle','rb'))
print("Loading Encodings")
while True:
        ret, frame = video_capture.read()
        face_locations = fr.face_locations(frame, model="hog")
        face_encodings = fr.face_encodings(frame, face_locations)
        face_names = []
        name = "Unknown"
        for face_encoding in face_encodings:
                print("Matching")
                matches = fr.compare_faces(known_face_encodings, face_encoding, 0.4)
                if True in matches:
                        first_known_face = matches.index(True)
                        print("saisaaketh")
                        face_is_match = True
                else:
                        print("Access Denied")

