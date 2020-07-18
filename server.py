from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open("data_base.csv", mode="a") as data_base2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            data_base2,
            delimiter=",",
            quotechar="'",
            quoting=csv.QUOTE_MINIMAL,
            newline=""
        )
        csv_writer.writerow([email, subject, message])

@app.route("/submit_form", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "Ooops! Not Saved!"
    else:
        return "Something went wrong!"
