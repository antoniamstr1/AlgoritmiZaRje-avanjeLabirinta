from flask import Blueprint, render_template, request
from LABIRINTI.CreateLabirint import createMaze
from LABIRINTI.DFS import DFS, pokretanje_dfs
from LABIRINTI.pyamaze import maze, agent, COLOR
from LABIRINTI.main2 import pokretanje_dijkstre

import gc
views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/stvoriLabirint_", methods=['GET', 'POST'])
def stvoriLabirint():
    if request.method == 'POST':
        n = request.form.get('n')
        globalni_n = n
        loopPercent = request.form.get('looppercent')
        createMaze(int(n), int(loopPercent))
    gc.collect()

    return render_template("stvoriLabirint.html")


@views.route("/dfs_alg", methods=['GET', 'POST'])
def dfs_alg():
    with open('labirint.csv') as f:
        for line in f:
            pass
        last_line = line

    # initializing substrings
    sub1 = "("
    sub2 = ","

    last_line = last_line.replace(sub1, "*")
    last_line = last_line.replace(sub2, "*")
    re = last_line.split("*")
    res = re[1]

    # printing result

    # dio s stvaranjem labirinta
    if request.method == 'POST':
        s1 = request.form.get('smjer1')
        s2 = request.form.get('smjer2')
        s3 = request.form.get('smjer3')
        s4 = request.form.get('smjer4')

        pokretanje_dfs(int(res), s4, s3, s2, s1)
    gc.collect()

    return render_template("dfs.html")


@views.route("/dijkstra", methods=['GET', 'POST'])
def dfs_alg2():
    with open('labirint.csv') as f:
        for line in f:
            pass
        last_line = line

    # initializing substrings
    sub1 = "("
    sub2 = ","

    last_line = last_line.replace(sub1, "*")
    last_line = last_line.replace(sub2, "*")
    re = last_line.split("*")
    res = re[1]

    # printing result

    # dio s stvaranjem labirinta
    if request.method == 'POST':
        x = request.form.get('x')
        y = request.form.get('y')

        pokretanje_dijkstre(int(res), int(x), int(y))
        gc.collect()

    return render_template("dijkstra.html")
