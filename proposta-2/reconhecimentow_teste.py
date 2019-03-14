import dlib
import cv2
import os
from glob import glob
import numpy as np

detectorFace = dlib.get_frontal_face_detector()
detectorPontos = dlib.shape_predictor("recursos/shape_predictor_68_face_landmarks.dat")
reconhecimentoFacial = dlib.face_recognition_model_v1("recursos/dlib_face_recognition_resnet_model_v1.dat")
indices = np.load("recursos/indices_w.pickle")
descritorFaciais = np.load("recursos/descritores_w.npy")
limiar = 0.5

for arquivo in glob(os.path.join("imagens", "*.jpg")):
    imagem = cv2.imread(arquivo)
    facesDetectadas = detectorFace(imagem, 2)
    for face in facesDetectadas:
        e, t, d, b = (int(face.left()),int(face.top()),int(face.right()),int(face.bottom()))
        pontosFaciais = detectorPontos(imagem, face)
        descritorFacial = reconhecimentoFacial.compute_face_descriptor(imagem, pontosFaciais)
        listaDescritorFacial = [fd for fd in  descritorFacial]
        npArrayDescritorFacial = np.asarray(listaDescritorFacial, dtype=np.float64)
        npArrayDescritorFacial = npArrayDescritorFacial[np.newaxis, :]

        ditancias = np.linalg.norm(npArrayDescritorFacial - descritorFaciais, axis=1)
        print("Distâncias: {}".format(ditancias))
        minimo = np.argmin(ditancias)
        print(minimo)
        distanciaMinima = ditancias[minimo]
        print(distanciaMinima)

        nome = ""

        if distanciaMinima <= limiar:
            nome = os.path.split(indices[minimo])[1].split(".")[0]

        cv2.rectangle(imagem,(e, t),(d, b),(0, 255, 0), 2)
        texto = "{} {:.4f}".format(nome, distanciaMinima)
        cv2.putText(imagem, texto, (d, t), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0, 255, 0))
    cv2.imshow("Detector", imagem)
    cv2.waitKey(0)
cv2.destroyAllWindows()
