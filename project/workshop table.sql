
create table customer(name varchar(20),Account_id int,grade varchar(10), gender varchar(10),address varchar(10),age int,primary key(Account_id));
create table Employee(name varchar(20),Account_id int,workload int,primary key(Account_id));
create table Manager(name varchar(20),Account_id int,primary key(Account_id));
create table Account(Account_id int,password int,primary key(Account_id));
create table VIP(Account_id int,Point int,primary key(Account_id));
create table StoreAccount(Date date,Profit int,primary key(Date));
create table Orderforgoods(Order_id int,Goods_Amount int,cost int,Goods_Name varchar(20),Address varchar(10),Date date,Customer_id int,employee_id varchar(20),primary key(Order_id));
create table Goods(Goods_id int,type varchar(10),Goods_Name varchar(20),price int,Goods_Amount int,Sale_Amount int,primary key(Goods_id));
create table shoppingcart(Goods_Name varchar(20),Goods_Amount int,primary key(Goods_Name));
create table Login(Account_id int,name varchar(20),passward int,primary key(Account_id));
create table have(Account_id int,Order_id int,Customer_Name varchar(20),Employee_Name varchar(20),Manager_Name varchar(20),primary key(Account_id,Order_id));
create table Order_Goods(Order_id int,Goods_id int,Goods_name varchar(20),price int,primary key(Order_id,Goods_id));
create table Manage(Account_id int,Manager_Name varchar(20),Employee_Name varchar(20),primary key(Account_id));
create table Service(Account_id int,Employee_Name varchar(20),Manager_Name varchar(20),customer_Name varchar(20),primary key(Account_id));
create table Buy(Account_id int,Customer_Name varchar(20),Employee_Name varchar(20),Goods_id int,Goods_Amount int,primary key(Account_id,Goods_id));
create table checkout(Account_id int,Manager_Name varchar(20),Date date,Profit int,primary key(Account_id));
create table apply(Account_id int,Goods_name varchar(20),Customer_Name varchar(20),Goods_Amount int,primary key(Account_id));