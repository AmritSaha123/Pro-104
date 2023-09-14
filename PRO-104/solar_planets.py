import cv2

img = cv2.imread("solar-system.jpg")
print(img)

cv2.putText(img,"Sun",(16,260),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0,color=(216,56,39))
cv2.putText(img,"Mercury",(80,260),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(216,56,39))
cv2.putText(img,"Venus",(160,290),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(216,56,39))
cv2.putText(img,"Earth",(260,260),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(216,56,39))
cv2.putText(img,"Mars",(370,260),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(216,56,39))
cv2.putText(img,"Jupiter",(540,260),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(216,56,39))
cv2.putText(img,"Saturn",(730,260),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(216,56,39))
cv2.putText(img,"Uranus",(940,260),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(216,56,39))
cv2.putText(img,"Neptune",(1080,260),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(216,56,39))

cv2.imshow("output",img) 
cv2.waitKey(0)