import os, shutil, sys

def makerunsdir(namedir):
    if os.path.exists(namedir):
        print("existed:"+namedir)
        #shutil.rmtree(namedir)
        print("removing:"+namedir)
    else:
        print("not exist:"+namedir)

    origindir=os.getcwd()
    path = os.path.join(origindir, namedir)
    #os.mkdir(path)
    print("creating:"+namedir)
    orgrundir=origindir + "/" + namedir + "/"
    return orgrundir

def text_num_split(item):
    for index, letter in enumerate(item, 0):
        if letter.isdigit():
            return [item[:index],item[index:]]


        
def getdat(DIRDATA, name):
    output = 0
    if os.path.exists(DIRDATA):
        with open(DIRDATA) as openfile:
            for line in openfile:
                for part in line.split():
                    if name in part:
                        output = part
            output = text_num_split(output)[1]
            return output
    else:
        print("thre is no data file")
    return output



def changeAllrun(dirY, x, y):
    filename = dirY + "/" + "Allrun" 
    openfile= open(filename, "rt")
    readfile=openfile.read()
    openfile.close()

    replacedata=readfile.replace('ThPython', x)
    replacedata=replacedata.replace('gravityPython', y)


    openfile= open(filename,"wt")
    openfile.write(replacedata)
    openfile.close()
    return

def gendir(Dirname):
    if os.path.exists(Dirname):
        print("existed:"+Dirname)
    else:
	print("not exist:"+Dirname)
	os.mkdir(Dirname)


def runOF(X, Y, orgrundir):
    origindir=os.getcwd()
    src = origindir + "/case0"
    print (src)
    Xn = len(X)
    Yn = len(Y)


    for x in range (0, Xn, 1):
	dirX = os.path.join(orgrundir, "Th" + str(X[x]))
	gendir(dirX)

	for y in range (0, Yn, 1):
	    dirY = os.path.join(dirX, "gravity" + str(Y[y]))
	    #gendir(dirY)

    	    if os.path.exists(dirY):
		print("existed:"+dirY)
	    else:
		print("not exist:"+dirY)
		shutil.copytree(src, dirY)
		changeAllrun( dirY, str(X[x]), str(Y[y]) )

	    os.system(dirY + "/Allrun")




orgrundir = makerunsdir("Runs")
X = [293, 313, 333]
Y = [-9.81e-2, -9.81e-1, -9.81]

runOF(X, Y, orgrundir)






