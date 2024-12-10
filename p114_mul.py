from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    #URLパラメーターを取得---
    a=request.args.get("a")
    b=request.args.get("b")
    
    #パラメータが設定されているかを確認
    if (a is None) or (b is None):
        return "パラメータが足りません。"
    
    #パラメータを数値に変換して計算
    c = int(a) * int(b)

    #結果を出力
    return "<h1>"+str(c)+"</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

#URLの後ろに/?a=30&b=50をつけてアクセスすると計算して1500と表示されます。