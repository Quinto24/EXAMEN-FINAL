import cv2

def aplicar_suavizado(ruta_imagen):
    imagen = cv2.imread(\Desktop\EXAMEN DE PDI\HD.jpeg)

    
    imagen = cv2
    imagen_suavizada = cv2.GaussianBlur(imagen, (
    imagen_suavizada = cv2.GaussianBl

    imagen_suaviza
5, 5), 0)

    cv2.imwrite(
    cv2.im
'imagen_suavizada.jpg', imagen_suavizada)
    cv2.imshow(
    cv2.ims

   
'Imagen Suavizada', imagen_suavizada)
    cv2.waitKey(
    cv2.waitKey

    cv2.wa

    c
0)
    cv2.destroyAllWindows()


    cv2.destroyAllWindows

    cv2.destroyAllWin

    cv2.destroyA

    cv2.des

    cv

 
aplicar_suavizado(
aplicar_suavizado(

aplicar_suaviz

aplicar_su

aplica

ap
'\Desktop\EXAMEN DE PDI\HD.jpeg')