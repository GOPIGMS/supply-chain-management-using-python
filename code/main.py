from flask import Flask,render_template,request,redirect, session,url_for
import mysql.connector
import hashlib
import os
import smtplib
from twilio.rest import Client
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

UPLOAD_FOLDER = "/static/file"
app = Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
# Initialize Twilio client
account_sid = 'AC37b88798ffb16ea0c00b639df7678c81'
auth_token = '653cf56c354f94dae772101426d48476'
client = Client(account_sid, auth_token)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.urandom(24)
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="fruits1")
mycursor = mydb.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buyer')
def buyer():
    return render_template('buyer.html')

@app.route('/seller')
def seller():
    return render_template('seller.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/buy_reg')
def buy_reg():
    return render_template('buyer_reg.html')

@app.route('/sell_reg')
def sell_reg():
    return render_template('seller_reg.html')

@app.route('/buyerreg',methods=['POST','GET'])
def buyerreg():
    if request.method == 'POST':
        name = request.form.get('username')
        gender = request.form.get('gender')
        mail = request.form.get('mail')
        phone = request.form.get('phone')
        password = request.form.get('password')
        role = request.form.get('role')  # Get role from the form
        sql = "INSERT INTO buyer (`name`, `gender`, `mail`, `phone`, `password`, `acc`, `role`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (name, gender, mail, phone, password, 'no', role)  # Include role in the insert query
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('buyer.html')

@app.route('/sellerreg',methods=['POST','GET'])
def sellerreg():
    if request.method == 'POST':
        name = request.form.get('username')
        gender = request.form.get('gender')
        mail = request.form.get('mail')
        phone = request.form.get('phone')
        password = request.form.get('password')
        accno = request.form.get('accno')
        bran = request.form.get('bran')
        role = request.form.get('role')  # Get role from the form
        sql = "INSERT INTO seller (`name`, `gender`, `mail`, `phone`, `password`, `accno`, `branch`, `bal`, `role`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (name, gender, mail, phone, password, accno, bran, '0', role)  # Include role in the insert query
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('seller.html')
@app.route('/buyerval', methods=['POST', 'GET'])
def buyerval():
    if request.method == 'POST':
        name = request.form.get('username')
        upass = request.form.get('password')
        sql = 'SELECT * FROM `buyer` WHERE `name` = %s AND `password` = %s'
        val = (name, upass)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result:
            session['name'] = name
            session['role'] = result[7]  # Store role in the session
            return redirect(url_for('buy_dash'))
        else:
            return render_template('buyer.html', msg='Invalid Data')

@app.route('/sellerval',methods=['POST','GET'])
def sellerval():
    global name
    if request.method == 'POST':
        name = request.form.get('username')
        upass = request.form.get('password')
        sql = 'SELECT * FROM `seller` WHERE `name` = %s AND `password` = %s'
        val = (name, upass)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result:
            session['name'] = name
            session['role'] = result[8]  # Store role in the session
            return redirect(url_for('sell_dash'))
        else:
            return render_template('seller.html', msg = 'Invalid Data')

@app.route('/adminval',methods=['POST','GET'])
def adminval():
    if request.method == 'POST':
        name = request.form.get('username')
        upass = request.form.get('password')
        if name == 'admin' and upass == '1234':
            return redirect(url_for('admin_dash'))
        else:
            return render_template('admin.html', msg = 'Invalid Data')
@app.route('/buy_dash')
def buy_dash():
    name = session.get('name')  # Retrieving 'name' from session
    result1 = None  # Initialize result1
    if name:
        # Use name for further operations
        sql = 'SELECT * FROM `products` WHERE `seller` != %s'
        val = (name,)
        mycursor.execute(sql, val)
        result1 = mycursor.fetchall()

    if result1 is not None:
        return render_template('buy_dashboard.html', value=result1[0], data=result1)
    else:
        # Handle the case where result1 is None
        return render_template('buy_dashboard.html', value=0, data=[])


@app.route('/admin_dash')
@app.route('/buy_detail')
def admin_dash():
    sql = 'SELECT * FROM `buyer`'
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return render_template('admin_dashboard.html', data = result)

@app.route('/sell_dash')
def sell_dash():
    name = session.get('name')
    sql = 'SELECT `bal` FROM `seller` WHERE `name` = %s'
    val = (name,)
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    return render_template('sell_dashboard.html',value = result[0])

@app.route('/purchase', methods=['POST', 'GET'])
def purchase():
    name = session.get('name')
    if request.method == 'POST':
        product = request.form.get('product')
        seller = request.form.get('seller')
        rate = request.form.get('rate')

        if name is not None:
            sql = "INSERT INTO purchase (`seller`, `buyer`, `name`, `rate`) VALUES (%s, %s, %s, %s)"
            val = (seller, name, product, rate)
            mycursor.execute(sql, val)
            mydb.commit()
        else:
            print("Error: Buyer's name is None, cannot insert into the purchase table.")
            return "Error: Buyer's name is None, cannot insert into the purchase table."

        # Update buyer's account balance
        sql = 'SELECT `amount` FROM `account` WHERE `name` = %s'
        val = (name,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result is not None:  # Check if result is not None
            num = float(result[0]) - float(rate)
            sql = 'UPDATE `account` SET `amount` = %s WHERE `name` = %s'
            val = (num, name)
            mycursor.execute(sql, val)
            mydb.commit()

        # Update seller's account balance
        sql = 'SELECT `bal` FROM `seller` WHERE `name` = %s'
        val = (seller,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result is not None:  # Check if result is not None
            num = float(result[0]) + float(rate)  # Use float() instead of int()
            sql = 'UPDATE `seller` SET `bal` = %s WHERE `name` = %s'
            val = (num, seller)
            mycursor.execute(sql, val)
            mydb.commit()

        # Send SMS to buyer
        message = client.messages.create(
            body="Purchase completed for {} at rate {}.".format(product, rate),
            from_='no',  # Your Twilio number
            to='no'  # Buyer's phone number
        )
        print("SMS sent:", message.sid)

        return redirect(url_for('buy_dash'))

@app.route('/p_prod')
def p_prod():
    name = session.get('name')
    if name:
        sql = 'SELECT * FROM `purchase` WHERE `buyer` = %s'
        val = (name,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        sql = 'SELECT `amount` FROM `account` WHERE `name` = %s'
        val = (name,)
        mycursor.execute(sql, val)
        result1 = mycursor.fetchone()
        if result1:
            return render_template('purchased.html', data=result, value=result1[0])
        else:
            return render_template('purchased.html', data=result, value=0)
    else:
        return redirect(url_for('buyer'))  # Redirect to buyer page if 'name' is not in session
@app.route('/acc')
def acc():
    name = session.get('name')
    if name:
        sql = 'SELECT `acc` FROM `buyer` WHERE `name`=%s'
        val = (name,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result[0] == 'no':
            sql = 'SELECT `amount` FROM `account` WHERE `name` = %s'
            val = (name,)
            mycursor.execute(sql, val)
            result1 = mycursor.fetchone()
            if result1:
                return render_template('account.html', view='style=display:block', value=result1[0])
            else:
                return render_template('account.html', view='style=display:block', value=0)

        else:
            sql = 'SELECT * FROM `account` WHERE `name`=%s'
            val = (name,)
            mycursor.execute(sql, val)
            result = mycursor.fetchall()
            sql = 'SELECT `amount` FROM `account` WHERE `name` = %s'
            val = (name,)
            mycursor.execute(sql, val)
            result1 = mycursor.fetchone()
            if result1:
                return render_template('account.html', view1='style=display:block', data=result, value=result1[0])
            else:
                return render_template('account.html', view1='style=display:block', data=result, value=0)
    else:
        return redirect(url_for('buyer'))  # Redirect to buyer page if 'name' is not in session

@app.route('/acc_details',methods = ['POST','GET'])
def acc_details():
    if request.method == 'POST':
        name = request.form.get('name')
        accno = request.form.get('accno')
        bran = request.form.get('bran')
        amt = request.form.get('amt')
        sql = 'INSERT INTO `account` (`name`, `acc`, `branch`, `amount`) VALUES (%s, %s, %s, %s)'
        val = (name, accno, bran, amt)
        mycursor.execute(sql, val)
        mydb.commit()
        sql = 'UPDATE `buyer` SET `acc` = %s WHERE `name` = %s'
        val = ('yes', name)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for('acc'))

@app.route('/add_prod', methods=['POST', 'GET'])
def add_prod():
    if request.method == 'POST':
        name = request.form.get('name')
        sr_name = session.get('name')
        print("name_addd",name)
        print("sr_name",sr_name)
        prod_type = request.form.get('prod_type') 
        q_score = request.form.get('q_score')  # Access form field using request.form
        img = request.files['img']
        price = request.form.get('price')
        desc = request.form.get('desc')
        prod_img = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(prod_img)
        print(prod_img)
        hashid = hashlib.sha256(prod_type.encode()).hexdigest()
        sql = 'INSERT INTO `products` (`seller`, `name`, `type`, `hash`, `img`, `q_score`, `price`, `desc`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        val = (sr_name, name, prod_type, hashid, prod_img, q_score, price, desc)
        mycursor.execute(sql, val)
        mydb.commit()

        sql = 'SELECT `bal` FROM `seller` WHERE `name` = %s'
        val = (name,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        
        if result is not None:  # Check if result is not None
            return render_template('sell_dashboard.html', msg='Product Added', value=result[0])
        else:
            return render_template('sell_dashboard.html', msg='Product Added')  # Handle the case where result is None


@app.route('/sell_acc')
def sell_acc():
    name = request.form.get('name')
    name = session.get('name')
    sql = 'SELECT * FROM `seller` WHERE `name` = %s'
    val = (name,)
    mycursor.execute(sql, val)
    result1 = mycursor.fetchall()
    print("result",result1[0])
    sql = 'SELECT `bal` FROM `seller` WHERE `name` = %s'
    val = (name,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    print("Result",result[0])
    if result1:
        return render_template('sell_acc.html', value=result[0], data=result1)
    else:
        # Handle the case where result1 is empty, perhaps by returning an error message or redirecting the user.
        return "No data found: result1 is empty"

@app.route('/view')
def view():
    name = request.form.get('name')
    
    name = session.get('name')
    print("view_name",name)
    sql = 'SELECT * FROM `products` WHERE `seller` = %s'
    val = (name,)
    mycursor.execute(sql,val)
    result1 = mycursor.fetchall()
    
    sql = 'SELECT `bal` FROM `seller` WHERE `name` = %s'
    val = (name,)
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    
    if result is not None:
        return render_template('view.html', value=result[0], data=result1)
    else:
        # Handle the case where no rows were returned for the given name
        return render_template('error.html', message="No data found for the given name")



@app.route('/sell_detail')
def sell_detail():
    sql = 'SELECT * FROM `seller`'
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return render_template('admin_dashboard.html', data = result)

if __name__ == '__main__':
    app.run(debug=True,port=1234)
