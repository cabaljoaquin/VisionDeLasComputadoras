###################################################################################################################
##########################  Si da error correr los siguientes comandos en la consola  #############################
#############################       pip install opencv-python==3.4.2.16               #############################
#############################       pip install opencv-contrib-python==3.4.2.16       #############################
###################################################################################################################

# Basado en el practico 12 y
# https://medium.com/@dagorik/detectar-similitudes-de-dos-im%C3%A1genes-con-python-y-opencv-cf5bb8b0fbf9

#Este algoritmo es bueno cuando buscamos tener similitudes en color y forma dado que aqui  tenemos imagenes iguales pero
# movidas entre si no veo necesario trabajarlas para igualar los canales de color una opcion valida tambien seria
# pasarlos a una escala de grises
#Gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#Gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
import cv2
import numpy as np

MIN_MATCH_COUNT = 10

img1 = cv2.imread('Img1.jpeg')
img2 = cv2.imread('Img2.jpeg')

# Inicializamos el detector y el descriptor
dscr = cv2.xfeatures2d.SIFT_create()
kp1, des1 = dscr.detectAndCompute(img1, None)
kp2, des2 = dscr.detectAndCompute(img2, None)

matcher = cv2.BFMatcher(cv2.NORM_L2)

matches = matcher.knnMatch(des1, des2, k=2)

# Guardamos los buenos matches usando el test de razón de Lowe
good = [ ]
for m, n in matches :
    if m.distance < 0.70*n.distance:
        good.append(m)

if(len(good) > MIN_MATCH_COUNT):
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

H, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)  # Computamos la homografía con RANSAC

wimg2 = cv2.warpPerspective(img2, H, (img1.shape[1], img1.shape[0]))

# Mezclamos ambas imágenes
alpha = 0.5
blend = np.array(wimg2 * alpha + img1 * (1 - alpha), dtype=np.uint8)
result = cv2.drawMatches(img1, kp1, img2, kp2, good, None)
cv2.imshow("Alineacion de imagenes", cv2.resize(result, None, fx = 0.4, fy=0.4))
cv2.imwrite("Comparacion.jpg", result)



cv2.waitKey(0)
cv2.destroyAllWindows()