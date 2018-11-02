import cv2 #подключение библиотеки OpenCV

img = cv2.imread("lego_flash.jpeg")  #в переменную(массив) img выгружаем картинку lion.jpg

print(img.shape) #выводим размер картинки

img[250:350,400:500]=(0,0,255)   #квадрат штриной 100х100 рисуем в центре экрана
img2=cv2.resize(img,(400,400))  #изменяем размер

crop_img=img[100:170, 200:260]

#отразим изображение по горизонтали
flip_image = cv2.flip(img,1)
cv2.imshow("Flip image", flip_image)

cv2.imshow("cropped", crop_img)

cv2.imshow("name img",img)  #создаем окно с картинкой из переменной img (заголовок окна name img)
cv2.imshow("name img2",img2)#создаем окно с картинкой из переменной img2 (заголовок окна name img2)

cv2.waitKey(0)  #ожидание нажатия любой клавиши
cv2.destroyAllWindows()#закрывает все открытые окна