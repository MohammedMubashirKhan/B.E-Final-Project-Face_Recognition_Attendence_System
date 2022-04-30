# from sklearn import svm
import pickle
from time import time
import cv2
import os
from sklearn import svm
import face_recognition
import markAttedence
import numpy as np
import Face_Mesh.medoapipe_face_mesh as medoapipe_face_mesh
import face_recognition as fr
localMP = medoapipe_face_mesh.FaceMesh()
from Face_Mesh.mediapipe_face_detection import FaceDetection
fd = FaceDetection()

class Save_Encoding:
    def save_face_recognize_data(dir):
        face_encoding_average = np.array(128) * 0
        # Training the SVC classifier
        # The training data would be all the 
        # face encodings from all the known 
        # images and the labels are their names
        dir = "GetStudentDetails/Students Encoding of Face"
        # Training directory
        if dir[-1]!='/':
            dir += '/'
        train_dir = os.listdir(dir)
    
        # Loop through each person in the training directory
        for person in train_dir:
            pix = os.listdir(dir + person)
    
            # Loop through each training image for the current person
            for person_img in pix:
                # Get the face encodings for the face in each image file
                face = cv2.imread(
                    dir + person + "/" + person_img)
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face_bounding_boxes = [(0, face.shape[1], face.shape[0], 0)]
                # cv2.imshow("face", cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
                cv2.waitKey(1)
    
                # If training image contains exactly one face
                if len(face_bounding_boxes) == 1:
                    face_enc = face_recognition.face_encodings(face, known_face_locations= face_bounding_boxes)[0]
                    # Add face encoding for current image 
                    # with corresponding label (name) to the training data
                
                    # encodings.append(face_enc)
                    # names.append(person)
                else:
                    print(person + "/" + person_img + " can't be used for training")
        

            save_face_encoding = {}   
            print(os.path.exists("face_Encoding.dat"))
            # if  
            try:
                with open("face_Encoding.dat", "rb") as f:
                    save_face_encoding = pickle.load(f)
                    save_face_encoding[person] = face_enc
            except:
                save_face_encoding[person] = face_enc
            
            with open("face_Encoding.dat", "wb") as f:
                pickle.dump(save_face_encoding, f)
        cv2.destroyAllWindows()
                
                
    
  

    
        # # Find all the faces in the test image using the default HOG-based model
        # face_locations = face_recognition.face_locations(test_image)

        # no = len(face_locations)
        # print("Number of faces detected: ", no)
        # for (top, right, bottom, left) in face_locations:
        #     cv2.rectangle(test_image,(left,top), (right, bottom), color=(0,0,255), thickness=2)
        #     cv2.imshow("test image", cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB))
        #     cv2.waitKey(0)
    
        # # Predict all the faces in the test image using the trained classifier
        # print("Found:")
        # for i in range(no):
        #     test_image_enc = face_recognition.face_encodings(test_image, known_face_locations=face_locations)[i]
        #     name = clf.predict([test_image_enc])
        #     print(*name)
        






    # cap = cv2.VideoCapture(0)
    # frame_width = cap.get(3) / 4
    # frame_width = int (frame_width)
    # frame_height = cap.get(4) / 4
    # frame_height = int (frame_height)
    # pastTime = 0
    # count = 0
    # process_this_frame = True
    # only_one = True
    # face_encoding_average = np.array(128) * 0
    # while(count < 20):
    #     success, frame = cap.read()
    #     if success != True or cv2.waitKey(1) == ord('q'):
    #         print("Video has ended")
    #         break
    #     count +=1
    #     # print(frame.shape)
    #     # frame = cv2.flip(frame,1)
    #     small_frame = cv2.resize(frame, dsize=(frame_width, frame_height), dst=-1,)
    #     small_frameRGB = cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)
    #     cv2.imshow("small_frame", small_frame)


    #     ## processing face mesh and storing all point in a list in pixel form
    #     ## for processing face mesh the function required image in RGB format
    #     face_meshs_custom_landmarks = localMP.faceMeshDetection(small_frameRGB, enlargeby=4)
    #     # localMP.drawFaceMeshPoints(frame, face_meshs_custom_landmarks=face_meshs_custom_landmarks)
    #     faceLocation = localMP.extractFace(face_meshs_custom_landmarks=face_meshs_custom_landmarks)
    #     # print("faceLocation : ",faceLocation)
    #     # face_encodings = []

    #     try:
    #         for (ymin, xmax, ymax, xmin) in faceLocation:
    #             # xmin = xmin * 4 
    #             # ymin = ymin * 4 
    #             # xmax = xmax * 4 
    #             # ymax = ymax * 4 
    #             cv2.rectangle(frame, (xmin, ymin), (xmax, ymax),color=(0,0,255),thickness=2)
    #             # cv2.imshow("Croped", frame[ymin:ymax,xmin:xmax,0:3])
    #     #         cv2.imshow("CropedRGB", frameRGB[ymin:ymax,xmin:xmax,0:3])
    #     #         face_encoding = fr.face_encodings(face_image=frameRGB)
    #     #         face_encodings.append(face_encoding[0])
    #     #         print(face_encoding[0]) 
    #     #         print()
    #     #         count += 1
    #     #         if count == 2:
    #     #             exit()
    #     except Exception as e:
    #         print(e)
        
    #     if only_one and faceLocation:
    #         for (ymin, xmax, ymax, xmin) in faceLocation:
    #             face_Encoding_only_one = fr.face_encodings(face_image=frame, known_face_locations=[(ymin, xmax, ymax, xmin)])[0]
    #             only_one =False

    #     if process_this_frame and faceLocation:
    #         face_encodings = fr.face_encodings(frame, faceLocation)
    #         if face_encodings:
    #             test = face_encodings[0]
    #             face_encoding_average = (face_encoding_average+test)/2
    #     # process_this_frame = not process_this_frame

    #     # faces = fr.face_locations(small_frameRGB)
    #     # print("face_recognition :",faces)
    #     # for (top, right, bottom, left) in faces:
    #     # #     print("Inside forr loop")
    #     #     top *=4
    #     #     right *=4
    #     #     bottom *=4
    #     #     left *=4
    #     #     cv2.rectangle(frame, (left,top),(right,bottom),
    #     #                 color=(0,255,0), thickness=2)
    #     #     cv2.imshow("Croped", frameRGB[top:bottom,left:right,0:3])
    #     #     faceEncoding = fr.face_encodings(frameRGB[top:bottom,left:right,0:3])


















    #     currentTime = time()
    #     fps = 1/(currentTime - pastTime)
    #     fps = int(fps)

    #     pastTime = currentTime
    #     cv2.putText(frame, str(fps)+" FPS", (30,30), cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0,120,255), thickness=2)
    #     cv2.imshow("frame", frame)
    # cv2.destroyAllWindows()



    # data = {
    #     "Mubashir Khan":face_Encoding_only_one,
    #     "Mubashir averge":face_encoding_average
    # }
    # all_face_encoding = {}

    def recognize_face():
        markattendence_obj = markAttedence.MarkAttendence()
        pastTime = 0
        process_this_frame = True
        try:
            with open("face_Encoding.dat", "rb") as f:
                all_face_encoding = pickle.load(f)
                face_name = list(all_face_encoding.keys())
                face_encodings = np.array(list(all_face_encoding.values()))
                face_name_count = np.zeros(len(face_name), dtype=np.uint8)
        except:
            print("face encoding.dat file NOT FOUND")
            # all_face_encoding[name] = face_encoding_average    
            # with open("face_Encoding.dat", "wb") as f:
            #     pickle.dump(all_face_encoding, f)
        cap = cv2.VideoCapture(0)
        print(face_name)
        print(face_encodings)
        print(face_name_count)
        while True:
            success, frame = cap.read()
            if success != True :
                print("Video has ended")
                break
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # fd.faceDetection(image=frameRGB)

            face_meshs_custom_landmarks = localMP.faceMeshDetection(image=frameRGB)
            facesLocations = localMP.extractFace(face_meshs_custom_landmarks=face_meshs_custom_landmarks)

            if facesLocations and process_this_frame:
                
                # print(faceLocation)
                for faceLocation in  facesLocations:
                    unKnow_face = fr.face_encodings(face_image=frameRGB, known_face_locations=[faceLocation])
                    result = fr.compare_faces(face_encodings, unKnow_face, tolerance=0.6)
                    # print(result)
                    # TO check which index is true in result
                    for i in range(len(result)):
                        if result[i] == True:
                            break

                    if result[i]:
                        print(face_name_count[i])
                        cv2.rectangle(frame, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]),color=(0,255,0),thickness=1)
                        # cv2.rectangle(frame, (x1, y1), (x2, y2),color=(0,255,0),thickness=1)
                        cv2.putText(frame, face_name[i], (faceLocation[3],faceLocation[0]+20), cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0,0,255), thickness=1)
                        face_name_count[i] += 1
                        if face_name_count[i] == 25:
                            # TODO:Now mark this student attendence 
                            cv2.rectangle(frame, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]),color=(0,255,0),thickness=-1)
                            markattendence_obj.markAttendence(attendenceFilePath="attendence.csv", UIN_name=face_name[i])
                        else:
                            markAttendence_obj = markAttedence.MarkAttendence()
                            markAttendence_obj.markAbsent(attendenceFilePath="attendence.csv")
                    else:
                    # for (y1,x2,y2,x1) in [face]:
                        cv2.rectangle(frame, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]),color=(0,0,255),thickness=2)
                        cv2.putText(frame, "UnKnow Face", (faceLocation[3],faceLocation[0]+20), cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0,0,255), thickness=1)
                        # cv2.rectangle(frame, (x1, y1), (x2, y2),color=(0,0,255),thickness=2)
                        # cv2.putText(frame, "UnKnow Face", (x1,y1+20), cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0,0,255), thickness=1)

                currentTime = time()
                fps = int(1/(currentTime - pastTime))
                pastTime = currentTime
                cv2.putText(frame, str(fps)+" FPS", (30,30), cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0,120,255), thickness=2)
                cv2.imshow("face", frame)
                cv2.waitKey(1)
            else:
                pass
                # result =False
            process_this_frame = not process_this_frame
            print(len(face_name_count))
            # for i in range(len(face_name_count)):
                
            #     if (face_name_count[i] > 0 and face_name_count[i] < 25):
            #         break
            #     elif i == len(face_name_count)-1:
            #         cv2.destroyAllWindows()
            #         cap.release()
            #         print("Breaak hjgabgh")
            #         return 0
            # if cv2.waitKey(10) == ord('q'):
            #     break
            
        cv2.destroyAllWindows()
        cap.release()
        print("Breaak")

    if __name__ == "__main__":
        # save_face_recognize_data("GetStudentDetails/Students Encoding of Face")
        recognize_face()


