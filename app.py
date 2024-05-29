from flask import Flask, session, redirect, url_for, request, render_template
from db_scripts import get_question_after, quiz_form, main, show_ans



def index():
    return render_template("index.html")


def index2():
    return render_template("index2.html")


def quest():
    main()
    session['counter']=0
    session['last_question']=0
    if request.method=='GET':
        return render_template("quest.html")
    if request.method=='POST':
        res=request.form.get('quiz')
        session['quiz']=res
        return redirect(url_for('test'))


def test():
    k=[1]
    result = get_question_after(session['last_question'], session['quiz'])
    if request.method=='POST':
        k.remove(1)
        k.append(request.form.get('answer'))
        if str(k[0])==str(show_ans()[session['last_question']-1][0]):
            session['counter']+=1
    if result is None or len(result)==0:
        return redirect(url_for('result'))
    else:
        session['last_question'] = result[0]
        return '<h1>'+ str(result[1]) + '</h1>' + '<img src="/static/images/'+str(result[3])+'">'+'<form method="post" action="/test"><p><b>Введите ответ:  <input type="text" name="answer" maxlength="40" size="25" ></b></p><input type="submit" value="Отправить ответ и перейти к следующему вопросу"></form>'


def result():
    return '<html><head><title>Результаты тестирования</title></head><body class="wall"><h1>Вы завершили прохождение теста. Процент выполнения: '+str((session['counter'])*20)+'%</h1></body></html>' + '<a href="http://127.0.0.1:5000/">Вернуться на главную</a>'



app = Flask(__name__)

app.add_url_rule('/','index',index)
app.add_url_rule('/1','index',index)
app.add_url_rule('/2','index2',index2)
app.add_url_rule('/quest','quest', quest, methods=['post','get'])
app.add_url_rule('/test','test', test, methods=['post','get'])
app.add_url_rule('/result','result', result)
app.config['SECRET_KEY']='Deepestpurplest'
if __name__ == "__main__":
    app.run(host=('0.0.0.0'))