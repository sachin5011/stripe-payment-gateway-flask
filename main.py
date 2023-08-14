
from flask import Flask, render_template, redirect
import yaml
import stripe

with open("config.yaml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

secret_key = data["payment_secret_key"]

stripe.api_key = secret_key
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/product-detail")
def productdetail():
    return render_template("product-detail.html")

@app.route("/success-page")
def success():
    return render_template("success.html")

@app.route("/cancle-page")
def cancle():
    return render_template("cancle.html")

@app.route("/buy-now", methods=["POST"])
def buynow():
    check_out_session = stripe.checkout.Session.create(
        line_items = [
            {
                "price" : "price_1New0iSESxH9hlX7VoLemeMd",
                "quantity" : 1
            }
        ],
        mode = "payment",
        success_url = "http://127.0.0.1:5000/success-page",
        cancel_url = "http://127.0.0.1:5000/cancle-page",
    )
    return redirect(check_out_session.url, code=3030)

if __name__ == "__main__":
    app.run(debug=True)
