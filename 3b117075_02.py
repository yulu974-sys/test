# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


# 首頁
@app.route("/")
def home():
    return "<h1>歡迎來到 Flask!</h1>"


# 動態路由：問候
@app.route("/hello/<name>")
def hello(name):
    return f"<h1>Hello, {name}!</h1>"


# 動態路由 + 轉換器：出生年
@app.route("/birth/<int:year>")
def birth(year):
    roc_year = year - 1911
    age = 2026 - year
    return f"<p>您是民國 {roc_year} 年出生，今年 {age} 歲</p>"


if __name__ == "__main__":
    app.run(debug=True)
