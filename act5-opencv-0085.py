import cv2
import numpy

# 2.1 Ejemplo de código:
# Leer la imagen del archivo
image = cv2.imread('carrorojo.jpg')
# Mostrar la imagen en una ventana
cv2.imshow('2.1 - Original Ricardo Lopez 0085', image)
# Esperar a que se presione una tecla y cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3.1 Ejemplo de código: Convertir una imagen a escala de grises
# Cargar la imagen
image = cv2.imread('carrorojo.jpg')
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Guardar la imagen en escala de grises
cv2.imwrite('gray_carrorojo.jpg', gray_image)
# Mostrar la imagen
cv2.imshow('3.1 - Escala de grises Ricardo Lopez 0085', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4.1 Ejemplo de código: Cambiar el tamaño de la imagen
# Cargar la imagen
image = cv2.imread('carrorojo.jpg')
# Redimensionar la imagen a 300x200
resized_image = cv2.resize(image, (300, 200))
# Guardar la imagen redimensionada
cv2.imwrite('resized_carrorojo.jpg', resized_image)
# Mostrar la imagen
cv2.imshow('4.1 - Redimensionada Ricardo Lopez 0085', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5.1 Ejemplo de código: Girar la imagen 90 grados.
# Cargar la imagen
image = cv2.imread('carrorojo.jpg')
# Obtener la altura y el ancho de la imagen
(h, w) = image.shape[:2]
# Definir el centro de la imagen
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
# Realizar la rotación
rotated_image = cv2.warpAffine(image, matrix, (w, h))
# Guardar la imagen rotada
cv2.imwrite('rotated_carrorojo.jpg', rotated_image)
# Mostrar la imagen
cv2.imshow('5.1 - Rotada 90 grados Ricardo Lopez 0085', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6.1 Ejemplo de código: Aplicación de un desenfoque gaussiano
# Cargar la imagen
image = cv2.imread('carrorojo.jpg')
# Aplicar desenfoque gaussiano
blured_image = cv2.GaussianBlur(image, (15, 15), 0)
# Guardar la imagen desenfocada
cv2.imwrite('blurred_carrorojo.jpg', blured_image)
# Mostrar la imagen
cv2.imshow('6.1 - Desenfoque Gaussiano Ricardo Lopez 0085', blured_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7.1 Ejemplo de código: Detección de bordes mediante el algoritmo de Canny
# Cargar la imagen
image = cv2.imread('carrorojo.jpg')
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Aplicar el detector de bordes Canny
edges = cv2.Canny(gray_image, 100, 200)
# Guardar la imagen de bordes
cv2.imwrite('edgescarrorojo.jpg', edges)
# Mostrar la imagen
cv2.imshow('7.1 - Bordes Canny Ricardo Lopez 0085', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 8.1 Ejemplo de código: Dibujar un rectángulo y añadir texto.
# Cargar la imagen
image = cv2.imread('carrorojo.jpg')
# Dibujar un rectángulo
cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 3)
# Agregar texto a la imagen
cv2.putText(image, 'OpenCV', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
# Guardar la imagen de salida
cv2.imwrite('output_carrorojo.jpg', image)
# Mostrar la imagen
cv2.imshow('8.1 - Rectangulo y texto Ricardo Lopez 0085', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 9.1 Ejemplo de código: Aplicar umbralización binaria
# Cargar la imagen
image = cv2.imread('carrorojo.jpg', 0)
# Aplicar umbralización
_, thresh_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# Guardar la imagen umbralizada
cv2.imwrite('threshold_carrorojo.jpg', thresh_image)
# Mostrar la imagen
cv2.imshow('9.1 - Umbralizacion binaria Ricardo Lopez 0085', thresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 10.1 Ejemplo de código: Detectar contornos y dibujarlos
# Cargar la imagen
image = cv2.imread('carrorojo.jpg')
# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Encontrar bordes
edges = cv2.Canny(gray_image, 100, 200)
# Encontrar contornos
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Dibujar contornos en la imagen original
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# Guardar la imagen de salida con contornos
cv2.imwrite('contours_carrorojo.jpg', image)
# Mostrar la imagen
cv2.imshow('10.1 - Contornos Ricardo Lopez 0085', image)
cv2.waitKey(0)
cv2.destroyAllWindows()