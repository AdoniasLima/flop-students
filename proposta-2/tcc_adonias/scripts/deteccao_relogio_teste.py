import os
import dlib
import cv2
import glob

detectorRelogio = dlib.simple_object_detector("../treinamento_xml/detector_etiquetas.svm")
for imagem in glob.glob(os.path.join("../imagens_etiquetas", "*.jpg")):
    img = cv2.imread(imagem)
    objetos_detectados = detectorRelogio(img, 2)
    for d in objetos_detectados:
        e, t, d, b = (int(d.left()), int(d.top()), int(d.right()), int(d.bottom()))
        cv2.rectangle(img, (e, t), (d, b), (0, 0, 255), 2)
    cv2.imshow("Detector", img)
    cv2.waitKey(0)
cv2.destroyAllWindows()