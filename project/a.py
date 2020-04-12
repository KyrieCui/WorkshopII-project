
import datetime
import string
import pymysql
import time
import flask
from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user

from wtforms import Form, StringField, PasswordField, DateField, validators

app = Flask(__name__)

db = pymysql.connect("localhost", "root", "", "project")
cursor = db.cursor()


@app.route('/')
def index():
    return render_template('customer/customer1.html')

@app.route('/drink')
def drink():
    return render_template('customer/drink.html')

@app.route('/snack')
def snack():
    return render_template('customer/snack.html')
@app.route('/fruit')
def fruit():
    return render_template('customer/fruit.html')
@app.route('/daily')
def daily():
    return render_template('customer/daily.html')
@app.route('/sport')
def sport():
    return render_template('customer/sport.html')
@app.route('/stationery')
def stationery():
    return render_template('customer/stationery.html')

@app.route('/customer1')
def all():
    return render_template('customer/customer1.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':		
        sql = "TRUNCATE TABLE vip"
        sql1 = "TRUNCATE TABLE shoppingcart"
        cursor.execute(sql)
        db.commit()
        cursor.execute(sql1)
        db.commit()
        return redirect('./loginpage')

@app.route('/back')
def back():
	return render_template('login/login.html')

@app.route('/loginpage')
def loginpage():
	return render_template('login/login.html')	
		
@app.route('/login',methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		id = request.form['name']
		password = request.form['password']
		account_id = int(id)
		account_password = int(password)
		identity = request.form["identity"]
		db = pymysql.connect("localhost", "root", "", "project")
		with db.cursor() as cursor:
			if identity == "customer":
				sql="select name from customer where customer_id = %d" % account_id
				cursor.execute(sql)
				row = cursor.rowcount
				name = cursor.fetchone()
				if row == 1:
					sql="select password from account where Account_id = %d" % account_id
					cursor.execute(sql)
					result = cursor.fetchone()
					password_result = int(result[0])
					if password_result==account_password:
						id = request.form.get('name')
						sql = """ INSERT INTO vip(Account_id, point) VALUES('%s', '%d')""" % (id, 1)
						cursor.execute(sql)
						db.commit()
						return render_template('customer/customer1.html',name=name[0])
					else:
						message = "<p style='color:red'>Your password is Wrong! Please try again.</p>"
						return render_template('login/test.html',message=message)
				else:
					message = "<p style='color:red'>Your ID is not exist or choose the wrong identity! Please try again.</p>"
					return render_template('login/test.html',message=message)
			
			elif identity == "employee":
				sql="select name from employee where employee_id = %d" %account_id
				cursor.execute(sql)
				row = cursor.rowcount
				name = cursor.fetchone()
				if row == 1:
					sql="select password from account where Account_id = %d" %account_id
					cursor.execute(sql)
					result = cursor.fetchone()
					password_result = int(result[0])
					if password_result==account_password:
						id = request.form.get('name')
						sql = """ INSERT INTO vip(Account_id, point) VALUES('%s', '%d')""" % (id, 1)
						cursor.execute(sql)
						db.commit()
						return redirect('./employee')
					else:
						message = "<p style='color:red'>Your password is Wrong! Please try again.</p>"
						return render_template('login/test.html',message=message)
				else:
					message = "<p style='color:red'>Your ID is not exist or choose the wrong identity! Please try again.</p>"
					return render_template('login/test.html',message=message)		
			
			elif identity == "manager":
				sql="select name from manager where manager_id = %d" %account_id
				cursor.execute(sql)
				row = cursor.rowcount
				name = cursor.fetchone()
				if row == 1:
					sql="select password from account where Account_id = %d" %account_id
					cursor.execute(sql)
					result = cursor.fetchone()
					password_result = int(result[0])
					if password_result==account_password:
						id = request.form.get('name')
						sql = """ INSERT INTO vip(Account_id, point) VALUES('%s', '%d')""" % (id, 1)
						cursor.execute(sql)
						db.commit()
						return redirect('./manager')
					else:
						message = "<p style='color:red'>Your password is Wrong! Please try again.</p>"
						return render_template('login/test.html',message=message)
				else:
					message = "<p style='color:red'>Your ID is not exist or choose the wrong identity! Please try again.</p>"
					return render_template('login/test.html',message=message)

					
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register/register.html')
    else:
        username=request.form['name']
        gender=request.form['gender']
        grade=int(request.form['grade'])
        address=request.form['address']
        user_id=int(request.form['id'])
        password=int(request.form['password'])
        repeatPassword = int(request.form['repeat-password'])
        #if the repeat Password is not equal to password, register fail
        if password != repeatPassword:
            return render_template('register/register.html',message="Your repeatPassword is different")
        else:
            db = pymysql.connect("localhost", "root", "", "project")
            cur=db.cursor()
            rename="""select * from account where account_id=%d """
            n=cur.execute(rename % user_id)
            db.commit()
            #if the account_id not exist,create a new account
            if n <=0:
                sql_insert1="""insert into account values(%d,%d)"""
                cur.execute(sql_insert1 % (user_id,password))
                db.commit()
                sql_insert2="""insert into customer values('%s',%d,%d,'%s','%s',%d)"""
                cur.execute(sql_insert2 % (username,user_id,grade,gender,address,int((17+grade))))
                db.commit()
                return render_template('login/login.html')
            else:
                return render_template('login/login.html',message="Your account is existed")
    


@app.route('/1')
def customer1():
    return render_template('customer/customer1.html')

@app.route('/2')
def customer2():
    return render_template('customer/customer2.html')

@app.route('/3')
def customer3():
    return render_template('customer/customer3.html')

@app.route('/4')
def customer4():
    return render_template('customer/customer4.html')

@app.route('/add',methods=['GET', 'POST'])	
def add():
	if request.method == 'POST':
		name = request.form["add"]
		amount = request.form["number"]
		number = int(amount)
		db = pymysql.connect("localhost", "root", "", "project")
		with db.cursor() as cursor:
				sql = "INSERT INTO shoppingcart VALUES ('%s',%d)" %(name,number)
				cursor.execute(sql)
				db.commit()
				return render_template('customer/customer1.html')

				
	
@app.route('/shoppingcart',methods=['GET', 'POST'])	
def shoppingcart():
	search_result = []
	table = ""
	db = pymysql.connect("localhost", "root", "", "project")
	with db.cursor() as cursor:
		sql = "select Goods_Name,Goods_Amount from shoppingcart"
		cursor.execute(sql)
		result = cursor.fetchall()
		row = cursor.rowcount
		search_result.extend(result)			
		for i in range(0,row):
			table = "<tr>" + table
			name = ''.join(search_result[i][0])
			amount = str((search_result[i][1]))
			table = table + "<td>" + name + "</td><td>" + amount + "</td></tr>"
		return render_template('customer/shoppingcart.html',table=table)
	
	
@app.route('/search', methods=['GET', 'POST'])
def search():
    search_result = []
    if request.method == 'POST':
        keyword = request.form['keyword']
        search_result.extend(search_query(keyword))
        if len(search_result) is 0:
            #if the search information is not exist
            message='Unknown good! Please input the correct good !'
            return render_template('customer/searchResult.html',search_type=message)
        
        for row in search_result:
            search_type = search_result[0]
            search_name = search_result[1]
            search_price = search_result[2]
        return render_template('customer/searchResult.html', search_type=search_type[0], search_name=search_name[1], search_price=search_price[2])


def search_query(keyword):
    db = pymysql.connect("localhost", "root", "", "project")
    with db.cursor() as cursor:
        sql = "select type,Goods_Name,price from goods where Goods_name like '%{keyword}%'".format(
            keyword=keyword)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

@app.route('/employee')
def employee():
    db_op = DatabaseOperations()
    result = db_op.employee_order()
    return render_template('employee/employee.html', events=result)

@app.route('/deliver', methods=['GET', 'POST'])
def deliver():
    if request.method == 'POST':
        b = request.form["d"]
        a = int(b)
		
        db_op = DatabaseOperations()
        result = db_op.vip()    
		
        sql = "UPDATE orderforgoods SET employee_id = %s WHERE employee_id is NULL and Order_id = %d" % (result, a)
        sql1 = "UPDATE employee SET workload = workload + 1 WHERE employee_id = %s" % (result)
        cursor.execute(sql)
        db.commit()
        cursor.execute(sql1)
        db.commit()
        return render_template('./employee')


@app.route('/employee history')
def employee_history():
    db_op = DatabaseOperations()
    result = db_op.employee_history()
    return render_template('employee/employee history.html', events=result)

@app.route('/customer history')
def customer_history():
    db_op = DatabaseOperations()
    result = db_op.customer_history()
    return render_template('customer/customer history.html', events=result)

@app.route('/manager')
def manager():
    return render_template('manager/manager.html')

@app.route('/workload')
def workload():
    db_op = DatabaseOperations()
    result = db_op.workload()
    return render_template('manager/workload.html')
	
@app.route('/sale volume')
def sale_volume():
    db_op = DatabaseOperations()
    result = db_op.sale_volume()
    return render_template('manager/sale volume.html', events=result)

@app.route('/order',methods=['GET', 'POST'])
def order():
        search_result = []
        if request.method == 'POST':
                goodsName=[]
                amount=[]
                cost=[]
                date=time.strftime('%Y.%m.%d',time.localtime(time.time()))
                db = pymysql.connect("localhost", "root", "", "project")
                with db.cursor() as cursor:
                                sql = "select * from shoppingcart"
                                cursor.execute(sql)
                                result = cursor.fetchall()
                                row = cursor.rowcount
                                search_result.extend(result)
                                for i in range(0,row):
                                        goodsName.append(''.join(search_result[i][0]))
                                        amount.append(str((search_result[i][1])))
                                search_result = []
                                for i in range(0,row):
                                        sql_cost="select price from goods where goods.Goods_Name='%s'"%(goodsName[i])
                                        cursor.execute(sql_cost)
                                        result = cursor.fetchall()
                                        search_result.extend(result)
                                        sql_minus="update goods set Goods_Amount=Goods_Amount-%d"%(int(float(amount[i])))
                                        cursor.execute(sql_minus)
                                        db.commit()
                                        sql_plus="update goods set Sale_Amount=Sale_Amount+%d"%(int(float(amount[i])))
                                        cursor.execute(sql_plus)
                                        db.commit()
										
                                db_op = DatabaseOperations()
                                vip = db_op.vip() 
								
                                for i in range(0,row):
                                        cost.append(int(float(search_result[i][0])*float(amount[i])))
                                search_result = []
                                sql_address="select address from customer where Customer_id = %d" % (vip)
                                cursor.execute(sql_address)
                                result = cursor.fetchall()
                                search_result.extend(result)
                                address=search_result[0][0]
                                for i in range(0,row):
                                        sql_order = "INSERT INTO orderforgoods VALUES ('','%s','%s','%s','%s','%s','%s',null)" %(amount[i],cost[i],goodsName[i],address,date,vip)
                                        cursor.execute(sql_order)
                                        db.commit()
                                sql_delete="delete from shoppingcart"
                                cursor.execute(sql_delete)
                                db.commit()
                                return render_template('customer/customer1.html')
class DatabaseOperations():
    __db_url = 'localhost'
    __db_username = 'root' 
    __db_password = ''
    __db_name = 'project'
    __db = ''

    def __init__(self):
        self.__db = self.db_connect()

    def __del__(self):
        self.__db.close()

    def db_connect(self):
        self.__db = pymysql.connect(
            self.__db_url, self.__db_username, self.__db_password, self.__db_name)
        return self.__db

    def employee_order(self):
        cursor = self.__db.cursor()
        try:
            sql = 'SELECT * FROM orderforgoods WHERE employee_id is NULL'
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except Exception as e:
            return None

    def employee_history(self):
        cursor = self.__db.cursor()
        try:
            sql = "SELECT Account_id FROM vip LIMIT 1"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                id = row[0]
            sql = 'SELECT * FROM orderforgoods WHERE employee_id = %d' % (id)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            return None

    def workload(self):
        cursor = self.__db.cursor()
        try:
            sql = "SELECT * FROM employee"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except Exception as e:
            return None

    def sale_volume(self):
        cursor = self.__db.cursor()
        try:
            sql = "SELECT Goods_Name, sum(Goods_Amount), sum(cost), Date FROM orderforgoods group by Date, Goods_Name"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except Exception as e:
            return None
			
    def vip(self):
        cursor = self.__db.cursor()
        try:
            sql = "SELECT Account_id FROM vip LIMIT 1"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                id = row[0]
            return id
        except Exception as e:
            return None
			
    def customer_history(self):
        cursor = self.__db.cursor()
        try:
            sql = "SELECT Account_id FROM vip LIMIT 1"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                id = row[0]
            sql = 'SELECT * FROM orderforgoods WHERE Customer_id = %d' % (id)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            return None
