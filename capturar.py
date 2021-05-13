import cv2
import os
import imutils

contador = 0 
personName = input()
direccion = 'media' #Cambia a la ruta donde hayas almacenado Data
personita = direccion + '/' + personName

if not os.path.exists(personita):
	print('Carpeta creada: ',personita)
	os.makedirs(personita)


#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
def generar(number):
	nombreArchivo = "media/video"
	nombreArchivo += str(number) + ".mp4"
	#print("Debuggueando -> ",nombreArchivo)
	cap = cv2.VideoCapture(nombreArchivo)
	faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
	#print("aun sigo vivo")
	#contador = 
	global contador
	imagenes = 0
	while True:
		#print("esta pasando algo")
		ok, cuadro = cap.read()
		if ok == False: break
		cuadro =  imutils.resize(cuadro, width=640)
		gray = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)
		auxcuadro = cuadro.copy()

		faces = faceClassif.detectMultiScale(gray,1.3,5)

		for (x,y,w,h) in faces:
			cv2.rectangle(cuadro, (x,y),(x+w,y+h),(0,255,0),2)
			rostro = auxcuadro[y:y+h,x:x+w]
			rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
			cv2.imwrite(personita + '/rostro_{}.jpg'.format(contador),rostro)
			contador +=  1
			imagenes += 1 
		cv2.imshow('cuadro',cuadro)

		k =  cv2.waitKey(1)
		if k == 27 or imagenes >= 500:
			break

	cap.release()
	cv2.destroyAllWindows()


def main():
	for c in range(1,10):
		generar(c)

if __name__ == "__main__":
	main()