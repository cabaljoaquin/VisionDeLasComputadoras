import cv2

img = cv2.imread('hoja.png', 0)
print(img)
for array in img:
    for index in range(0, len(array)):
        if array[index] > 220:
            array[index] = 255
        else:
            array[index] = 0


print(img)
cv2.imwrite('resultado.png', img)
