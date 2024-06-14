from flask import Flask, render_template, request, redirect, url_for
from dbservice import get_all_products,get_all_sales, insert_product

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/sales')
def sales():
     sales = get_all_sales()
     
     print("Sales fetched:", sales)  # This will print the list of sales once
     return render_template('sales.html', sales=sales)
     products = get_all_products()
     print("Products fetched:", products)  # This will print the list of products once
 
     return render_template('products.html', products=products)

@app.route('/products')
def products():
    products = get_all_products()
    print("Products fetched:", products)  # This will print the list of products once
 
    return render_template('products.html', products=products)



@app.route('/add_products', methods=["POST", "GET"])
def add_products():
    if request.method == "POST":
        # Get form data using the name attribute and request function inside Flask
        pname = request.form['product_name']
        pprice = request.form['product_price']
        
        # Insert to database
        insert_product (pname, pprice)
       
        
        return redirect(url_for('products'))
    
   
app.run(debug=True)




