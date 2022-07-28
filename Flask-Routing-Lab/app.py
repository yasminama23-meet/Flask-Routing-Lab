from flask import Flask, jsonify, request, render_template, url_for

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)


@app.route('/home')  # '/' for the default page
def home():
    return render_template('home.html')



@app.route('/')  # '/' for the default page
def x():
    return render_template('home.html')
   


@app.route('/about')  # '/' for the default page
def cart():
    return render_template('cart.html')


@app.route('/product')  # '/' for the default page
def product():
    return render_template('product.html')
   


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)

