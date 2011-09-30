import subprocess
import os
import os.path

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


pdb=raw_input('pdb code?  ')
p=Structure(pdb)
p.runCrysol()
p.runCryson()
x=0.0
while x<=1.0:
    p.runCryson(x)
    x=x+0.1

        
        
        
