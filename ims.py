import pyodbc
from flask import Flask,jsonify,request,render_template
app = Flask(__name__)

server = 'MADHAV\SQLEXPRESS'
database = 'newims'
driver =  '{SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};trusted_connection = yes'

conn = pyodbc.connect(connection_string)

cn = conn.cursor()

cn.execute("select * from customer")
print(cn.fetchall())

# customer_name = 'RAMAN'
# customer_addr = 'NZB'
# customer_email= 'RAMAN@GMAIL.COM'

# cn.execute(f"insert into customer(customer_name,customer_addr,customer_email)values('{customer_name}','{customer_addr}','{customer_email}')")
# conn.commit()


#main code:-----------------------------------------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/show-customers")
def customer_show():
    cn = conn.cursor()
    cn.execute("select * from customer")
    data = []
    for i in cn.fetchall():
       customer={}
       customer['customer_id'] =i[0]
       customer['customer_name']=i[1]
       customer['customer_addr']=i[2]
       customer['customer_email']=i[3]
       data.append(customer)
    print(data)

    return render_template('showcustomers.html',data=data)


#product------------------------------------

@app.route("/show-PRODUCT")
def product_show():
    cn = conn.cursor()
    cn.execute("select * from PRODUCT")
    data = []
    for i in cn.fetchall():
       PRODUCT={}
       PRODUCT['PRODUCT_id'] =i[0]
       PRODUCT['PRODUCT_name']=i[1]
       PRODUCT['PRODUCT_STOCK']=i[2]
       PRODUCT['PRODUCT_price']=i[3]
       PRODUCT['SUPPLIER_ID']=i[4]
       data.append(PRODUCT)
    print(data)

    return render_template('showproduct.html',data=data)



#supplier-------------------------

@app.route("/show-supplier")
def supplier_show():
    cn = conn.cursor()
    cn.execute("select * from supplier")
    data = []
    for i in cn.fetchall():
       supplier={}
       supplier['supplier_id'] =i[0]
       supplier['supplier_name']=i[1]
       supplier['supplier_addr']=i[2]
       supplier['supplier_email']=i[3]
       data.append(supplier)
    print(data)

    return render_template('showsupplier.html',data=data)

#orders-----------------

@app.route("/show-order")
def order_show():
    cn = conn.cursor()
    cn.execute("select * from orders")
    data = []
    for i in cn.fetchall():
       order={}
       order['order_id'] =i[0]
       order['product_id']=i[1]
       order['customer_id']=i[2]
       order['customer_email']=i[3]
       data.append(order)
    print(data)
    

    return render_template('showorder.html',data=data)




##########################################################################################################################################
#++++++++++++++++++++++++++++insert data+++++++++++++++++++++++++++++++++++++++++++++++++++++
@app.route("/add-customer",methods = ['GET','POST'])
def addcustomer():
     if request.method=='POST':
         cn = conn.cursor()
         customername=request.form.get('name')
         customeraddr=request.form.get('address' )
         customeremail=request.form.get('email')
         cn.execute(f"insert into customer(customer_name,customer_addr,customer_email)values('{customername}','{customeraddr}','{customeremail}')")
         conn.commit()
         print('Data as been inserted')
         return jsonify({'message':'sucessfull'})
     else:
         return render_template('addcustomer.html')
     




@app.route("/update-customer",methods = ['GET','POST'])    
def updatecustomer():
    if request.method=='POST':
        cn = conn.cursor()
        customerid=request.form.get('customerid')
        change=request.form.get('change')
        newvalue = request.form.get('newvalue')
        cn.execute(f"update customer set {change}='{newvalue}' where customer_id = '{customerid}'")
        conn.commit()
        print('Data as been updated')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updatecustomer.html')


#=======================add===========================================================================




@app.route("/add-product",methods = ['GET','POST'])
def addproduct():
    if request.method=='POST':
        cn = conn.cursor()
        productname=request.form.get('name')
        stock=request.form.get('stock' )
        price=request.form.get('price')
        supplierid=request.form.get('id')
        cn.execute(f"insert into product(product_name,stock,price,supplier_id)values('{productname}','{stock}','{price}','{supplierid}')")
        conn.commit()
        print('Data as been inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addproduct.html')



@app.route("/update-PRODUCT",methods = ['GET','POST'])    
def updatePRODUCT():
    if request.method=='POST':
        cn = conn.cursor()
        productid=request.form.get('productid')
        change=request.form.get('change')
        newvalue = request.form.get('newvalue')
        cn.execute(f"update product set {change}='{newvalue}' where product_id = '{productid}'")
        conn.commit()
        print('Data as been updated')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updateproduct.html')


#======================================SUPPLIER


@app.route("/add-supplier",methods = ['GET','POST'])
def addsupplier():
    if request.method=='POST':
        cn = conn.cursor()
        suppliername=request.form.get('name')
        supplieraddr=request.form.get('addr' )
        supplieremail=request.form.get('email')
        cn.execute(f"insert into supplier(supplier_name,supplier_addr,supplier_email) values('{suppliername}','{supplieraddr}','{supplieremail}')")
        conn.commit()
        print('Data as been inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addsupplier.html')
    

    
@app.route("/update-supplier",methods = ['GET','POST'])    
def updatesupplier():
    if request.method=='POST':
        cn = conn.cursor()
        supplierid=request.form.get('supplierid')
        change=request.form.get('change')
        newvalue = request.form.get('newvalue')
        cn.execute(f"update supplier set {change}='{newvalue}' where supplier_id = '{supplierid}'")
        conn.commit()
        print('Data as been updated')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updatesupplier.html')
    


#============================================================ORDERS


@app.route("/add-orders",methods = ['GET','POST'])
def addorders():
    if request.method=='POST':
        cn = conn.cursor()
        productid=request.form.get('productid')
        customerid=request.form.get('customerid' )
        quantity=request.form.get('quantity')
        print(productid,customerid,quantity)
        cn.execute(f"insert into orders(product_id,customer_id,quantity) values('{productid}','{customerid}',{quantity})")
        conn.commit()
        print('Data as been inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addorders.html')
    
    
@app.route("/update-orders",methods = ['GET','POST'])    
def updateorder():
    if request.method=='POST':
        cn = conn.cursor()
        orderid=request.form.get('order_id')
        change=request.form.get('change')
        newvalue = request.form.get('newvalue')
        cn.execute(f"update orders set {change}='{newvalue}' where orders_id = '{orderid}'")
        conn.commit()
        print('Data as been updated')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updateorder.html')
    



    #################################################delete#################################



@app.route("/delete-supplier", methods=['GET','POST'])
def deletesupplier():    
    if request.method=='POST':
        cn=conn.cursor()
        supplierid=request.form.get('supplierid')
        cn.execute(f"delete from supplier where supplier_id='{supplierid}'")
        conn.commit()
        print('Data as been Delete')
        return jsonify({'message':'sucessfull'})
    else:
        cn=conn.cursor()
        cn.execute('select * from supplier')
        data=[]
        for j in cn.fetchall():
            supplier={}
            supplier['supplier_id'] = j[0]
            supplier['supplier_name'] = j[1]
            supplier['supplier_addr'] = j[2]
            supplier['supplier_email'] = j[3]
            data.append(supplier)
        return render_template('deletesupplier.html',data=data)

if __name__=='__main__':
    app.run()

    app.run()