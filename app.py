from flask import Flask,request,redirect,url_for
from flask_mail import Mail, Message
from cred import password,email
app= Flask(__name__)
mail = Mail(app)

# configuration of mail
#  https://www.sparkpost.com/blog/what-smtp-port/
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465 #25, ((587 ,466) -> for ssl)
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/splunkhook",methods=['POST','GET'])
def splunkhooks():

    if request.method =='POST':
        print(request.json)




        return 'success',200
    else :
        return 'WORKING USE POST',200

@app.route('/')
def hello():
    msg = Message(
        'Hello',
        sender='naveennoob95@gmail.com',
        recipients=['mknaveen837@gmail.com']
    )
    msg.body = 'Hello Flask message sent from Flask-Mail'
    mail.send(msg)

    return redirect(url_for('splunkhooks'))

if __name__ == '__main__':
    app.run()