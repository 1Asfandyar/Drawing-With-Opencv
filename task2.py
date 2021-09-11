import cv2
import numpy as np

#img = cv2.imread("whiteback.jpg")
#y,x,h=img.shape
img = 255 *np.ones([600,1200,3], dtype=np.uint8)

# first diagram
circle_color = (0,0,255)
line_color = (255,0,0)
text_color = (0,0,0)
font = cv2.FONT_HERSHEY_SIMPLEX


img = cv2.line(img, (325,250), (422,162), line_color, 2)
img = cv2.line(img, (445,150), (530,150), line_color, 2)
img = cv2.line(img, (445,350), (530,350), line_color, 2)
img = cv2.line(img, (625	,265), (540,353), line_color, 2)
img = cv2.line(img, (338,263), (420,343), line_color, 2)
img = cv2.line(img, (625,237), (543,160), line_color, 2)

img = cv2.circle(img,(430,150),15,circle_color,-1)
img = cv2.putText(img,"(0,4)",(430,140),font,0.5,text_color,2,cv2.LINE_AA)

img = cv2.circle(img,(530,150),15,circle_color,-1)
img = cv2.putText(img,"(1,4)",(530,140),font,0.5,text_color,2,cv2.LINE_AA)
img = cv2.circle(img,(330,250),15,circle_color,-1)
img = cv2.putText(img,"(5,4)",(345,240),font,0.5,text_color,2,cv2.LINE_AA)



img = cv2.circle(img,(630,250),15,circle_color,-1)
img = cv2.putText(img,"(1,4)",(580,240),font,0.5,text_color,2,cv2.LINE_AA)
img = cv2.circle(img,(430,350),15,circle_color,-1)
img = cv2.putText(img,"(1,2)",(430,340),font,0.5,text_color,2,cv2.LINE_AA)
img = cv2.circle(img,(530,350),15,circle_color,-1)
img = cv2.putText(img,"(1,3)",(550,340),font,0.5,text_color,2,cv2.LINE_AA)



#first left diagram


img = cv2.circle(img,(630,50),15,circle_color,-1)
img = cv2.putText(img,"(2,3)",(630,30),font,0.5,text_color,2,cv2.LINE_AA)

img = cv2.line(img, (645,50), (730,50), line_color, 2)
img = cv2.line(img, (535,135), (620,60), line_color, 2)
img = cv2.line(img, (645,250), (730,250), line_color, 2)
img = cv2.line(img, (730,50), (830,150), line_color, 2)
img = cv2.line(img, (730,250), (830,150), line_color, 2)

img = cv2.circle(img,(730,50),15,circle_color,-1)
img = cv2.putText(img,"(2,7)",(730,30),font,0.5,text_color,2,cv2.LINE_AA)


img = cv2.circle(img,(730,250),15,circle_color,-1)
img = cv2.putText(img,"(1,7)",(730,230),font,0.5,text_color,2,cv2.LINE_AA)
img = cv2.circle(img,(830,150),15,circle_color,-1)
img = cv2.putText(img,"(0,7)",(850,140),font,0.5,text_color,2,cv2.LINE_AA)



#right 2nd diagrram

img = cv2.circle(img,(630,450),15,circle_color,-1)
img =cv2.putText(img,"(2,0)",(630,430),font,0.5,text_color,2,cv2.LINE_AA)

img = cv2.line(img, (645,450), (730,450), line_color, 2)
img = cv2.line(img, (740,260), (830,350), line_color, 2)
img = cv2.line(img, (830,350), (730,450), line_color, 2)
img = cv2.line(img, (620,440), (540,360), line_color, 2)
img = cv2.circle(img,(730,450),15,circle_color,-1)
img = cv2.putText(img,"(2,9)",(730,430),font,0.5,text_color,2,cv2.LINE_AA)


img = cv2.circle(img,(830,350),15,circle_color,-1)
img = cv2.putText(img,"(5,7)",(850,370),font,0.5,text_color,2,cv2.LINE_AA)


#2nd center diagram

img = cv2.line(img, (620,460), (540,540), line_color, 2)
img = cv2.line(img, (445,550), (515,550), line_color, 2)
img = cv2.line(img, (335,465), (420,543), line_color, 2)
img = cv2.line(img, (335,435), (417,355), line_color, 2)

img = cv2.circle(img,(430,550),15,circle_color,-1)
img = cv2.putText(img,"(8,7)",(450,530),font,0.5,text_color,2,cv2.LINE_AA)

img = cv2.circle(img,(330,450),15,circle_color,-1)
img = cv2.putText(img,"(9,7)",(350,450),font,0.5,text_color,2,cv2.LINE_AA)

img = cv2.circle(img,(530,550),15,circle_color,-1)
img = cv2.putText(img,"(6,7)",(550,550),font,0.5,text_color,2,cv2.LINE_AA)



#righ new



img = cv2.line(img, (845,350), (915,350), line_color, 2)

img = cv2.line(img, (945,155), (1030,250), line_color, 2)


img = cv2.line(img, (943,345), (1030,250), line_color, 2)

img = cv2.circle(img,(930,150),15,circle_color,-1)
img = cv2.putText(img,"(8,7)",(950,140),font,0.5,text_color,2,cv2.LINE_AA)

img = cv2.line(img, (845,150), (915,150), line_color, 2)
img = cv2.circle(img,(930,350),15,circle_color,-1)
img = cv2.putText(img,"(5,0)",(950,370),font,0.5,text_color,2,cv2.LINE_AA)

img = cv2.circle(img,(1030,250),15,circle_color,-1)
img = cv2.putText(img,"(8,0)",(1030,230),font,0.5,text_color,2,cv2.LINE_AA)

#lef side final

img = cv2.line(img, (245,450), (315,450), line_color, 2)

img = cv2.line(img, (245,250), (315,250), line_color, 2)


img = cv2.line(img, (130,350), (240,245), line_color, 2)


img = cv2.line(img, (130,350), (220,443), line_color, 2)

img = cv2.circle(img,(230,450),15,circle_color,-1)
img = cv2.putText(img,"(9,0)",(230,430),font,0.5,text_color,2,cv2.LINE_AA)

img = cv2.circle(img,(230,250),15,circle_color,-1)
img = cv2.putText(img,"(9,1)",(230,230),font,0.5,text_color,2,cv2.LINE_AA)


img = cv2.circle(img,(130,350),15,circle_color,-1)
img = cv2.putText(img,"(9,7)",(70,350),font,0.5,text_color,2,cv2.LINE_AA)
cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()