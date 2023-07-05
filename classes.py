class magari:
    def __init__(self,modelname,color,year,cc):
        self.model=modelname
        self.mycolor=color
        self.myyear=year
        self.capacity=cc
    def onyesha(self):
        print(self.model,self.mycolor,self.myyear,self.capacity)
# create now an object
object1=magari("toyota","white",2020,1500)
object1.onyesha()
object2=magari("nissan","white",1990,"2000")
object2.onyesha()