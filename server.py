from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary, get_cupcake_order

@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("cupcakes.csv"))

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html")

@app.route("/cupcake_individual", methods = ['GET', 'POST'])
def individual_cupcake():
    cupcakes = get_cupcakes("cupcakes.csv")
    selected_cupcake = None

    if request.method == 'POST':
        cupcake_name = request.form['cupcake_name']
        selected_cupcake = find_cupcake("cupcakes.csv", cupcake_name)

    return render_template("cupcake_individual.html", cupcakes=cupcakes, selected_cupcake=selected_cupcake)

@app.route("/order")
def order():
    cupcakes = get_cupcake_order()
    
    return render_template("order.html", cupcakes=cupcakes)

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "sorry cupcake not found."


if __name__ == '__main__':
    app.env = "developement"
    app.run(debug = True, port = 8000, host = "localhost")