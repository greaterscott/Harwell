import subprocess
import os
import os.path
import crysox
import matplotlib.pyplot as plt

class Structure:

    def __init__(self, pdb=None):
        """Init method for a toy structure class"""

        self.pdb = pdb
        self.pdbpath = self.pdb + '.pdb'
        self.structurerootpath = os.getcwd()
        
        self.initDir('crysol')
        self.initDir('cryson')
        self.initDir('stuhrmann')

    def initDir(self, dirname):
        if os.path.exists(dirname) and os.path.isdir(dirname):
            pass
        else:
            os.mkdir(dirname)            

    def runCrysol(self):
        """Method for running crysol over the pdb""" 

        # crysol directory should exist and throwing error if not is appropriate
        os.chdir('crysol')
        pdbpath = '../' + self.pdbpath
        if os.path.exists(pdbpath):
            p = subprocess.Popen(['crysol', pdbpath], stdout=subprocess.PIPE)
            p.wait()
        
        else:
            print "Can't find file"
        
        os.chdir('..')
        return


    def runCryson(self, d2o=0.0):
        """Method for running crysol over the pdb"""

        os.chdir('cryson')
        pdbpath = '../' + self.pdbpath
        d2o = str(d2o)
        if os.path.exists(pdbpath):
            p = subprocess.Popen(['cryson', pdbpath, '/d2o', d2o], stdout=subprocess.PIPE)
            p.wait()
        
        else:
            print "Can't find file"

        os.chdir('..')
        return

    def runStuhrmann(self, contrasts=[]):
        """Generating Data for a Sturhmann Plot, defaults to 10 points"""

        if contrasts == []: 
            for contrast in range(11):
                contrasts.append(float(contrast)/10)
    

        for contrast in contrasts:
            self.runCryson(contrast)
            print contrast

        outfiles = os.listdir('cryson/')
        logfiles = filter(self.filterLogFiles, outfiles)
        
        stuhrvalues = []
        for log in logfiles:
            params = crysox.parseLogFile('cryson/' + log)
            rg = params['rg']
            contrast = params['particle_cont']
            stuhrvalues.append([contrast, rg])

        return stuhrvalues
        

    def filterLogFiles(self, filename):
        if filename[(len(filename)-3):len(filename)] == 'log': return True


p = Structure('3Q8L')
s = p.runStuhrmann()
inv_cont=[]
rg_sq=[]
for point in s:
    inv_cont.append(1/point[0])
    rg_sq.append(point[1]**2)

plt.plot(inv_cont, rg_sq, 'ro')
plt.show()

while True:
    pass
    


#pdb=raw_input('pdb code?  ')
#p=Structure(pdb)
#p.runCrysol()
#p.runCryson()
#x=0.0
#while x<=1.0:
#    p.runCryson(x)
#    x=x+0.1

        
        
        
