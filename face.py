from typing import final
import cv2
import dlib



def findfaces(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hog_face_detector = dlib.get_frontal_face_detector()
    dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    faces = hog_face_detector(gray)
    print("Number of faces detected: ", len(faces))
    result = []
    for face in faces:
        face_landmarks = dlib_facelandmark(gray, face)
        result.append(Face(face,face_landmarks))

    return result

class Face( ):

    # final stander scale = 623
    def calEYE(self,L,R):
        x = round((self.landmarks.part(L).x + self.landmarks.part(R).x)/2)
        y = round((self.landmarks.part(L).y + self.landmarks.part(R).y)/2)
        return [x,y]

    def __init__(self,arg_location,arg_landmarks):
        self.location = arg_location
        self.landmarks = arg_landmarks
        self.lefteye = self.calEYE(37,40)
        self.righteye = self.calEYE(43,46)
        
        self.chin = [self.landmarks.part(9).x , self.landmarks.part(9).y]

    def array_mid(self, a,b):
        return [round((a[0]+b[0])/2) , round((a[1]+b[1])/2)]
    
    def array_diff_y(self,a,b,c=0):
        return [round((a[0]*2-b[0])) ,round( a[1] + (a[1]-b[1])*(1+c) ) ]

    def getscale(self):
        eye_mid = self.array_mid(self.lefteye , self.righteye)
        return round((self.chin[1]-eye_mid[1])*100/623)

    def gethat(self):
        # return self.array_mid(self.lefteye , self.righteye)
        return self.array_diff_y(self.array_mid(self.lefteye , self.righteye) , self.chin)

    def gethat_offset(self, arg_int):
        return self.array_diff_y(self.array_mid(self.lefteye , self.righteye) , self.chin,arg_int)

    # testing
    def getlandmarks(self):
        return self.landmarks

    def test (self):
        print(self.chin,self.lefteye,)

    def __str__(self) -> str:
        return self.chin,self.lefteye
        
        
        
