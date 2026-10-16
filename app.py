
from flask import Flask, render_template

app = Flask(__name__)

products = {
    1: {
        "name": "Crevette, avocat & fromage",
        "description": "Sushi aux crevettes, avocat et fromage.",
        "price": 21,
        "image": "images/844684451_946405118151474_3432577056852962605_n.jpg"
    },
    2: {
        "name": "Crevette, concombre & fromage",
        "description": "Sushi aux crevettes, concombre et fromage.",
        "price": 20,
        "image": "images/849476763_1609711274222892_6667936430413566145_n.jpg"
    },
    3: {
        "name": "Poulet, avocat & fromage",
        "description": "Sushi au poulet, avocat et fromage.",
        "price": 20,
        "image": "images/849550158_995083413641899_1238495075351724402_n.jpg"
    },
    4: {
        "name": "Poulet, concombre & fromage",
        "description": "Sushi au poulet, concombre et fromage.",
        "price": 19,
        "image": "images/850736319_1128435336778406_2112592734505842864_n.jpg"
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/product/<int:product_id>")
def product(product_id):
    item = products.get(product_id)

    if item is None:
        return "Produit introuvable", 404

    return render_template("product.html", **item)

if __name__ == "__main__":
    app.run(debug=True)
