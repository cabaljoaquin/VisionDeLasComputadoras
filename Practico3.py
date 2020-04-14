import sys
import cv2

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print('Pass a filename as first argument')
    sys.exit(0)

cap = cv2.VideoCapture(filename)

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #prueba = cap.get(5)# Encotrado en internet, me devuelve los mismos fps y la funcion cap de fps sin el get te devuelve 5

    #agregue el int adelante para convertirlo por que el waitkey espera entero
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    cv2.imshow(' frame ', gray)
    if(cv2.waitKey(23) & 0xFF) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()