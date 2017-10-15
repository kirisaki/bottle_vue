#!/usr/bin/python
# -*- coding: utf-8 -*-
from bottle import route, get, HTTPResponse, static_file, run
import json
import os
import sys

# ルーティングはvue.jsに任せる
@route("/")
@route("/<aid:int>")
def index(aid=0):
    return static_file('/html/index.html', root='./')

# 静的ファイルはそのまま返す
# 画像とかのディレクトリがある場合は適宜追加してやる
@route('/scripts/<name:path>')
def return_script(name):
    return static_file(name, root='./scripts')

# json取得していい感じにjsonでリクエストに答える
# こっちは記事IDとタイトルを持ってくる
@get('/api/article')
def get_article():
    with open("testdata.json", "r") as f:
        data = json.load(f)
    records = [{"aid":rec['aid'],"title":rec['title']} for rec in data]
    body = json.dumps(records)
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r

# こっちは記事そのものを持ってくる
@get('/api/article/<aid:int>')
def getsrticle(aid):
    with open("testdata.json", "r") as f:
        data = json.load(f)
    body = json.dumps([r for r in data if r['aid']==aid][0])
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r

if __name__ == "__main__":
    run(host='0.0.0.0', port=8000)        
