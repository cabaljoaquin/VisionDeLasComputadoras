import cv2


drawing = False  # true if mouse is pressed
ChosenImg = cv2.imread('resultado.png', 1)
CutImg = cv2.imread('resultado.png', 1)
XStart, XEnd, YStart, YEnd = -1, -1, -1, -1


def draw_rectangle(event, x, y,  flags, param):
    global XStart, YStart, XEnd, YEnd, drawing, ChosenImg, CutImg
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        XStart, YStart = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            cv2.rectangle(ChosenImg, (XStart, YStart), (x, y), (0, 255, 0), 0)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        XEnd, YEnd = x, y
        CutImg = CutImg[YStart:YEnd, XStart:XEnd]
        cv2.rectangle(ChosenImg, (XStart, YStart), (x, y), (0, 255, 0), 0)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)
while 1:
    cv2.imshow('image', ChosenImg)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('g'):
        cv2.imwrite('RecortePractico5.png', CutImg)
        break
    if k == ord('r'):
        CutImg = cv2.imread('resultado.png', 1)
        ChosenImg = cv2.imread('resultado.png', 1)
    elif k == ord('q'):
        break


cv2.destroyAllWindows()