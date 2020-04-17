import cv2
import numpy as np
ImgTest = cv2.imread('resultado.png', 1)


def ScalateEuclideanTransformation(image, angle, tx, ty, scale):
    center = None
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

    resultEuclidianTranformation = cv2.warpAffine(shifted, rotationMatrix, (w, h))

    return resultEuclidianTranformation


cv2.imshow('ScalatedImagen_euclidiana.png', ScalateEuclideanTransformation(ImgTest, 180, 20, 20, 2))
cv2.imwrite('ScalatedImagen_euclidiana.png', ScalateEuclideanTransformation(ImgTest, 180, 20, 20, 2))
cv2.waitKey(0)
cv2.destroyAllWindows()

