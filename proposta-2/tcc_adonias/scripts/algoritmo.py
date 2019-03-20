import os
import dlib
import cv2
import glob

#links = ["link1",'link2','link3']

#print(links)

#def executarApp(dados):
#    for dado in dados:
#        print(dado)

#executarApp(links)
#
# Autor: Adonias
# Data 18/03/2019
# Descrição: Teste para implementação do algoritmo, criação da função executarApp()

dados = dlib.test_simple_object_detector("../treinamento_xml/treinamento_etiquetas.xml", "../treinamento_xml/detector_etiquetas.svm")
print(dados.average_precision) #dados é uma variável que está recebendo a classe acima.

detectorRelogio = dlib.simple_object_detector("../treinamento_xml/detector_etiquetas.svm")
for imagem in glob.glob(os.path.join("../imagens_etiquetas", "etiqueta2.jpg")):
    img = cv2.imread(imagem)
    objetos_detectados = detectorRelogio(img, 2)
    for d in objetos_detectados:
        e, t, d, b = (int(d.left()), int(d.top()), int(d.right()), int(d.bottom()))
        cv2.rectangle(img, (e, t), (d, b), (0, 0, 255), 2)
    cv2.imshow("Detector", img)
    cv2.waitKey(0)
cv2.destroyAllWindows()