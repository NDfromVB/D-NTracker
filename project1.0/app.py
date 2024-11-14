import os
from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, extract_date_components

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///huge.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    return apology("TODO")



#food&drink
#food&drink
#food&drink

@app.route("/foodndrink")
@login_required
def foodndrink():
    return render_template("foodndrink/foodndrink.html", list=db.execute(
        "SELECT * FROM fridge WHERE id=? ORDER BY expiry ASC LIMIT 10", session["user_id"]
    ))

@app.route("/addfridge", methods=["GET", "POST"])
@login_required
def addfridge():
    if request.method == "POST":
        if not request.form.get("fridgename") or not request.form.get("foodname") or not request.form.get("amount") or not int(request.form.get("iyear")) or not int(request.form.get("imonth")) or not int(request.form.get("iday")) or not int(request.form.get("eyear")) or not int(request.form.get("emonth")) or not int(request.form.get("eday")):
            return apology("STOP MESSING WITH MY CODE")
        else:
            fridge_name = request.form.get("fridgename")
            food_name = request.form.get("foodname")
            amount = request.form.get("amount")
            input_date = request.form.get("iyear") + "/" + request.form.get("imonth") + "/" + request.form.get("iday")
            expiry = request.form.get("eyear") + "/" + request.form.get("emonth") + "/" + request.form.get("eday")
            if request.form.get("description"):
                description = request.form.get("description")
            else:
                description = ""
            db.execute(
                "INSERT INTO fridge (id, fridge_name, food_name, amount, input_date, expiry, description) VALUES (?,?,?,?,?,?,?)",
                 session["user_id"], fridge_name, food_name, amount, input_date, expiry, description
            )
            flash("Added a new fridge")
            return redirect("/find")
    else:
        return render_template("foodndrink/addfridge.html")


@app.route("/addfood", methods=["GET", "POST"])
@login_required
def addfood():
    if request.method == "POST":
        if not request.form.get("fridge_name"):
            return apology("Must choose a fridge")
        else:
            if not request.form.get("foodname") or not request.form.get("amount") or not int(request.form.get("iyear")) or not int(request.form.get("imonth")) or not int(request.form.get("iday")) or not int(request.form.get("eyear")) or not int(request.form.get("emonth")) or not int(request.form.get("eday")):
                return apology("STOP MESSING WITH MY CODE")
            else:
                fridge_name = request.form.get("fridge_name")
                food_name = request.form.get("foodname")
                amount = request.form.get("amount")
                input_date = request.form.get("iyear") + "/" + request.form.get("imonth") + "/" + request.form.get("iday")
                expiry = request.form.get("eyear") + "/" + request.form.get("emonth") + "/" + request.form.get("eday")
                if request.form.get("description"):
                    description = request.form.get("description")
                else:
                    description = ""
                db.execute(
                    "INSERT INTO fridge (id, fridge_name, food_name, amount, input_date, expiry, description) VALUES (?,?,?,?,?,?,?)",
                     session["user_id"], fridge_name, food_name, amount, input_date, expiry, description
                )
                flash("Added a new food")
                return redirect("/find")
    else:
        list=db.execute(
            "SELECT DISTINCT fridge_name FROM fridge WHERE id=?", session["user_id"]
        )
        return render_template("foodndrink/addfood.html", list=list)


@app.route("/find", methods=["GET", "POST"])
@login_required
def find():
    if request.method == "POST":
        func = request.form.get("clickedbutton")
        if func == "Delete":
            db.execute(
                "DELETE FROM fridge WHERE food_id=?", int(request.form.get("foodid"))
            )
            list=db.execute(
            "SELECT * FROM fridge WHERE id=?", session["user_id"]
            )
            flash("Deleted")
            return render_template("foodndrink/find.html", list=list)
        elif func == "Update":
            list=db.execute(
                "SELECT * FROM fridge WHERE food_id=?", int(request.form.get("foodid"))
            )
            iyear, imonth, iday = extract_date_components(list[0]['input_date'])
            eyear, emonth, eday = extract_date_components(list[0]['expiry'])
            return render_template("foodndrink/update.html",list=list, iyear=iyear, imonth=imonth, iday=iday, eyear=eyear, emonth=emonth, eday=eday, des=list[0]["description"],
                                   num=db.execute("SELECT DISTINCT fridge_name FROM fridge WHERE id=? AND fridge_name !=?", session["user_id"], list[0]["fridge_name"]))
        elif func == "change":
            if not request.form.get("fridge_name"):
                return apology("Must choose a fridge")
            else:
                if not request.form.get("foodname") or not request.form.get("amount") or not int(request.form.get("iyear")) or not int(request.form.get("imonth")) or not int(request.form.get("iday")) or not int(request.form.get("eyear")) or not int(request.form.get("emonth")) or not int(request.form.get("eday")):
                    return apology("STOP MESSING WITH MY CODE")
                else:
                    fridge_name = request.form.get("fridge_name")
                    food_name = request.form.get("foodname")
                    amount = request.form.get("amount")
                    input_date = request.form.get("iyear") + "/" + request.form.get("imonth") + "/" + request.form.get("iday")
                    expiry = request.form.get("eyear") + "/" + request.form.get("emonth") + "/" + request.form.get("eday")
                    if request.form.get("description"):
                        description = request.form.get("description")
                    else:
                        description = ""
                    db.execute(
                        "UPDATE fridge SET fridge_name=?, food_name=?, amount=?, input_date=?, expiry=?, description=? WHERE food_id=? ",
                         fridge_name, food_name, amount, input_date, expiry, description, int(request.form.get("foodid"))
                    )
                    flash("Updated")
                    return redirect("/find")
        else:
            return apology("STOP MESSING AROUND")
    else:
        list=db.execute(
            "SELECT * FROM fridge WHERE id=? ORDER BY fridge_name, food_name", session["user_id"]
        )
        return render_template("foodndrink/find.html", list=list)

@app.route("/rename", methods=["GET", "POST"])
@login_required
def rename():
    if request.method =="POST":
        if not request.form.get("old_fridge_name"):
            return apology("Must choose a fridge")
        else:
            db.execute(
                "UPDATE fridge SET fridge_name=? WHERE id=? AND fridge_name=?",
                request.form.get("new_fridge_name"), session["user_id"], request.form.get("old_fridge_name")
            )
            return redirect("/find")
    else:
        return render_template("foodndrink/rename.html", list=db.execute(
            "SELECT DISTINCT fridge_name FROM fridge WHERE id=?", session["user_id"]
        ))


#end of food&drink
#end of food&drink
#end of food&drink






@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username") or not request.form.get("password") or not request.form.get("confirmation"):
            return apology("YOU MUST FILL IN THE BLANK, IDIOT!")
        else:
            username = request.form.get("username")
            password = request.form.get("password")
            rows = db.execute(
                "SELECT * FROM users WHERE username = ?", request.form.get("username")
            )
            if len(rows) != 0:
                return apology("Used username")
            else:
                if request.form.get("confirmation") != password:
                    return apology("Incorrect retype password")
                else:
                    db.execute(
                        "INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password, method='pbkdf2', salt_length=16)
                    )
                    return redirect ("/")
    else:
        return render_template("register.html")


