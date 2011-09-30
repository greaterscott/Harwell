import subprocess
import os.path

class Structure:

    def __init__(self, pdb=None):
        """Init method for a toy structure class"""

        self.pdb = pdb
        self.pdbpath = self.pdb + '.pdb'

    def runCrysol(self):
        """Method for running crysol over the pdb""" 

        if os.path.exists(self.pdbpath):
            p = subprocess.Popen(['crysol', self.pdbpath], stdout=subprocess.PIPE)
            p.wait()
            return
        
        else:
            print "Can't find file"

    def runCryson(self, d2o=1.0):
        """Method for running crysol over the pdb"""

        d2o = str(d2o)
        if os.path.exists(self.pdbpath):
            p = subprocess.Popen(['cryson', self.pdbpath, '/d2o', d2o], stdout=subprocess.PIPE)
            p.wait()
            return
        
        else:
            print "Can't find file"



p = Structure('fen1')
p.runCrysol()
p.runCryson()
p.runCryson(0.0)

        
        
        
