# save this as app.py
from flask import Flask
import mecab
mecab = mecab.MeCab()

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    txt = '사랑하고싶게하는가슴속온감정을헤집어놓는영화예요정말최고'

    #print(mec.pos(txt, flatten=False, join=True)) #mecab
    #print(kom.pos(txt,flatten=False, join=True)) #komoran
    #print(kkm.pos(txt,flatten=False, join=True)) #kkma
    #print(okt.pos(txt,norm=True, stem=True, join=True)) #okt

    return mecab.pos(txt)

@app.route('/user/<user_name>/<int:user_id>')
def user1(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'
