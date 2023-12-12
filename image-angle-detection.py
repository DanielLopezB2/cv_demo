import cv2
import mediapipe as mp
import numpy as np

def calculate_angle(a, b, c):
    a = np.array(a) # Primer punto
    b = np.array(b) # Segundo punto
    c = np.array(c) # Tercer punto
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
        
    return angle

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

#Puntos articulares
right_shoulder = 12
left_shoulder = 11
right_elbow = 14
left_elbow = 13
right_wrist = 16
left_wrist = 15
right_hip = 24
left_hip = 23
right_knee = 26
left_knee= 25
right_ankle = 28
left_ankle = 27

with mp_pose.Pose(
    static_image_mode = True) as pose:

    image = cv2.imread("Image-Treatment/BarbellSquat/BarbellSquat1.jpg")
    height, width, _ = image.shape
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    results = pose.process(image_rgb)
    print("Pose landmarks:", results.pose_landmarks)
    
    if results.pose_landmarks is not None:
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(128,0,250), thickness=2, circle_radius=3),
                mp_drawing.DrawingSpec(color=(0,255,0), thickness=2)
            )
            
            try:
                landmarks = results.pose_landmarks.landmark
                
                # Coordenadas de las articulaciones del hombro, codo y muñeca del lado derecho
                shoulder = [landmarks[right_shoulder].x, landmarks[right_shoulder].y]
                elbow = [landmarks[right_elbow].x, landmarks[right_elbow].y]
                wrist = [landmarks[right_wrist].x, landmarks[right_wrist].y]
                
                # Calcula el ángulo del codo derecho
                angle = calculate_angle(shoulder, elbow, wrist)
                
                # Coordenadas de las articulaciones del hombro y la muñeca del lado derecho
                shoulder_wrist = [shoulder, wrist]

                # Calcula el ángulo del hombro y la muñeca del lado derecho
                angle_shoulder_wrist = calculate_angle(shoulder_wrist[0], shoulder_wrist[1], wrist)

                # Redondear el resultado
                angle_shoulder_wrist = round(angle_shoulder_wrist, 2)

                # Muestra el ángulo en el frame de la videocaptura
                cv2.putText(image, str(angle_shoulder_wrist),
                        tuple(np.multiply(shoulder, [width, height]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0), 1, cv2.LINE_AA)
                
                
                #Redondear el resultado
                angle = round(angle, 2)
                
                # Muestra el ángulo en el frame de la videocaptura
                cv2.putText(image, str(angle),
                            tuple(np.multiply(elbow, [width, height]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0), 1, cv2.LINE_AA)
                
                # Coordenadas de las articulaciones del hombro, codo y muñeca del lado izquierdo
                shoulder2 = [landmarks[left_shoulder].x, landmarks[left_shoulder].y]
                elbow2 = [landmarks[left_elbow].x, landmarks[left_elbow].y]
                wrist2 = [landmarks[left_wrist].x, landmarks[left_wrist].y]
                
                # Calcula el ángulo del codo izquierdo
                angle2 = calculate_angle(shoulder2, elbow2, wrist2)
                
                #Redondear el resultado
                angle2 = round(angle, 2)
                
                # Muestra el ángulo en la imagen
                cv2.putText(image, str(angle2),
                            tuple(np.multiply(elbow2, [width, height]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0), 1, cv2.LINE_AA)
                

            except:
                pass

    cv2.imshow("Image", image)
    cv2.waitKey(0)

cv2.destroyAllWindows()