from re import X
import OOMP
import subprocess
import os.path

types = ["Bbls","Diag","Iden","Schem","Simp"]

def generateDiagrams(item, diagrams=False, renders=False, overwrite=False):  
    oompID = item.getTag("oompID").value
    global types
    if diagrams:
        #print(item.fullString())                 
        for type in types:                
            #print("    Type: " + type)
            folder = OOMP.getDir("parts",base=False) + oompID + "/"
            outFile = folder + "diag" + type.upper() + ".py" 
            if not os.path.isfile(outFile) or overwrite:    
                print("Drawing item: " + oompID)
                f = open(outFile,"w")
                ####### Setup Commands
                #svg_root.set('width', '148mm')
                #svg_root.set('height', '210mm')
                wid = 50
                hei = 50
                line = "import os"
                f.write(line + "\n")
                line = "svg_root.set('width', '" + str(wid) + "mm')"
                f.write(line + "\n")
                line = "svg_root.set('height', '" + str(hei) + "mm')"
                f.write(line + "\n")
                line = "width, height = svg_root.width, svg_root.height"
                f.write(line + "\n")
                line = "svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))"
                f.write(line + "\n")
                line="svg_root.namedview.set('showgrid', 'false')"
                f.write(line + "\n")
                line = "shapes=[]"
                f.write(line + "\n")

                line = "shiftX=" + str(wid) 
                f.write(line + "\n")
                line = "shiftY=" + str(hei) 
                f.write(line + "\n")
                line = getInkscapePython("rect",[],x=0,y=0,width=50,height=50,style="white",start="shapes.append(")
                f.write(line + "\n")
                
                tags = item.tags
                for tag in tags:
                    if tag.name == "oomp" + type:
                        line = tag.value.replace("\n","") 
                        
                        line = processCommand(line,item)
                        #print(line)
                        f.write(line + "\n")
                f.write('os.chdir("' + OOMP.getDir("base",base=True) + folder + '")\n')  
                f.write('try:\n')              
                f.write('    os.remove("' + OOMP.getDir("base",base=True) + folder + 'diag' + type.upper() + '.svg")\n')
                f.write('except:\n')  
                f.write('    f=0\n')  
                f.write("inkex.command.write_svg(svg_root, 'diag" + type.upper() + ".svg')\n\n")
                f.write("for shape in shapes:\n")
                f.write("    shape.remove()")
                f.close()
    if renders:
        
        for type in types:
            #print("    Type: " + type)
            folder = OOMP.getDir("parts") + oompID + "/"
            file = folder + "diag" + type.upper()
            inFile = file + ".svg"
            outFile = file + ".png"
            if not os.path.isfile(outFile) or overwrite:  
                print("Rendering item: " + oompID)
                if os.path.exists(inFile):
                    launchString = 'inkscape.exe --export-type="png" ' + inFile
                    print("        " + launchString)
                    subprocess.run(launchString)
                    launchString = 'inkscape.exe --export-type="dxf" ' + inFile
                    print("        " + launchString)
                    subprocess.run(launchString)
                    launchString = 'inkscape.exe --export-type="pdf" ' + inFile
                    print("        " + launchString)
                    subprocess.run(launchString)
                    
                                

def processCommand(line,item):
    part=item
    line2 = line
    hexID = item.getTag("hexID").value
    name = item.getTag("name").value
    ooDesignator = item.getTag("ooDesignator").value
    #print("Line: " + line)
    line = line.replace("%%i%%","&&i&&")
    line = line.replace("%%","")
    line = line.replace("##hexID@@",hexID)
    line = line.replace("##name@@",name)
    line = line.replace("##ooDesignator@@",'"' + ooDesignator + '"')
    details = line.split(";")
    if len(details) > 0:
        type = details[0]
    if(type == "XXXX"):
        type = type
######  LINEWIDTH    
    elif(type == "hLine"):
        #hLine; 7.5;    (%%pins%%*10/2)-(%%i%%-1)*10-5; 5;  0;  pin %%i%%")
        #       X       Y                               W   H
        line = "######  " + line2 + "\n" + getInkscapePython("shape = polyline",details,style="hLine")        
        line = line + "shapes.append(shape)\n"
        
######  LINEWIDTH    
    elif(type == "linewidth"):
        line = "linewidth = " + details[1] + "    #  " + line
######  OOMPNAME 
    elif(type == "oompName"):
        #text = '"'+ name+'"'
        line = "######  " + line2 + "\n" + getInkscapePython("shape = rect",details,style="invisible")
        line = line + "shapes.append(shape)\n"
        line = line + getInkscapePython("shape = text",details,style="oompName")
        line = line + "shapes.append(shape)\n"
######  OOMPURL    
    elif(type == "oompURL"):
        text = 'http://oom.lt/' + hexID       
        line = "######  " + line2 + "\n" + getInkscapePython("shape = rect",details,style="invisible")
        line = line + "shapes.append(shape)\n"
        line = line + getInkscapePython("shape = text",details,text=text,style="oompURL")
        line = line + "shapes.append(shape)\n"

######  PIN
    elif(type == "pin"):
        line2 = line
        line = "######  " + line2 + "\n" + getInkscapePython("rect",details, style="pin",start="shapes.append(")
######  PIN Holder
    elif(type == "pinHolder"):
        line2 = line
        line = "######  " + line2 + "\n" + getInkscapePython("rect",details, style="pinHolder",start="shapes.append(")
######  RECTANGLE    
    elif(type == "rectangle"):
        line2 = line
        line = "######  " + line2 + "\n" + getInkscapePython("rect",details, style=None,start="shapes.append(")
        
######  REPEAT
    elif(type == "repeat"):        
        shorterCommand = ""
        index = 0
        for a in details:
            if index < 2:
                index = index + 1
            else:
                shorterCommand = shorterCommand + a + ";"    
        line2 = line
        line = "for b in range(" + details[1] + "):" + "    # " + line2 + "\n" + "    i = b + 1\n" + "    " + processCommand(shorterCommand,part).replace("\n","\n    ")
######  TEMPLATE    
    elif(type == "template"):
        line = "# TEMPLATE  " + line + "\n"
        item = OOMP.getPartByHex(details[1])            
        tags = item.tags
        #print("Tag Length:" ,len(tags))
        if(len(tags) > 1):
            for tag in tags:
                if tag.name == "drawItem":
                    line = line + processCommand(tag.value,part) + "\n"
        else:            
            line = "# MISSING TEMPLATE " + line
######  TEXTB    
    elif(type == "textB"):
        details = [details[0],details[1],details[2],0,0,details[3],details[4],]        
        line = getInkscapePython("text",details,style="textB",start="shapes.append(")            
######  VARIABLE        
    elif(type == "variable"):
        if not details[1] == "clear": 
            line = details[1] + " = " + details[2] + "    #  " + line
        else:
            line = "#  CLEAR " + line
        
    else:
        line = "#  " + line
    return line



def getInkscapePython(type,details, drawType=None, x=None, y=None, width=None, height=None,style=None,text=None,fontSize=None,start=None):
    #print("Details: ", end="")
    #print( details)
    if len(details) > 0:
        drawType = details[0]
    if len(details) > 1 and x == None:
        x = details[1] 
    if len(details) > 2 and y == None:    
        y = details[2]
    if len(details) > 3 and width == None:    
        width = details[3]
    if len(details) > 4 and height == None:            
        height = details[4]
    if len(details) > 5 and fontSize == None:   
        fontSize = details[5]
    if len(details) > 6 and text == None:            
        text = details[6]

    ######  Style Stuff
    style = getInkscapeStyle(style,fontSize=fontSize)

    #print("Details: ", details)

    line = ""


    if text == None:
        text = ""

    if start == None:
        start=""
        end=""
    else:
        start=start
        end=")"    

    if("text" in type):
        text = text.replace("&&i&&", "' + str(i) + '")
        line = "x = " + x.replace("&&i&&","i") + "\n"
        line = line + "y = (" + y.replace("&&i&&","i") + ")* -1\n"
        line = line + "fontShift = (" + fontSize + ")* 0.3527 * .5\n"
        line = line + start+ type +  "('" + text + "',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm)," + style + ")" + end + "\n"
    elif("polyline" in type):
        #hLine; 7.5;    (%%pins%%*10/2)-(%%i%%-1)*10-5; 5;  0;  pin %%i%%")
        #       X       Y                               W   H
        line = "x = " + x.replace("&&i&&","i") + "\n"
        line = line + "y = (" + y.replace("&&i&&","i") + ")* -1\n"
        line = line + "width = " + str(width.replace("&&i&&","i")) + "\n"
        line = line + "height = " + str(height.replace("&&i&&","i")) + "\n"
        line = line + "x1 = x - width/2 \ny1 = y - height/2 \nx2 = x + width/2 \ny2 = y + height/2 \n"
        line = line + start + type +  "([((x1+shiftX/2)*mm,(y1+shiftY/2)*mm),((x2+shiftX/2)*mm,(y2+shiftY/2)*mm)]," + style + ")" + end + "\n"
    else:    
        line = "x = " + str(x).replace("&&i&&","i") + "\n"
        line = line + "y = (" + str(y).replace("&&i&&","i") + ")* -1\n"
        line = line + "width = " + str(str(width).replace("&&i&&","i")) + "\n"
        line = line + "height = " + str(str(height).replace("&&i&&","i")) + "\n"
        line = line + "x1 = x - width/2 \ny1 = y + height/2 \nx2 = x + width/2 \ny2 = y - height/2 \n"
        line = line + start +type + "(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1," + style + ")" + end + "\n"


    return line

def getInkscapeStyle(style=None, fontSize=None):
    if fontSize == None:
        fontSize = "1"
    rv =  "stroke_width=linewidth"   
    if(style == ""):
        c = 0
    elif(style == "hLine"):
        rv = getStyleDraw(fill="black")
    elif(style ==  "invisible"):
        rv =  "stroke_width=0"   
    elif(style == "oompName"):
        rv = "stroke_width=0.4,stroke='black',font_size='" + fontSize + "pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape"
    elif(style == "oompURL"):
        rv = "stroke_width=0.1,stroke='black',font_size='" + fontSize + "pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape"
    elif(style == "pin"):
        rv = getStyleDraw(fill="gold",stroke_width=0.5)
    elif(style == "pinHolder"):
        rv = getStyleDraw(fill="black",stroke_width=1)
    elif(style == "textB"):
        rv = getStyleText(stroke_width=0.25,stroke='black',font_size=fontSize,text_anchor='middle')
    elif(style == "white"):
        rv = getStyleDraw(stroke_width=0.0,fill='white',stroke="white")

    return rv

def getStyleText(stroke_width=None,stroke=None,font_size=None,font_family=None,text_anchor='center',shape_inside=None):
        rv = ""
        ###### Stroke
        if(stroke != None):
            rv = rv + "stroke='" + getColor(stroke) + "',"
        ###### Font Size
        if(font_size == None):
            font_size = 4
        rv = rv + "font_size='" + str(font_size) + "pt',"
        ###### Font Family
        if(font_family == None):
            font_family = 'Relief Single Line Outline'
        rv = rv + "font_family='" + font_family + "',"
        ###### Text Anchor
        if(text_anchor != None):
            rv = rv + "text_anchor='" + text_anchor + "',"

        ###### Stroke Width        
        if(stroke_width == None):
            stroke_width = 1
        rv = rv + "stroke_width=" + str(stroke_width)
        #print("text Style= " + rv)
        return rv

def getStyleDraw(fill=None,stroke_width=None,stroke=None,):
        rv = ""
        ######  Fill
        color = getColor(fill)
        if(color != None):
            rv=rv+"fill='" + color + "',"
        ###### Stroke
        if(stroke != None):
            rv = rv + "stroke='" + getColor(stroke) + "',"            
        ######  Stroke Width
        if(stroke_width != None):
            rv = rv + "stroke_width=" + str(stroke_width)
        else:    
            rv = rv + "stroke_width=1"
        return rv

def getColor(color):
    rv = None
    if(color == "black"):
        rv='#000000'
    if(color == "gold"):
        rv='#FFD700'
    if(color == "white"):
        rv='#FFFFFF'
    return rv


def genAllDiagramsFile():
    base = "C:/GH/oomlout_OOMP/"
    OOMP.setBaseDir(base)
    directory = OOMP.getDir("parts",base=True)
    filter1 = "diag"
    filter2 = ".py"
    count = 0
    diagFiles = []
    print("        Generating diagrams for: " + directory)
    for subdir, dirs, files in os.walk(directory):
            for file in files:
                if(filter1 in file and filter2 in file and not "diagsAll.py" in file and not "__pycache__" in subdir):
                    moduleName = file.replace(".py","")                    
                    moduleName = subdir.replace(base,"").replace("\\",".").replace("/",".") + "." + moduleName
                    fileName = subdir + "/" + file
                    #print("    moduleName: " + moduleName)
                    #print(".",end="")
                    #__import__(moduleName)
                    diagFiles.append(fileName)
    outFile = directory + "diagsAll.py"
    out = open(outFile,"w")
    for file in diagFiles:
        f = open(file)
        out.write(f.read())
        out.write("\n")
        f.close()    