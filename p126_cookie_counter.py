from flask import Flask,make_response,request #Cookieのため
from datetime import datetime

app=Flask(__name__)

@app.route("/")
def index():
    #Cookieの値を取得
    cnt_s = request.cookies.get("cnt")
    if cnt_s is None:
        cnt=0
    else:
        cnt=int(cnt_s)

    #訪問回数カウンタに1加算
    cnt += 1
    response = make_response("""
        <h1>訪問回数：{}回</h1>
    """.format(cnt))

    #Cookieに値を保存
    max_age = 60 *60 *24 * 90 #90日
    expires = int(datetime.now().timestamp()) + max_age
    response.set_cookie("cnt",value=str(cnt),
                        max_age=max_age,
                        expires=expires)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)