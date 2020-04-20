import cv2
import numpy as np

drawing = False
AddChosenImg = cv2.imread('Pelota2.jpg', 1)
x1, x2, x3, y1, y2, y3 = -1, -1, -1, -1, -1, -1
threePoint = 0


def Draw3PointFuction(event, x, y, flags, param):
    global x1, x2, x3, y1, y2, y3, threePoint, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if threePoint == 0:

            x1, y1 = x, y
        elif threePoint == 1:
            x2, y2 = x, y
        elif threePoint == 2:
            x3, y3 = x, y
        threePoint = threePoint + 1
        cv2.circle(ChosenImgInitial, (x, y), 5, (0, 255, 0), -1)


ChosenImgInitial = cv2.imread('arquero.jpg', 1)
cv2.namedWindow('Inserte 3 puntos')
cv2.setMouseCallback('Inserte 3 puntos', Draw3PointFuction)

while 1:

    cv2.imshow('Inserte 3 puntos', ChosenImgInitial)

    if threePoint == 3:
        # Transformacion afin de la imagen que vamos a adherir
        # sacado de http://acodigo.blogspot.com/2017/07/transformaciones-geometricas.html
        # y https://unipython.com/transformaciones-geometricas-de-imagenes-con-opencv/
       #print(AddChosenImg.shape) 0 height 1 weidht 3 chanel

        rows, cols, ch = AddChosenImg.shape

        pt1 = np.float32([[cols, 0],
                         [0, 0],
                         [0, rows]])

        pt2 = np.float32([[x1, y1],
                          [x2, y2],
                          [x3, y3]])

        Transformation = cv2.getAffineTransform(pt1, pt2)
        resultransformation = cv2.warpAffine(AddChosenImg, Transformation, (AddChosenImg.shape[1],
                                                                            AddChosenImg.shape[0]))

    #pedazos de codigo sacado de :https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html
        test = cv2.imread('arqueroFinal.jpg', cv2.IMREAD_COLOR)
        rows2, cols2, channels = test.shape
        Sticker = resultransformation[0:rows2, 0:cols2]
        img2gray = cv2.cvtColor(Sticker, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        test = cv2.bitwise_and(test, test, mask=mask_inv)

        ImgFinal = cv2.add(test, Sticker)
        cv2.imshow('Result', ImgFinal)

    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
    if k == ord(' '):
        threePoint = 0
        cv2.destroyWindow('Result')
        cv2.destroyWindow('Inserte 3 puntos')
        ChosenImgInitial = cv2.imread('arquero.jpg', 1)
        cv2.namedWindow('Inserte 3 puntos')
        cv2.setMouseCallback('Inserte 3 puntos', Draw3PointFuction)


cv2.destroyAllWindows()


