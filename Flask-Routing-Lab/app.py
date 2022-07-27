from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def x ():
    return render_template('home.html')
 
@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/product')
def product():
    return render_template('product.html')



@app.route('/cart/<string:name>')
def cart_name_route(name):
    return render_template(
        'cart.html', n = name)




# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
