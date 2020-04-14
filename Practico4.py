import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Tambien puede ser
#width2 = int(cap.get(3))
#height2 = int(cap.get(4))
#print('width, height:{0}, {1} o width, height: {2}, {3}'.format(width, height, width2, height2))

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord ('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()