import os
import sys

path = os.path.dirname(sys.path[0])
if path and path not in sys.path:
    sys.path.append(path)

from flask import Flask

app = Flask("Product")


@app.route("/")
def welcome():
    return "欢迎来到通达信数据分析的世界"


if __name__ == '__main__':
    app.run()
