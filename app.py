from flask import Flask,jsonify,request,render_template
app = Flask(__name__)
import sqlite3



def idgenerator(tab):    
    conn = sqlite3.connect('ims.db')
    cn = conn.cursor()
    idval = ''
    if tab=='CUSTOMER':
        idval = 'CUSTOMER_ID'
    if tab=='PRODUCT':
        idval = 'PRODUCT_ID'
    if tab=='ORDERS':
        idval = 'ORDER_ID'
    if tab=='SUPLIER':
        idval = 'SUPLIER_ID'
    print(tab,idval)
    cn.execute(f"SELECT {idval} FROM {tab}")
    new = cn.fetchall()
    cud = str(new[len(new)-1][0])
    for i in range(len(str(cud))):
        if cud[i].isnumeric():
            f = i
            break
    myint = cud[f:]
    myint = int(myint)+1
    return idval[0:3]+str(myint)

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
    conn = sqlite3.connect('ims.db')
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
    conn = sqlite3.connect('ims.db')
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
    conn = sqlite3.connect('ims.db')
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
    conn = sqlite3.connect('ims.db')
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
     conn = sqlite3.connect('ims.db')
     if request.method=='POST':
         cn = conn.cursor()
         customername=request.form.get('name')
         customeraddr=request.form.get('address' )
         customeremail=request.form.get('email')
         id = idgenerator('CUSTOMER')
         cn.execute(f"insert into customer(customer_id,customer_name,customer_addr,customer_email)values('{id}','{customername}','{customeraddr}','{customeremail}')")
         conn.commit()
         print('Data as been inserted')
         return jsonify({'message':'sucessfull'})
     else:
         return render_template('addcustomer.html')
     




@app.route("/update-customer",methods = ['GET','POST'])    
def updatecustomer():
    conn = sqlite3.connect('ims.db')
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
    conn = sqlite3.connect('ims.db')
    if request.method=='POST':
        cn = conn.cursor()
        productname=request.form.get('name')
        stock=request.form.get('stock' )
        price=request.form.get('price')
        supplierid=request.form.get('id')
        id = idgenerator('PRODUCT')
        cn.execute(f"insert into product(product_id,product_name,stock,price,supplier_id)values('{id}','{productname}','{stock}','{price}','{supplierid}')")
        conn.commit()
        print('Data as been inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addproduct.html')



@app.route("/update-PRODUCT",methods = ['GET','POST'])    
def updatePRODUCT():
    conn = sqlite3.connect('ims.db')
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
    conn = sqlite3.connect('ims.db')
    if request.method=='POST':
        cn = conn.cursor()
        suppliername=request.form.get('name')
        supplieraddr=request.form.get('addr' )
        supplieremail=request.form.get('email')
        id = idgenerator('SUPPLIER')
        cn.execute(f"insert into supplier(supplier_id,supplier_name,supplier_addr,supplier_email) values('{id}','{suppliername}','{supplieraddr}','{supplieremail}')")
        conn.commit()
        print('Data as been inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addsupplier.html')
    

    
@app.route("/update-supplier",methods = ['GET','POST'])    
def updatesupplier():
    conn = sqlite3.connect('ims.db')
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
    conn = sqlite3.connect('ims.db')
    if request.method=='POST':
        cn = conn.cursor()
        productid=request.form.get('productid')
        customerid=request.form.get('customerid' )
        quantity=request.form.get('quantity')
        id = idgenerator('ORDERS')
        print(productid,customerid,quantity)
        cn.execute(f"insert into orders(order_id,product_id,customer_id,quantity) values('{id}','{productid}','{customerid}',{quantity})")
        conn.commit()
        print('Data as been inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addorders.html')
    
    
@app.route("/update-orders",methods = ['GET','POST'])    
def updateorder():
    conn = sqlite3.connect('ims.db')
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
    conn = sqlite3.connect('ims.db')    
    if request.method=='POST':
        cn=conn.cursor()
        supplierid=request.form.get('supplierid')
        cn.execute(f"delete from supplier where supplier_id='{supplierid}'")
        conn.commit()
        print('Data as been Delete')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('deletesupplier.html')
    




            
@app.route('/delete-customer',methods =['GET','POST'])
def deletecustomer():
    conn = sqlite3.connect('ims.db')
    if request.method=='POST':
        cn=conn.cursor()
        CUSTOMER_ID=request.form.get("customerid")
        cn.execute(f"DELETE FROM CUSTOMER WHERE customer_id = '{CUSTOMER_ID}'")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('deletecustomer.html')




                
@app.route('/delete-product',methods =['GET','POST'])
def deleteproduct():
    conn = sqlite3.connect('ims.db')
    if request.method=='POST':
        cn=conn.cursor()
        product_id=request.form.get("productid")
        cn.execute(f"DELETE FROM product WHERE product_id = '{product_id}'")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('deleteproduct.html')




@app.route('/delete-orders',methods =['GET','POST'])
def deleteorders():
    conn = sqlite3.connect('ims.db')
    if request.method=='POST':
        cn=conn.cursor()
        order_id=request.form.get("orderid")
        cn.execute(f"DELETE FROM orders WHERE order_id = '{order_id}'")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('deleteorders.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5002,debug=False)