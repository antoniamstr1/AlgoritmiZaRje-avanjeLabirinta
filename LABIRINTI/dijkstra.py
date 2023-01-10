from pyamaze import maze, agent, COLOR, textLabel


def pokretanje_dijkstre(n, x, y):
    n

    def Dijkstra(labirint, *agent):
        neposjecene = {}
        istrazene = {}
        smjerovi = ['E', 'S', 'N', 'W']

        prepreke = []
        """ for i in agent:
            prepreke.append((i.position, i.cost)) """
        prepreke = [(i.position, i.cost) for i in agent]

        for i in labirint.grid:
            neposjecene[i] = float('inf')
        neposjecene[n, n] = 0

        # dodajem za ispis puta
        revPath = {}

        # dok neposjeceni nisu prazni
        while neposjecene:
            trenutna = min(neposjecene, key=neposjecene.get)

            istrazene[trenutna] = neposjecene[trenutna]

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
                    ukupna_tezina = neposjecene[trenutna]+1
                    for i in prepreke:
                        if i[0] == trenutna:
                            ukupna_tezina += i[1]

                    if ukupna_tezina < neposjecene[sljedeca]:
                        neposjecene[sljedeca] = ukupna_tezina
                        revPath[sljedeca] = trenutna
            neposjecene.pop(trenutna)

        fwdPath = {}
        cell = (1, 1)
        while cell != (labirint.rows, labirint.cols):
            fwdPath[revPath[cell]] = cell
            cell = revPath[cell]

        return fwdPath, istrazene[(1, 1)]

    labirint = maze(n, n)
    # perfectmaze nema argumenata
    labirint.CreateMaze(loadMaze="labirint.csv")
    agent1 = agent(labirint, x, y, color=COLOR.red)
    #agent2 = agent(labirint, 4, 7, color=COLOR.red)
    agent1.cost = 100
    #agent2.cost = 100

    path, rezultat = Dijkstra(labirint, agent1)
    textLabel(labirint, "Total cost", rezultat)

    agent3 = agent(labirint, color=COLOR.cyan,
                   filled=True, footprints=True)

    labirint.tracePath({agent3: path})

    labirint.run()
