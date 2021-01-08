from tkinter import *
import cv2
import time
import numpy
import glob

class ClickCircleF:
    
    def __init__(self):
        
        
        self.circle = None
        self.dataset = None
        self.file_to_fill = None
        
        # we load all the data in the data directory
        try:
            self.dataset = glob.glob("./*.csv")
        except:
            self.dataset = None
        
        #we save a dictionary with: keys: the filename, values the dimension
        self.dataset_dimension = {}
        length = 0
        if self.dataset != None:
            length = len(self.dataset)
        
        for i in range(length):
            #s will be like firstdimension_seconddimension_thirddimension
            s = self.dataset[i][self.dataset[i].find('./data/')+len('./data/'):self.dataset[i].find('.csv')]
            self.dataset_dimension[self.dataset[i]] = s.split('_')
        # lets connect the camera with opencv
        self.camera = None
        try:
            self.camera = cv2.VideoCapture(0)
        except:
            print("Error: you have no camera connected")
            exit(1)
        
        # take the dimensions from the current camera
        return_value, image = self.camera.read()
        #image = [480][640][3], rows, cols, channels (colours) with my default camera
        n_dim = image.ndim
        rows = 0
        cols = 0
        channels = 0
        for i in range(n_dim):
            if i == 0:
                rows = len(image)
            elif i == 1:
                cols = len(image[0])
            else:
                channels = len(image[0][0])
        temp = [str(rows),str(cols),str(channels)]
        for i in self.dataset_dimension.keys():
            if self.dataset_dimension[i] == temp:
                self.file_to_fill = i
                break
        if self.file_to_fill == None:
            self.file_to_fill = "./data/"+str(rows)+"_"+str(cols)+"_"+str(channels)+".csv"
            
        # create root set to full screen
        self.root = Tk()
        self.root.title("Create Circles")
        self.root.attributes('-fullscreen', True)
        
        #add canvas to root and set to full screen too (background black)
        self.myCanvas = Canvas(self.root)
        self.myCanvas.configure(background='black')
        self.myCanvas.pack(fill=BOTH, expand=True)
        
        # add an exit button on canvas
        self.exit_button = self.myCanvas.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
        self.txt_button = self.myCanvas.create_text(50, 15, text="Close")
        self.myCanvas.tag_bind(self.exit_button, "<Button-1>", self.clicked) ## when the square is clicked runs function "clicked".
        self.myCanvas.tag_bind(self.txt_button, "<Button-1>", self.clicked) ## same, but for the text.
        
        #got the screen dimensions
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        #current x and y to save
        self.x = 0
        self.y = 0
        
        self.generate_x_y()
        self.create_circle(self.x,self.y,5,"white","white")
        self.run()
        
    def generate_x_y(self):
        self.x = int(numpy.random.uniform(100, self.screen_width, 1))  
        self.y = int(numpy.random.uniform(30, self.screen_height, 1))
        
    def create_circle(self, x, y, r, outline_colour, fill_colour): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        self.circle = self.myCanvas.create_oval(x0, y0, x1, y1,outline=outline_colour,fill=fill_colour)
        self.myCanvas.tag_bind(self.circle,"<Button-1>",self.circle_clicked)
        return self.circle
    
    def circle_clicked(self,event):
        # unbind the circle with the event
        self.myCanvas.tag_unbind(self.circle,"<Button-1>")
        #capture with the camera you image
        return_value, image = self.camera.read()
        #image = [480][640][3], rows, cols, channels (colours) with my default camera
        #set the dimensions
        n_dim = image.ndim
        rows = 0
        cols = 0
        channels = 0
        for i in range(n_dim):
            if i == 0:
                rows = len(image)
            elif i == 1:
                cols = len(image[0])
            else:
                channels = len(image[0][0])
        #save the data in the file
        f = open(self.file_to_fill,'a+')
        for i in range(rows):
            for j in range(cols):
                for k in range(channels):
                    f.write(str(image[i][j][k])+';')
                if channels == 0:
                    f.write(str(image[i][j])+';')
        
        f.write(str(self.x)+';'+str(self.y)+';\n')
        f.close() 
        time.sleep(2)
        self.myCanvas.delete(self.circle)
        self.generate_x_y()
        self.create_circle(self.x,self.y,5,"white","white")
        
        
    def run(self):
        self.root.mainloop()
    
    def clicked(self,event):
        try:
            del(self.camera)
        except:
            print("can't execute del(self.camera)")
        self.root.quit()



