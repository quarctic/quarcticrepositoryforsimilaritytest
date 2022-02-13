from unicodedata import name
import cv2
import numpy as np 
#histogram değerlerinin tutulduğu yer
deger_arrayilk = []

#Histogram adları
histogramadlari= []
#Fotoğraf adları
photo = []

#Üstüne işlem yapılmış histogram değerlerini depolama aracı
finalhistogramvalues = []
while True: 
#Ana fotoğrafın adını alıyor
	anafotograf = input("Enter the name of the main photo:  ")

	x = int(input("Enter how many photos are there"))
	#Fotoğraf listesinin içine fotoğraf adlarını yerleştiriyor
	for i in range(1,x+1):
		a = input("Enter the name of photos")
		photo.append(a)	
	a_string = "histogramk"


	# test image
	saimage = cv2.imread(anafotograf)
	gray_image = cv2.cvtColor(saimage, cv2.COLOR_BGR2GRAY)
	histogram = cv2.calcHist([gray_image], [0],
							None, [256], [0, 256])

	def histogramcreation(x):
			arr = np.array([])
			a_string = "histogramk"
			image = cv2.imread(x)
			gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			numbervariable = photo.index(x)
			numbervariable = numbervariable + 1
			numbervariable = str(numbervariable)
			a_string = a_string.replace("k",numbervariable)
			histogramadlari.append(a_string)
			histogramss = cv2.calcHist([gray_image1], [0],
								None, [256], [0, 256])
			deger_arrayilk.append(histogramss)
	def finals(a):
		c1, c2 = 0, 0
		i = 0
		while i<len(histogram) and i<len(a):
			c1 += (histogram[i]-a[i])**2
			i+= 1
		c1 = c1**(1 / 2)
		finalhistogramvalues.append(c1)	


	for i in photo:
		
		histogramcreation(i)		

	for i in deger_arrayilk:
		finals(i)

	smallest = min(finalhistogramvalues)
	findervariable = finalhistogramvalues.index(smallest)
	print(findervariable)

	
	print("Most similar photo to main photo:  {}".format(photo[findervariable]))
	print("Enter Q for finish the process")
	if cv2.waitKey(0) & 0xFF == ord('q'):
		break
			





