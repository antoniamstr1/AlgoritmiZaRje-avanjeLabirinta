from .pyamaze import maze, agent, COLOR


def DFS(labirint, smjerovi, istrazene, rubne, dfsPath, pocetak):
    istrazene.append(pocetak)
    rubne.append(pocetak)
    while len(rubne) > 0:
        trenutna = rubne.pop()
        if trenutna == (1, 1):
            break

        for sm in smjerovi:
            if labirint.maze_map[trenutna][sm] == True:
                if sm == 'E':
                    # istočna je desno od trenutne
                    sljedeca = (trenutna[0], trenutna[1]+1)
                elif sm == 'S':
                    # južna je ispod trenutne
                    sljedeca = (trenutna[0]+1, trenutna[1])
                elif sm == 'N':
                    # sjeverna je iznad trenutne
                    sljedeca = (trenutna[0]-1, trenutna[1])
                elif sm == 'W':
                    # zapadna je desno od trenutne
                    sljedeca = (trenutna[0], trenutna[1]-1)

                if sljedeca in istrazene:
                    continue

                istrazene.append(sljedeca)
                rubne.append(sljedeca)
                dfsPath[sljedeca] = trenutna

    fwdPath = {}
    cell = (1, 1)
    while cell != pocetak:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath


def pokretanje_dfs(n, smjer1, smjer2, smjer3, smjer4):
    labirint = maze(n, n)
    # perfectmaze nema argumenata
    labirint.CreateMaze(loadMaze="labirint.csv")

    pocetak = (n, n)
    smjerovi = []
    smjerovi.append(smjer1)
    smjerovi.append(smjer2)
    smjerovi.append(smjer3)
    smjerovi.append(smjer4)
    istrazene = []
    rubne = []

    dfsPath = {}

    path = DFS(labirint, smjerovi, istrazene, rubne, dfsPath, pocetak)

    a = agent(labirint, footprints=True)
    labirint.tracePath({a: path})

    labirint.run()
