import subprocess
import os.path

class Structure:
    
    def __init__(self,pdb=None):
        
        self.pdb=pdb
        self.pdbpath = self.pdb + '.pdb'

    def runCrysol(self):
        
        if os.path.exists(self.pdbpath):
            subprocess.Popen(['crysol',self.pdbpath])
            return
        else:
            print 'diSASTER!'

    def runCryson(self, d2o=1.0):
        d2o=str(d2o)
        if os.path.exists(self.pdbpath):
            p=subprocess.Popen(['cryson',self.pdbpath,'/d2o',d2o])
            p.wait()
            return
        else:
            print 'diSASTER!'

pdb=raw_input('pdb code?  ')
p=Structure(pdb)
p.runCrysol()
p.runCryson()
x=0.0
while x<=1.0:
    p.runCryson(x)
    x=x+0.1

    

                
