import cv2
import numpy as np
ImgTest = cv2.imread('resultado.png', 1)


def EuclideanTransformation(image, angle, tx, ty, center=None, scale=1.0):
#Comienzo de traslacion de imagen
    (h, w) = (image.shape[0], image.shape[1])

    translationMatrix = np.float32([[1, 0, tx],
                                    [0, 1, ty]])
    shifted = cv2.warpAffine(image, translationMatrix, (w, h))

#Comienzo de rotacion de la imagen
    (h, w) = image.shape[: 2]
    if center is None:
       center = (w/2, h/2)

    rotationMatrix = cv2.getRotationMatrix2D(center, angle, scale)

    #no entido por que no funciona esto que comente, pense que por algun problema de w y h aunque prove varios
    #rotated = cv2.warpAffine(image, rotationMatrix, (w, h))
    #resultEuclidianTranformation = cv2.warpAffine(shifted, rotated, (w, h))

    resultEuclidianTranformation = cv2.warpAffine(shifted, rotationMatrix, (w, h))

    return resultEuclidianTranformation


cv2.imshow('Imagen_euclidiana.png', EuclideanTransformation(ImgTest, 45, 20, 20))
cv2.imwrite('Imagen_euclidiana.png', EuclideanTransformation(ImgTest, 45, 20, 20))
cv2.waitKey(0)
cv2.destroyAllWindows()

#fuerte de ayuda : https://stackoverrun.com/es/q/2355801