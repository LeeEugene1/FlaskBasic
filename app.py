from models import User
import os
from flask import Flask, render_template, request, redirect
from models import db

app = Flask(__name__)

#현제있는 파일의 디렉토리 절대경로
basdir = os.path.abspath(os.path.dirname(__file__))
#basdir 경로안에 DB파일만들기
dbfile = os.path.join(basdir, 'db.sqlite')

#SQLAlchemy설정

#내가 사용할 DB url
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
#비즈니스로직이 끝날때 commit 실행(db반영)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#수정사항에 대한 Track
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#secret-key
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

db.init_app(app) #앱에 cofig외에 많은값들을 초기화
db.app = app #db안에 앱이라는 변수를 명시적으로 넣기
db.create_all() #db생성


#기본적으로 get만 설정되어있기때문에 메서드 post를 넣어준다 안그럼 메서드 에러남
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        #회원정보설정(모델에있는 class를 가져와서 사용자생성을하고 리다이랙션)
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re-password')
        print(userid)

        if not (userid and username and password and re_password):
            return render_template('register.html')

        if password != re_password:
            return render_template('register.html')
        
        #유저 객체생성
        useruser = User()
        useruser.userid = userid
        useruser.username = username
        useruser.password = password

        #db안에 session안에 add 후 커밋
        db.session.add(useruser)
        db.session.commit()

        return redirect('/')    

@app.route('/')
def home():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
