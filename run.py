import platform
from config import *
import os
class run:
    def runapp(_self):
        paths = appfolders[_self.getPlatform()]
        paths.append(os.environ['HOME']+'\Start Menu\Programs')
        print paths
    def getPlatform(_self):
        p = platform.platform()
        if p.startswith('Windows-XP'):
            p='windowsxp'
        return p

if __name__=='__main__':
    r = run()
    r.runapp()
