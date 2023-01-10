from contextlib import nullcontext
import os
from .pyamaze import maze


def createMaze(n, looppercent):
    ime = nullcontext
    for root, dirs, files in os.walk("./"):
        for file in files:
            if file.endswith(".csv"):
                ime = os.path.join(root, file)
    # ako file postoji, izbrišem ga
    if ime != nullcontext:
        print('IMA VEĆ')
        os.remove("labirint.csv")
    # napravljen novi maze
    # n za veličinu
    labirint = maze(n, n)

    # parametri za stvaranje labirinta
    # def CreateMaze(self,x=1,y=1,pattern=None,loopPercent=0,saveMaze=False,loadMaze=None,theme:COLOR=COLOR.dark):
    # pattern: v ili h (kojih će biti više)S
    # loopPercent: 0  da je perfect maze (jedan mogući put) do 100
    labirint.CreateMaze(saveMaze=True, loopPercent=looppercent)
    labirint.run()
    ime2 = 'a'

    # promjena imena u labirint.cvs
    for root, dirs, files in os.walk("./"):
        for file in files:
            if file.endswith(".csv"):
                ime2 = os.path.join(root, file)

    print('napravljen novi')
    os.rename(ime2[2:], "labirint.csv")
