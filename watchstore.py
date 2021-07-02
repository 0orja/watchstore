import flask
import json
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

watches = [{"id":"001", "count":0, "price": 200}]
watches = []
class watch:
    def __init__(self, id, count, price, disc_num = None, disc_price = None):
        self.id = id
        self.count = count
        self.price = price
        self.disc_num = disc_num
        self.disc_price = disc_price
    def subtotal(self):
        if self.disc_num is None:
            return self.count * self.price
        else:
            disc = self.count//self.disc_num   # number of discount groups
            rem = self.count % self.disc_num  # number of solo items left
            return disc*self.disc_price + rem*self.price

w1 = watch("001", 0, 100, 3, 200)
w2 = watch("002", 0, 80, 2, 120)
w3 = watch("003", 0, 50)
w4 = watch("004", 0, 30)

catalogue = [w1, w2, w3, w4]


def total_items(items):
    total = 0
    counts = {"001":0, "002":0, "003":0, "004":0}
    for item in items:
        if item not in counts.keys():
            raise ValueError("Watch ID not found")
        counts[item] += 1
    for watch in catalogue:
        print(counts[watch.id])
        watch.count = counts[watch.id]
        print(watch.subtotal())
        total += watch.subtotal()
    print(total)
    return total
""" Testing total_items function
items = ["001","002","001","004","003","002"]
print(total_items(items))
"""

@app.route('/', methods=["GET"])
def home():
    return "<h1>Watch Store</h1>"

@app.route('/checkout', methods=["GET", "POST"])
def checkout():
    items = request.json
    try:
        total = total_items(items)
        return json.dumps({"price": total})
    except ValueError:
        return "Watch ID not found", 400 

app.run()