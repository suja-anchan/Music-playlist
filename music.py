from flask import Flask,request,render_template, redirect,session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="anchan@123"
app.config['MYSQL_DB']="world"
mysql = MySQL(app)
app.secret_key = "skeshmnbvfjjdjfjhjjj"

@app.route('/')
def first():
    return render_template('first.html')

@app.route('/second')
def second():
    return render_template('second.html')    

@app.route('/pop',methods=["GET","POST"])
def pop():
    cur=mysql.connection.cursor()
    cur.execute("select Title,Length,Artist,Album from Pop")
    data=cur.fetchall()
    cur.close()
    return render_template('pop.html',data=data)
    
@app.route('/pop2',methods=["GET","POST"])
def pop2():
    cur=mysql.connection.cursor()
    cur.execute("select * from Pop")
    data=cur.fetchall()
    cur.close()
    
    if request.method=="POST":
         sng=request.form.getlist('songs')   
         length=len(sng)
         print(sng)
         for x in range(length):
                cur=mysql.connection.cursor()
                cur.execute(f'select Title,Sharelink from pop where Title="{sng[x]}"')
                sdata=cur.fetchall()
                cur.close()
                print(data[0][0])
                print(sdata[0][1])
                cur=mysql.connection.cursor()
                cur.execute(f'''insert into playlist values("{session['Email']}","{sdata[0][0]}","{sdata[0][1]}") ''')
                mysql.connection.commit()
                cur.close()
    # return render_template('songs.html',data=sdata)

    return render_template('pop2.html',data=data)    

@app.route('/newrelease',methods=["GET","POST"])
def new():
    cur=mysql.connection.cursor()
    cur.execute("select Title,Length,Artist,Album from trending")
    data=cur.fetchall()
    cur.close()
    return render_template('newrelease.html',data=data)  

@app.route('/newrelease2',methods=["GET","POST"])
def new2():
    cur=mysql.connection.cursor()
    cur.execute("select * from trending")
    ndata=cur.fetchall()
    cur.close()
    if request.method=="POST":
         nw=request.form.getlist('new')   
         length=len(nw)
         print(nw)
         for x in range(length):
                 cur=mysql.connection.cursor()
                 cur.execute(f'select Title,Sharelink from trending where Title="{nw[x]}"')
                 mdata=cur.fetchall()
                 cur.close()
                 print(mdata[0][0])
                 print(mdata[0][1])
                 cur=mysql.connection.cursor()
                 cur.execute(f'''insert into playlist values("{session['Email']}","{mdata[0][0]}","{mdata[0][1]}") ''')
                 mysql.connection.commit()
                 cur.close()
    return render_template('newrelease2.html',data=ndata)      

@app.route('/bollywood',methods=["GET","POST"])
def bollywood():
    cur=mysql.connection.cursor()
    cur.execute("select Title,Length,Artist,Album from bollywood")
    data=cur.fetchall()
    cur.close()
    return render_template('bollywood.html',data=data)

@app.route('/bollywood2',methods=["GET","POST"])
def bollywood2():
    cur=mysql.connection.cursor()
    cur.execute("select * from bollywood")
    bdata=cur.fetchall()
    cur.close()
    if request.method=="POST":
         nw=request.form.getlist('bolly')   
         length=len(nw)
         print(nw)
         for x in range(length):
                 cur=mysql.connection.cursor()
                 cur.execute(f'select Title,Sharelink from bollywood where Title="{nw[x]}"')
                 mdata=cur.fetchall()
                 cur.close()
                 print(mdata[0][0])
                 print(mdata[0][1])
                 cur=mysql.connection.cursor()
                 cur.execute(f'''insert into playlist values("{session['Email']}","{mdata[0][0]}","{mdata[0][1]}") ''')
                 mysql.connection.commit()
                 cur.close()
    return render_template('bollywood2.html',data=bdata)


@app.route('/classical',methods=["GET","POST"])
def classical():
    cur=mysql.connection.cursor()
    cur.execute("select Title,Length,Artist,Album from classical")
    data=cur.fetchall()
    cur.close()
    
    return render_template('classical.html',data=data)

@app.route('/classical2',methods=["GET","POST"])
def classical2():
    cur=mysql.connection.cursor()
    cur.execute("select * from classical")
    data=cur.fetchall()
    cur.close()
    if request.method=="POST":
         cl=request.form.getlist('classy')   
         length=len(cl)
         print(cl)
         for x in range(length):
                 cur=mysql.connection.cursor()
                 cur.execute(f'select Title,Sharelink from classical where Title="{cl[x]}"')
                 mdata=cur.fetchall()
                 cur.close()
                 print(mdata[0][0])
                 print(mdata[0][1])
                 cur=mysql.connection.cursor()
                 cur.execute(f'''insert into playlist values("{session['Email']}","{mdata[0][0]}","{mdata[0][1]}") ''')
                 mysql.connection.commit()
                 cur.close()
    
    return render_template('classical2.html',data=data)    

@app.route('/edm',methods=["GET","POST"])
def edm():
    cur=mysql.connection.cursor()
    cur.execute("select Title,Length,Artist,Album from edm")
    data=cur.fetchall()
    cur.close()
    return render_template('edm.html',data=data)  

@app.route('/edm2',methods=["GET","POST"])
def edm2():
    cur=mysql.connection.cursor()
    cur.execute("select * from edm")
    data=cur.fetchall()
    cur.close()
    if request.method=="POST":
         cl=request.form.getlist('edm')   
         length=len(cl)
         print(cl)
         for x in range(length):
                 cur=mysql.connection.cursor()
                 cur.execute(f'select Title,Sharelink from edm where Title="{cl[x]}"')
                 mdata=cur.fetchall()
                 cur.close()
                 print(mdata[0][0])
                 print(mdata[0][1])
                 cur=mysql.connection.cursor()
                 cur.execute(f'''insert into playlist values("{session['Email']}","{mdata[0][0]}","{mdata[0][1]}") ''')
                 mysql.connection.commit()
                 cur.close()
    return render_template('edm2.html',data=data)        


@app.route('/rock',methods=["GET","POST"])
def rock():
    cur=mysql.connection.cursor()
    cur.execute("select Title,Length,Artist,Album from rock")
    data=cur.fetchall()
    cur.close()
    return render_template('rock.html',data=data)    

@app.route('/rock2',methods=["GET","POST"])
def rock2():
    cur=mysql.connection.cursor()
    cur.execute("select * from rock")
    data=cur.fetchall()
    cur.close()
    if request.method=="POST":
         cl=request.form.getlist('rck')   
         length=len(cl)
         print(cl)
         for x in range(length):
                 cur=mysql.connection.cursor()
                 cur.execute(f'select Title,Sharelink from rock where Title="{cl[x]}"')
                 mdata=cur.fetchall()
                 cur.close()
                 print(mdata[0][0])
                 print(mdata[0][1])
                 cur=mysql.connection.cursor()
                 cur.execute(f'''insert into playlist values("{session['Email']}","{mdata[0][0]}","{mdata[0][1]}") ''')
                 mysql.connection.commit()
                 cur.close()
    return render_template('rock2.html',data=data)          

#     @app.route('/loginuser',methods=['GET','POST'])
# def login():
#     render_template('loginuser.html',msg='')

@app.route('/d_albums',methods=["GET","POST"])
def d_albums():
    cur=mysql.connection.cursor()
    cur.execute("select * from Albums")
    data=cur.fetchall()
    cur.close()
    return render_template('d_albums.html',data=data)     

@app.route('/loginuser',methods =["GET","POST"])
def loginuser():
    if request.method == "POST":
        email=request.form['email']
        psw=request.form['psw']
        cur=mysql.connection.cursor()
        cur.execute(f'select * from signup where email ="{email}"')
        cusData = cur.fetchall()
        print(cusData)
        if cusData:
            if cusData[0][2] == psw:
                # session['Id'] = cusData[0][0]
                session['Name'] = cusData[0][0]
                session['Email']=cusData[0][1]
                print(session['Email'])
                return redirect('/second')

            else:
                    print("Fail")
                    return render_template('loginuser.html')
        else:
                print("No user")
        
        
    return render_template('loginuser.html')

@app.route('/logout')
def logout():
    
    session.pop('Name')
    session.pop('Email')
    return render_template('logout.html')

@app.route('/reg',methods=['GET','POST'])
def reg():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        psw = request.form['psw']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute(f'insert into signup values("{name}","{email}","{psw}","{phone}")')
        mysql.connection.commit()
        cur.close()
        
    return render_template('reg.html')

    # else:
    #      return redirect('/second')
@app.route('/songs',methods=['GET','POST'])
def songs():
    cur=mysql.connection.cursor()
    cur.execute(f'''select Title,Sharelink from playlist where email="{session['Email']}" ''')
    data=cur.fetchall()
    cur.close()
    if request.method=="POST":
         cl=request.form.getlist('play')   
         length=len(cl)
         print(cl)
         for x in range(length):
                 cur=mysql.connection.cursor()
                 cur.execute(f'''select Title,Sharelink from playlist where Title="{cl[x]}" and email="{session['Email']}"''')
                 mdata=cur.fetchall()
                 cur.close()
                 print(mdata[0][0])
                 print(mdata[0][1])
                 curs=mysql.connection.cursor()
                 curs.execute(f'''delete from playlist where Title="{mdata[0][0]}" and email="{session['Email']}" ''')
                 mysql.connection.commit()
                 curs.close()
                #  print(session['Email'])
    return render_template('songs.html',data=data)  


if __name__ == "__main__":
    app.run(debug=True,port=5015)

