import cv2

# 1. Cargar la imagen original
image = cv2.imread('keniaos.png')

# Reducir la original al 50% para que no salga gigante en pantalla
small_original = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# 2. Convertir a escala de grises (y reducirla al 50% para mostrarla)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
small_gray = cv2.resize(gray_image, (0, 0), fx=0.5, fy=0.5)

# 3. Redimensionar a un tamaño fijo pequeño (150x100)
resized_image = cv2.resize(image, (150, 100))

# --- MOSTRAR LAS 3 VENTANAS EN PANTALLA ---
cv2.imshow('1. Original - jose solis 1472', small_original)
cv2.imshow('2. Escala de grises - jose solis 1472', small_gray)
cv2.imshow('3. Redimensionada - jose solis 1472', resized_image)

# --- GUARDAR LAS IMAGENES MODIFICADAS ---
cv2.imwrite('gray_keniaos.png', gray_image)
cv2.imwrite('resized_keniaos.png', resized_image)

# Esperar a que presiones cualquier tecla para cerrar todas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()


image = cv2.imread('keniaos.png')
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_image = cv2.warpAffine(image, matrix, (w, h))

small_rotated = cv2.resize(rotated_image, (0, 0), fx=0.5, fy=0.5)

cv2.imshow('Imagen rotada 90 grados - jose solis 1472', small_rotated)
cv2.imwrite('rotated_keniaos.png', rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('keniaos.png')
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Reducir al 50% para mostrar en pantalla
small_blurred = cv2.resize(blurred_image, (0, 0), fx=0.5, fy=0.5)

cv2.imshow('Desenfoque Gaussiano - jose solis 1472', small_blurred)
cv2.imwrite('blurred_keniaos.png', blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('keniaos.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 100, 200)

# Reducir al 50% para mostrar en pantalla
small_edges = cv2.resize(edges, (0, 0), fx=0.5, fy=0.5)

cv2.imshow('Bordes Canny - jose solis 1472', small_edges)
cv2.imwrite('edges_keniaos.png', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('keniaos.png')
cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 3)
cv2.putText(image, 'OpenCV', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Reducir al 50% para mostrar en pantalla
small_output = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

cv2.imshow('Rectangulo y Texto - jose solis 1472', small_output)
cv2.imwrite('output_keniaos.png', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('keniaos.png', 0)
_, thresh_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Reducir al 50% para mostrar en pantalla
small_thresh = cv2.resize(thresh_image, (0, 0), fx=0.5, fy=0.5)

cv2.imshow('Umbralizacion (Threshold) - jose solis 1472', small_thresh)
cv2.imwrite('threshold_keniaos.png', thresh_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

image = cv2.imread('keniaos.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 100, 200)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Reducir al 50% para mostrar en pantalla
small_contours = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

cv2.imshow('Contornos - jose solis 1472', small_contours)
cv2.imwrite('contours_keniaos.png', image)

cv2.waitKey(0)
cv2.destroyAllWindows()