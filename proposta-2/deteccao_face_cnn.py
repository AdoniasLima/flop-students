import cv2
import dlib

imagem = cv2.imread("fotos/grupo.9.jpg")
detector = dlib.cnn_face_detection_model_v1('recursos/mmod_human_face_detector.dat')
faceDetecadas = detector(imagem, 1)
print(faceDetecadas)
print(len(faceDetecadas))
for face in faceDetecadas:
    e, t, d, b, c = (int(face.rect.left()), int(face.rect.top()), int(face.rect.right()), int(face.rect.bottom()), face.confidence)
    print(c)
    cv2.rectangle(imagem, (e, t), (d, b), (255, 0, 0), 2)

cv2.imshow("Detector Cnn", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()