
from flask import Flask,request,redirect,url_for
from flask_mail import Mail, Message
from cred import password,email,smpt2goemail



app= Flask(__name__)


# configuration of mail
#  https://www.sparkpost.com/blog/what-smtp-port/
''' using gmail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465 #25, ((587 ,466) -> for ssl)
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

'''



# smtp2go port is  #25, ((587 ,466) -> for ssl)
app.config['MAIL_SERVER'] = 'mail.smtp2go.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS'] = 1
app.config['MAIL_USERNAME'] = smpt2goemail #smpt2go enter your email
app.config['MAIL_PASSWORD'] = password    #password
app.config['MAIL_SENDER']=email   #email
mail = Mail(app)

# Alternative PORTS: 8025, 587, 80


@app.route("/splunkhook",methods=['POST','GET'])
def splunkhooks():

    if request.method =='POST':
        JsonObject=request.json
        #print(JsonObject)
        print(f"Event : {JsonObject['search_name']} Form Host : {JsonObject['result']['ComputerName']} Event code : {JsonObject['result']['EventCode']}")

        if str(JsonObject['search_name'])=='FilesCreated' :

            msg = Message(
                str('ransomware ').upper(),
                sender='naveennoob95@gmail.com',
                recipients=['mknaveen837@gmail.com']
            )
            msg.body = 'possible ransomware detected '
            mail.send(msg)
            print("Email send ............................")
        else :
            print(" ignore ")

        return 'success',200
    else :
        return 'WORKING USE POST',200  #for testing endpoint


@app.route('/')
def hello():
    return redirect(url_for('splunkhooks'))

if __name__ == '__main__':
    app.run()