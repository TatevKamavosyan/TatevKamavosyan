class Point2D:

    def __init__(self,x,y):

        self.x=x
        self.y=y


    def distance(self):
         return(self.x**2+self.y**2)**0.5

    def __add__(self,other):
         return (self.x+other.x,self.y+other.y)

    def __sub__(self,other):

         return (self.x-other.x,self.y-other.y)

    def __neg__(self):
         return(-self.x,-self.y)        

    

if __name__=='__main__':


    p1=Point2D(12,11)
    p2=Point2D(-9,24)

    print(p1+p2)
    print(p1-p2)
    print(-p2)
    
    
    print('Distanse from center of coordinates:{:.2f}'.format(p1.distance()))
    print('Distanse from center of coordinates:{:.2f}'.format(p2.distance()))
