import cv2
import numpy as np

drawing = False
x1, x2, x3, x4, y1, y2, y3, y4 = -1, -1, -1, -1, -1, -1, -1, -1
fourPoint = 0

def Draw4PointFuction(event, x, y, flags, param):
    global x1, x2, x3, y1, y2, y3, x4, y4, fourPoint, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(ChosenImgInitial, (x, y), 5, (0, 255, 0), -1)
        drawing = False
        if fourPoint == 0:
            x1, y1 = x, y
        elif fourPoint == 1:
            x2, y2 = x, y
        elif fourPoint == 2:
            x3, y3 = x, y
        elif fourPoint == 3:
            x4, y4 = x, y
        fourPoint = fourPoint + 1



ChosenImgInitial = cv2.imread('Wally.jpg', 1)
cv2.namedWindow('Inserte 4 puntos')
cv2.setMouseCallback('Inserte 4 puntos', Draw4PointFuction)

while 1:

    cv2.imshow('Inserte 4 puntos', ChosenImgInitial)

    if fourPoint == 4:
#Pagina de ayuda
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html

        rows, cols, ch = ChosenImgInitial.shape

        ChosenPoints = np.float32([[x1, y1],
                          [x2, y2],
                          [x3, y3],
                          [x4, y4]])

        pt1 = np.float32([[0, 0],
                          [cols, 0],
                          [cols, rows],
                          [0, rows]])



        Transformation = cv2.getPerspectiveTransform(ChosenPoints, pt1)
        resultransformation = cv2.warpPerspective(ChosenImgInitial, Transformation, (ChosenImgInitial.shape[1],
                                                                            ChosenImgInitial.shape[0]))


        cv2.imshow('Result', resultransformation)

    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
    if k == ord(' '):
        fourPoint = 0
        cv2.destroyWindow('Result')
        cv2.destroyWindow('Inserte 4 puntos')
        ChosenImgInitial = cv2.imread('Wally.jpg', 1)
        cv2.namedWindow('Inserte 4 puntos')
        cv2.setMouseCallback('Inserte 4 puntos', Draw4PointFuction)


cv2.destroyAllWindows()