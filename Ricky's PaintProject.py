#paintProject.py

from math import*
from pygame import*
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

#Displaying screen size and caption of the program and mouse positions.
screen = display.set_mode((1300,825))
display.set_caption("League of Legends Paint")
mx,my = mouse.get_pos()

#This is for getting the filenames.
root = Tk() 
root.withdraw()

#Putting the images onto the screen and changing some of the picture sizes.
pic1 = image.load("Fiddlestick.jpg")
bigback = transform.scale(pic1,(1300,875))
screen.blit(bigback,(0,-50))
pic2 = image.load("pencil.jpg")
screen.blit(pic2,(30,630))
pic3 = image.load("eraser.jpg")
screen.blit(pic3,(95,630))
pic4 = image.load("line.gif")
screen.blit(pic4,(225,630))
pic5 = image.load("oval.png")
screen.blit(pic5,(290,630))
pic6 = image.load("save_icon.png")
screen.blit(pic6,(355,750))
pic7 = image.load("open-file-icon.png")
screen.blit(pic7,(420,750))
pic8 = image.load("palette.jpg")
smallColWheel = transform.scale(pic8,(200,200))
screen.blit(smallColWheel,(1100,630))
pic9 = image.load("Clear Button.jpg")
clearButton = transform.scale(pic9,(50,50))
screen.blit(clearButton,(485,750))
pic10 = image.load("Rectangle.png")
smallRectangle = transform.scale(pic10,(50,50))
screen.blit(smallRectangle,(355,630))
pic11 = image.load("Polygon Pic.png")
bigPoly = transform.scale(pic11,(50,50))
screen.blit(bigPoly,(420,630))
pic12 = image.load("fillword.png")
fillword = transform.scale(pic12,(50,50))
screen.blit(fillword,(485,630))
pic13 = image.load("unfillword.png")
unfillword = transform.scale(pic13,(50,50))
screen.blit(unfillword,(550,630))
pic14 = image.load("Undo Icon.png")
undoPic = transform.scale(pic14,(50,50))
screen.blit(undoPic,(550,750))
pic15 = image.load("Redo Icon.png")
redoPic = transform.scale(pic15,(50,50))
screen.blit(redoPic,(615,750))
pic16 = image.load("Paintbrush.png")
smallBrush = transform.scale(pic16,(50,50))
screen.blit(smallBrush,(160,630))
pic17 = image.load("unpause-button.jpg")
unpausePic = transform.scale(pic17,(70,70))
screen.blit(unpausePic,(915,655))
pic18 = image.load("pause-button.jpg")
pausePic = transform.scale(pic18,(70,70))
screen.blit(pausePic,(1000,655))
pic19 = image.load("restart-button.jpg")
restartPic = transform.scale(pic19,(70,70))
screen.blit(restartPic,(915,740))
pic20 = image.load("eyedropper.png")
sEyeDropperPic = transform.scale(pic20,(50,50))
screen.blit(sEyeDropperPic,(615,630))

#Putting stamps onto the screen and changing the sizes of them.
sticker1 = image.load("dragonblade_talon.png")
sSticker1 = transform.scale(sticker1,(200,200))
screen.blit(sSticker1,(695,200)) 
sticker2 = image.load("glacial_malphite.png")
sSticker2 = transform.scale(sticker2,(200,200))
screen.blit(sSticker2,(895,200))
sticker3 = image.load("Hecarim-Reaper.png")
sSticker3 = transform.scale(sticker3,(200,200))
screen.blit(sSticker3,(1095,200))
sticker4 = image.load("hired_gun_lucian.png")
sSticker4 = transform.scale(sticker4,(200,200))
screen.blit(sSticker4,(1095,10))
sticker5 = image.load("Renekton-Bloodfury.png")
sSticker5 = transform.scale(sticker5,(200,200))
screen.blit(sSticker5,(695,390))
sticker6 = image.load("special_forces_gangplank.png")
sSticker6 = transform.scale(sticker6,(200,200))
screen.blit(sSticker6,(895,390))
sticker7 = image.load("Taric-Bloodstone.png")
sSticker7 = transform.scale(sticker7,(200,200))
screen.blit(sSticker7,(1095,390))
sticker8 = image.load("Aatrox-Justicar.png")
sSticker8 = transform.scale(sticker8,(200,200))
screen.blit(sSticker8,(695,580))

#This is the white canvas and a black box around it.
draw.rect(screen,(0,0,0),(21,21,658,583))
draw.rect(screen,(255,255,255),(25,25,650,575))

#This loads the music and plays the music.
init()
mixer.music.load("Imagine Dragon - Worriors.mp3")
mixer.music.play(-1)

#These are variable used later.
message = ""
col = (0,0,0)
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)
start = 0,0
size = 10
polylist = []
tool = "pencil"
filltool = "fill"
musictool = "unpause"
newsize = 0
undo = []
redo = []
oldmx = 0
oldmy = 0

#These are the boxes for the pictures and highlighting boxes.
pencilRect = Rect(30,630,50,50)
pencilRect1 = Rect(28,628,54,54)
eraserRect = Rect(95,630,50,50)
eraserRect1 = Rect(93,628,54,54)
brushRect = Rect(160,630,50,50)
brushRect1 = Rect(158,628,54,54)
lineRect = Rect(225,630,50,50)
lineRect1 = Rect(223,628,54,54)
ovalRect = Rect(290,630,50,50)
ovalRect1 = Rect(288,628,54,54)
saveRect = Rect(355,750,50,50)
saveRect1 = Rect(353,748,54,54)
openRect = Rect(420,750,50,50)
openRect1 = Rect(418,748,54,54)
clearRect = Rect(485,750,50,50)
clearRect1 = Rect(483,748,54,54)
polyRect = Rect(420,630,50,50)
polyRect1 = Rect(418,628,54,54)
rectangleRect = Rect(355,630,50,50)
rectangleRect1 = Rect(353,628,54,54)
dropperRect = Rect(615,630,50,50)
dropperRect1 = Rect(613,628,54,54)
fillwordRect = Rect(485,630,50,50)
fillwordRect1 = Rect(483,628,54,54)
unfillwordRect = Rect(550,630,50,50)
unfillwordRect1 = Rect(548,628,54,54)
undoRect = Rect(550,750,50,50)
undoRect1 = Rect(548,748,54,54)
redoRect = Rect(615,750,50,50)
redoRect1 = Rect(613,748,54,54)
canvas = Rect(25,25,650,575)
screen1 = Rect(0,0,1300,825)
colPalette = Rect(1100,625,200,200)
sizebox = Rect(1015,755,70,70)

#These are the boxes for the stickers and the highlighting boxes.
talonRect = Rect(695,200,200,200)
talonRect1 = Rect(695,205,195,175)
malphiteRect = Rect(895,200,200,200)
malphiteRect1 = Rect(895,205,195,175)
hecarimRect = Rect(1095,200,200,200)
hecarimRect1 = Rect(1095,205,195,175)
lucianRect = Rect(1095,5,200,200)
lucianRect1 = Rect(1095,10,195,175)
renektonRect = Rect(695,395,200,200)
renektonRect1 = Rect(695,400,195,175)
gangplankRect = Rect(895,395,200,200)
gangplankRect1 = Rect(895,400,195,175)
taricRect = Rect(1095,395,200,200)
taricRect1 = Rect(1095,400,195,175)
aatroxRect = Rect(695,580,200,200)
aatroxRect1 = Rect(695,585,195,175)

#These are the music boxes and the highlighting boxes.
unpauseRect = Rect(915,655,70,70)
unpauseRect1 = Rect(913,653,74,74)
pauseRect = Rect(1000,655,70,70)
pauseRect1 = Rect(998,653,74,74)
restartRect = Rect(915,740,70,70)
restartRect1 = Rect(913,738,74,74)

#This is to show you the colour.
draw.rect(screen,(col),(1085,610,665,565))
screen.blit(smallColWheel,(1100,625))

running = True
while running:
    click = False
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONUP:
           if e.button == 1 and saveRect.collidepoint((mx,my)):
               fileName = asksaveasfilename(parent=root,title="Save the image as...") #This ask for the filname.
               if fileName != "":
                   image.save(screen.subsurface(canvas),"%s.png"%(fileName)) #This saves the image as a png file.
           if e.button == 1 and openRect.collidepoint((mx,my)):
               fileName = askopenfilename(parent=root,title="Open Image:") #This ask for the filename.
               if fileName != "":
                   picture = image.load("%s" %(fileName)) #This loads the image they pick.
                   screen.set_clip(canvas)
                   screen.blit(picture,(25,25)) #This puts the image on the screen at positions (25,25).
                   screen.set_clip(None)
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 4:
               size += 1 #This increases the size when scrolling up.
               if size > 25: #This caps the size to 25 max.
                   size = 25
            elif e.button == 5:
               size -= 1 #This decreases the size when scrolling down.
               if size < 1: #the smalliest size is 1 which is the minimum size.
                   size = 1
            else:
                start = e.pos #The position when first clicked.
                startx,starty = e.pos #The mx and my position when first clicked.
                copy = screen.copy() #Copies the screen.
                stickercopy = screen.copy() #Copies the screen for stickers.
              
        if e.type == MOUSEBUTTONDOWN and canvas.collidepoint((mx,my)):
           copycanvas = screen.subsurface(canvas).copy() #Copies the canvas.
           undo.append(copycanvas) #It adds the canvas to the list.
           redo = [] #Makes the redo to nothing.
        if e.type == MOUSEBUTTONUP and undoRect.collidepoint(mx,my):
            if len(undo) > 0:
                redoCopy = screen.subsurface(canvas).copy() #Copies the screen for redo.
                redo.append(redoCopy) #Adds the copied screen into the redo list.
                screen.blit(undo[-1],(25,25)) #This then puts the last thing in the undolist onto the screen.
                undo.pop() #This takes the lst thing in the undo list out.
        if e.type == MOUSEBUTTONUP and redoRect.collidepoint(mx,my):
            if len(redo) > 0:
                copycanvas = screen.subsurface(canvas).copy() #Copies the canvas.
                undo.append(copycanvas) #Adds it to the undo list.
                screen.blit(redo[-1],(25,25)) #puts the last item in the redo list onto the canvas.
                redo.pop() #Takes out the last thing in the redo list.

        #This is the mouse positions and what the three mouse button is.    
        mb = mouse.get_pressed()
        mx,my = mouse.get_pos()
        
        #This is the box that shows the size with the size of a circle.
        screen.set_clip(sizebox)
        draw.rect(screen,white,sizebox)
        draw.circle(screen,black,(1050,790),size)
        screen.set_clip(None)

        #This will get the colour from the pallete.
        if colPalette.collidepoint((mx,my)) and mb[0] == 1:
            col = screen.get_at((mx,my))
            draw.rect(screen,(col),(1085,610,665,565))
            screen.blit(smallColWheel,(1100,625))

        #This will either put a green box or black box around the tool, depending if the tool is active or not.
        if tool == "pencil":
            draw.rect(screen,green,pencilRect1)
        elif tool != "pencil":
            draw.rect(screen,black,pencilRect1)    
        if tool == "eraser":
            draw.rect(screen,green,eraserRect1)
        elif tool != "eraser":
            draw.rect(screen,black,eraserRect1)
        if tool == "brush":
            draw.rect(screen,green,brushRect1)
        elif tool != "brush":
            draw.rect(screen,black,brushRect1)
        if tool == "line":
            draw.rect(screen,green,lineRect1)
        elif tool != "line":
            draw.rect(screen,black,lineRect1)
        if tool == "oval":
            draw.rect(screen,green,ovalRect1)
        elif tool != "oval":
            draw.rect(screen,black,ovalRect1)
        if tool == "save":
            draw.rect(screen,green,saveRect1)
        elif tool != "save":
            draw.rect(screen,black,saveRect1)
        if tool == "open":
            draw.rect(screen,green,openRect1)
        elif tool != "open":
            draw.rect(screen,black,openRect1)
        if tool == "clear":
            draw.rect(screen,green,clearRect1)
        elif tool != "clear":
            draw.rect(screen,black,clearRect1)
        if tool == "rectangle":
            draw.rect(screen,green,rectangleRect1)
        elif tool != "rectangle":
            draw.rect(screen,black,rectangleRect1)
        if tool == "polygon":
            draw.rect(screen,green,polyRect1)
        elif tool != "polygon":
            draw.rect(screen,black,polyRect1)
        if tool == "dropper":
            draw.rect(screen,green,dropperRect1)
        elif tool != "dropper":
            draw.rect(screen,black,dropperRect1)
        if tool == "talon":
            draw.rect(screen,green,talonRect1)
        elif tool != "talon":
            draw.rect(screen,black,talonRect1)        
        if tool == "malphite":
            draw.rect(screen,green,malphiteRect1)
        elif tool != "malphite":
            draw.rect(screen,black,malphiteRect1) 
        if tool == "hecarim":
            draw.rect(screen,green,hecarimRect1)
        elif tool != "hecarim":
            draw.rect(screen,black,hecarimRect1)
        if tool == "lucian":
            draw.rect(screen,green,lucianRect1)
        elif tool != "lucian":
            draw.rect(screen,black,lucianRect1)
        if tool == "renekton":
            draw.rect(screen,green,renektonRect1)
        elif tool != "renekton":
            draw.rect(screen,black,renektonRect1)
        if tool == "gangplank":
            draw.rect(screen,green,gangplankRect1)
        elif tool != "gangplank":
            draw.rect(screen,black,gangplankRect1)
        if tool == "taric":
            draw.rect(screen,green,taricRect1)
        elif tool != "taric":
            draw.rect(screen,black,taricRect1)
        if tool == "aatrox":
            draw.rect(screen,green,aatroxRect1)
        elif tool != "aatrox":
            draw.rect(screen,black,aatroxRect1)

        #This will put a red or black box around the filltool, depending on if the filltool is active or not.
        if filltool == "unfill":
            draw.rect(screen,red,unfillwordRect1)
        elif filltool != "unfill":
            draw.rect(screen,black,unfillwordRect1)
        if filltool == "fill":
            draw.rect(screen,red,fillwordRect1)
        elif filltool != "fill":
            draw.rect(screen,black,fillwordRect1)

        #This will put a blue or black box around the musictool, depending on if the musictool is active or not.
        if musictool == "unpause":
            draw.rect(screen,blue,unpauseRect1)
        elif musictool != "unpause":
            draw.rect(screen,black,unpauseRect1)
        if musictool == "pause":
            draw.rect(screen,blue,pauseRect1)
        elif musictool != "pause":
            draw.rect(screen,black,pauseRect1)
        if musictool == "restart":
            draw.rect(screen,blue,restartRect1)
        elif musictool != "restart":
            draw.rect(screen,black,restartRect1)

        #This will highlight the music tool, filltool or tool that you are hovering your mouse over. 
        if pencilRect.collidepoint(mx,my):
            draw.rect(screen,green,pencilRect1)
        if eraserRect.collidepoint(mx,my):
            draw.rect(screen,green,eraserRect1)
        if brushRect.collidepoint(mx,my):
            draw.rect(screen,green,brushRect1)
        if lineRect.collidepoint(mx,my):
            draw.rect(screen,green,lineRect1)
        if ovalRect.collidepoint(mx,my):
            draw.rect(screen,green,ovalRect1)
        if saveRect.collidepoint(mx,my):
            draw.rect(screen,green,saveRect1)
        if openRect.collidepoint(mx,my):
            draw.rect(screen,green,openRect1)
        if clearRect.collidepoint(mx,my):
            draw.rect(screen,green,clearRect1)
        if rectangleRect.collidepoint(mx,my):
            draw.rect(screen,green,rectangleRect1)
        if polyRect.collidepoint(mx,my):
            draw.rect(screen,green,polyRect1)
        if fillwordRect.collidepoint(mx,my):
            draw.rect(screen,red,fillwordRect1)
        if unfillwordRect.collidepoint(mx,my):
            draw.rect(screen,red,unfillwordRect1)
        if dropperRect.collidepoint(mx,my):
            draw.rect(screen,green,dropperRect1)
        if talonRect.collidepoint(mx,my):
            draw.rect(screen,green,talonRect1)
        if malphiteRect.collidepoint(mx,my):
            draw.rect(screen,green,malphiteRect1)
        if hecarimRect.collidepoint(mx,my):
            draw.rect(screen,green,hecarimRect1)
        if lucianRect.collidepoint(mx,my):
            draw.rect(screen,green,lucianRect1)
        if renektonRect.collidepoint(mx,my):
            draw.rect(screen,green,renektonRect1)
        if gangplankRect.collidepoint(mx,my):
            draw.rect(screen,green,gangplankRect1)
        if taricRect.collidepoint(mx,my):
            draw.rect(screen,green,taricRect1)
        if aatroxRect.collidepoint(mx,my):
            draw.rect(screen,green,aatroxRect1)
        if unpauseRect.collidepoint(mx,my):
            draw.rect(screen,blue,unpauseRect1)
        if pauseRect.collidepoint(mx,my):
            draw.rect(screen,blue,pauseRect1)
        if restartRect.collidepoint(mx,my):
            draw.rect(screen,blue,restartRect1)

        #Undo Redo has a blue box around it.
        draw.rect(screen,blue,undoRect1)
        draw.rect(screen,blue,redoRect1)

        #This put the picture of over the colour boxes.
        screen.blit(pic2,(30,630))
        screen.blit(pic3,(95,630))
        screen.blit(smallBrush,(160,630))
        screen.blit(pic4,(225,630))
        screen.blit(pic5,(290,630))
        screen.blit(pic6,(355,750))
        screen.blit(pic7,(420,750))
        screen.blit(clearButton,(485,750))
        screen.blit(smallRectangle,(355,630))
        screen.blit(bigPoly,(420,630))
        screen.blit(fillword,(485,630))
        screen.blit(unfillword,(550,630))
        screen.blit(sEyeDropperPic,(615,630))
        screen.blit(undoPic,(550,750))
        screen.blit(redoPic,(615,750))
        screen.blit(sSticker1,(695,200))
        screen.blit(sSticker2,(895,200))
        screen.blit(sSticker3,(1095,200))
        screen.blit(sSticker4,(1095,10))
        screen.blit(sSticker5,(695,390))
        screen.blit(sSticker6,(895,390))
        screen.blit(sSticker7,(1095,390))
        screen.blit(sSticker8,(695,580))
        screen.blit(unpausePic,(915,655))
        screen.blit(pausePic,(1000,655))
        screen.blit(restartPic,(915,740))

        #This will say which tool it is.
        if pencilRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "pencil"
        elif eraserRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "eraser"
        elif brushRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "brush" 
        elif lineRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "line"
        elif ovalRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "oval"
        elif dropperRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "dropper"
        elif clearRect.collidepoint((mx,my)) and mb[0] == 1:
            lastTool = tool
            tool = "clear"
        elif rectangleRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "rectangle"
        elif polyRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "polygon"
        elif talonRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "talon"
        elif malphiteRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "malphite"
        elif hecarimRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "hecarim"
        elif lucianRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "lucian"
        elif renektonRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "renekton"
        elif gangplankRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "gangplank"
        elif taricRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "taric"
        elif aatroxRect.collidepoint((mx,my)) and mb[0] == 1:
            tool = "aatrox"
        elif fillwordRect.collidepoint((mx,my)) and mb[0] == 1:
            filltool = "fill"
        elif unfillwordRect.collidepoint((mx,my)) and mb[0] == 1:
            filltool = "unfill"
        elif unpauseRect.collidepoint((mx,my)) and mb[0] == 1:
            musictool = "unpause"
        elif pauseRect.collidepoint((mx,my)) and mb[0] == 1:
            musictool = "pause"
        elif restartRect.collidepoint((mx,my)) and mb[0] == 1:
            musictool = "restart"

        if tool == "pencil":
            if mb[0] == 1:
                screen.set_clip(canvas) #Clips the canvas.
                copy = screen.copy()
                draw.line(screen,col,(oldmx,oldmy),(mx,my)) #draws a line from the last point to the new point.
                screen.set_clip(None) #Unclips the canvas.
        if canvas.collidepoint((mx,my)) and tool == "eraser":
            screen.set_clip(canvas) #Clips the canvas.
            if mb[0] == 1:
                x = mx - oldmx #The difference between the x points.
                y = my - oldmy #The difference between the y points.
                d = int(((x)**2)+((y)**2)**0.5) #This is the distance formula.
                if d == 0:
                    d = 1
                for i in range(int(d)):
                    dx = int(oldmx+i/d*x) #This is getting all the distances between each point of x.
                    dy = int(oldmy+i/d*y) #This is getting all the distances between each point of y.
                    draw.circle(screen,white,(dx,dy),size)
            screen.set_clip(None) #Unclips the canvas.
        if tool == "brush":
            screen.set_clip(canvas)
            if mb[0] == 1:
                x = mx - oldmx #The difference between the x points.
                y = my - oldmy #The difference between the y points.
                d = int(((x)**2)+((y)**2)**0.5) #This is the distance formula.
                if d == 0:
                    d = 1
                for i in range(int(d)):
                    dx = int(oldmx+i/d*x) #This is getting all the distances between each point of x.
                    dy = int(oldmy+i/d*y) #This is getting all the distances between each point of y.
                    draw.circle(screen,col,(dx,dy),size)
            screen.set_clip(None)
        if tool == "line":
            screen.set_clip(canvas)
            if mb[0] == 1:
                screen.blit(copy,(0,0)) #Puts the last screen there.
                draw.line(screen,col,start,(mx,my),size) 
            screen.set_clip(None)
        if tool == "oval":
            if mb[0] == 1:
                screen.set_clip(canvas) 
                screen.blit(copy,(0,0)) #Puts the last screen there.
                if filltool == "fill":
                    circle = Rect(startx,starty,mx-startx,my-starty)
                    circle.normalize() #This corrects the negative sizes.
                    if size == abs(mx-startx) and size == abs(my-starty):
                        nothing = 0
                    elif size > abs((mx-startx)//2) or size > abs((my-starty)//2):
                        draw.ellipse(screen,col,circle) #draws filled circles.
                    elif size < abs((mx-startx)//2) and size < abs((my-starty)//2):
                        draw.ellipse(screen,col,circle) #draws filled circles.
                if filltool == "unfill":
                    circle = Rect(startx,starty,mx-startx,my-starty)
                    circle.normalize()
                    if size == abs(mx-startx) and size == abs(my-starty):
                        nothing = 0
                    elif size > abs((mx-startx)//2) or size > abs((my-starty)//2): #If the width is greater than the radius it draws a filled ellipse.
                        lastsize = size
                        size = 0
                        draw.ellipse(screen,col,circle,size)
                        size = lastsize
                    elif size < abs((mx-startx)//2) and size < abs((my-starty)//2): #If the width is smaller than the radius it draws a unfilled ellipse.
                        draw.ellipse(screen,col,circle,size)
                screen.set_clip(None)
        if clearRect.collidepoint((mx,my)) and tool == "clear":
            if mb[0] == 1:
                draw.rect(screen,(white),canvas) #Draws a white rectangle over the canvas which clears it.
                tool = lastTool #Changes the tool back to the last tool used.
        if canvas.collidepoint((mx,my)) and tool == "rectangle":
            screen.set_clip(canvas)
            if mb[0] == 1:
                if filltool == "fill":
                    screen.blit(copy,(0,0))
                    draw.rect(screen,col,(startx,starty,mx-startx,my-starty)) #draws filled rectangle.
                if filltool == "unfill":
                    screen.blit(copy,(0,0))
                    #Draws unfilled rectangle with the courners fixed.
                    draw.rect(screen,col,(startx,starty,mx-startx,my-starty),size)
                    draw.line(screen,col,(startx-((size)/2)+1,starty),(mx+((size)/2)-1,starty),size)
                    draw.line(screen,col,(startx-((size)/2)+1,my-1),(mx+((size)/2)-1,my-1),size)
                    draw.line(screen,col,(startx+((size)/2),starty),(mx-((size)/2),starty),size)
                    draw.line(screen,col,(startx+((size)/2),my-1),(mx-((size)/2),my-1),size)
            screen.set_clip(None)
        if canvas.collidepoint((mx,my)) and tool == "polygon":
            screen.set_clip(canvas)
            if mb[0] == 1:
                draw.line(screen,col,(mx,my),(mx,my),1) #Draws a small line.
                point = (mx,my) #It makes the point equals the mx and my position.
                polylist.append(point) #Adds the position into the list.
            if len(polylist) > 2:
                if mb[2] == 1 and filltool == "unfill":
                    draw.polygon(screen,col,polylist,size) #Draws unfilled polygons.
                    polylist = [] #Clear the list.
                if mb[2] == 1 and filltool == "fill":
                    draw.polygon(screen,col,polylist) #Draws filled polygons.
                    polylist = [] #Clear the list.
            screen.set_clip(None)
        if screen1.collidepoint((mx,my)) and tool == "dropper":
            if mb[0] == 1:
                col = screen.get_at((mx,my)) #Gets colour of anything on the screen but the tools.
                draw.rect(screen,(col),(1085,610,665,565)) #Shows the colour.
                screen.blit(smallColWheel,(1100,625)) #Draws the palette over the colour box.
        if canvas.collidepoint((mx,my)) and tool == "talon":
            screen.set_clip(canvas)
            if mb[0] == 1:
                screen.blit(stickercopy,(0,0)) #Puts the copied screen on the canvas.
                screen.blit(sSticker1, (mx - 100, my - 100)) #Puts the sticker onto the canvas.
            screen.set_clip(None)
        if canvas.collidepoint((mx,my)) and tool == "malphite":
            screen.set_clip(canvas)
            if mb[0] == 1:
                screen.blit(stickercopy,(0,0)) #Puts the copied screen on the canvas.
                screen.blit(sSticker2, (mx - 100, my - 100)) #Puts the sticker onto the canvas.
            screen.set_clip(None)
        if canvas.collidepoint((mx,my)) and tool == "hecarim":
            screen.set_clip(canvas)
            if mb[0] == 1:
                screen.blit(stickercopy,(0,0)) #Puts the copied screen on the canvas.
                screen.blit(sSticker3, (mx - 100, my - 100)) #Puts the sticker onto the canvas.
            screen.set_clip(None)
        if canvas.collidepoint((mx,my)) and tool == "lucian":
            screen.set_clip(canvas)
            if mb[0] == 1:
                screen.blit(stickercopy,(0,0)) #Puts the copied screen on the canvas.
                screen.blit(sSticker4, (mx - 100, my - 100)) #Puts the sticker onto the canvas.
            screen.set_clip(None) 
        if canvas.collidepoint((mx,my)) and tool == "renekton":
            screen.set_clip(canvas)
            if mb[0] == 1:
                screen.blit(stickercopy,(0,0)) #Puts the copied screen on the canvas.
                screen.blit(sSticker5, (mx - 100, my - 100)) #Puts the sticker onto the canvas.
            screen.set_clip(None)
        if canvas.collidepoint((mx,my)) and tool == "gangplank":
            screen.set_clip(canvas)
            if mb[0] == 1:
                screen.blit(stickercopy,(0,0)) #Puts the copied screen on the canvas.
                screen.blit(sSticker6, (mx - 100, my - 100)) #Puts the sticker onto the canvas.
            screen.set_clip(None)
        if canvas.collidepoint((mx,my)) and tool == "taric":
            screen.set_clip(canvas)
            if mb[0] == 1:
                screen.blit(stickercopy,(0,0)) #Puts the copied screen on the canvas.
                screen.blit(sSticker7, (mx - 100, my - 100)) #Puts the sticker onto the canvas.
            screen.set_clip(None)
        if canvas.collidepoint((mx,my)) and tool == "aatrox":
            screen.set_clip(canvas)
            if mb[0] == 1:
                screen.blit(stickercopy,(0,0)) #Puts the copied screen on the canvas.
                screen.blit(sSticker8, (mx - 100, my - 100)) #Puts the sticker onto the canvas.
            screen.set_clip(None)
        if unpauseRect.collidepoint((mx,my)) and musictool == "unpause":
            mixer.music.unpause() #Unpause the music.
        if pauseRect.collidepoint((mx,my)) and musictool == "pause":
            mixer.music.pause() #Pause the music.
        if restartRect.collidepoint((mx,my)) and musictool == "restart":
            mixer.music.rewind() #Restarts the music.

        #The positions of the last mx and my value.
        oldmx = mx 
        oldmy = my
                
    display.flip()
quit()
