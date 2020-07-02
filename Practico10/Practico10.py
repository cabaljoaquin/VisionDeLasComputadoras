import cv2
import numpy as np
from imutils import perspective, contours, grab_contours
from scipy.spatial.distance import euclidean

Referencia = 10
ChosenImgInitial = cv2.imread('medicion_objetos.jpeg', 1)

#Se debe trabajar la imagen le aplicamos un filtro gaussiano que le quita nitides a la imagen y
# nos permite eliminar todos los detalles que no nos interesan de la vista para despues aplicarle un filtro por bordes
FilterImg = cv2.cvtColor(ChosenImgInitial, cv2.COLOR_BGR2GRAY)
FilterImg = cv2.GaussianBlur(FilterImg, (9, 9), 0)
FilterImg = cv2.Canny(FilterImg, 50, 100)
FilterImg = cv2.dilate(FilterImg, None, iterations=1)
FilterImg = cv2.erode(FilterImg, None, iterations=1)

ContornoImg = cv2.findContours(FilterImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
ContornoImg = grab_contours(ContornoImg)
(ContornoImg, _) = contours.sort_contours(ContornoImg)
colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0))

ContornosAptos = [contorno for contorno in ContornoImg if cv2.contourArea(contorno) < 150]

cv2.drawContours(ChosenImgInitial, ContornosAptos, -1, (0, 255, 0), 3)
# la mayoria de este codigo me base de #https://www.pyimagesearch.com/2016/03/21/ordering-coordinates-clockwise-with-python-and-opencv/
#el primer objeto que agarra es el cuadrado que usaremos de referencia
BigSquare = ContornosAptos[0]
box = cv2.minAreaRect(BigSquare)
box = cv2.boxPoints(box)
box = np.array(box, dtype="int")
(tl, tr, br, bl) = box
Diferencia = euclidean(tl, tr)

Referencia2 = Diferencia / Referencia

print(Diferencia)
print(Referencia2)

for contorno in ContornosAptos:
    box = cv2.minAreaRect(contorno)
    box = cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    box = perspective.order_points(box)
    (tl, tr, br, bl) = box

    horizontal = (tl[0] + int(abs(tr[0] - tl[0]) / 2), tl[1] + int(abs(tr[1] - tl[1]) / 2))
    vertical = (tr[0] + int(abs(tr[0] - br[0]) / 2), tr[1] + int(abs(tr[1] - br[1]) / 2))

    horizontalAdaptado = euclidean(tl, tr) / Referencia2
    verticalAdaptado = euclidean(tr, br) / Referencia2

    cv2.putText(ChosenImgInitial, "{:.0f} cm".format(horizontalAdaptado), (int(horizontal[0] - 15), int(horizontal[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1, (20, 50, 0), 2)
    cv2.putText(ChosenImgInitial, "{:.1f} cm".format(verticalAdaptado), (int(vertical[0] + 10), int(vertical[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (20, 50, 0), 2)

cv2.imshow("Mediciones", ChosenImgInitial)
cv2.waitKey(0)
cv2.destroyAllWindows()


#https://docs.opencv.org/trunk/da/d22/tutorial_py_canny.html
#https://docs.opencv.org/trunk/dd/d49/tutorial_py_contour_features.html
#https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/