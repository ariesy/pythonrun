import platform
import sys
from config import *
import os
import subprocess
class run:
    def runapp(_self,appname):
        #appname=raw_input('input')
        print appname
        paths = appfolders[_self.getPlatform()]
        findapp=False
        for path in paths:
            
            if findapp==True:
                break
            print path
            for parent,dirnames,filenames in os.walk(path):
                if findapp==True:
                    break
                for dirname in dirnames:
                    if findapp==True:
                        break
                    for f in filenames:
                        if os.path.splitext(f)[0].lower()==appname.lower() and os.path.splitext(f)[1]=='.exe':
                            print f
                            print dirname
                            fullpath = os.path.join(path,parent,dirname)
                            print fullpath
                            os.chdir(fullpath)
                            os.startfile(f)
                            findapp=True
                            break
        raw_input('quit')

    def getPlatform(_self):
        p = platform.platform()
        if p.startswith('Windows-XP'):
            p='windowsxp'
        return p

if __name__=='__main__':
    appname=''
    if len(sys.argv)>=2:
        appname=sys.argv[1]
    #else:
     #   appname='7zFM'
    print appname
    if len(appname)>0:
        r = run()
        r.runapp(appname)
