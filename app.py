from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_sport", methods=["GET","POST"])
def add_one_sport():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into sport (name) values (:name)",hey)
        user = query_db('select * from sport')

        return render_template("sportform.html", sports=user, one_user=one_user, the_title="add new sport")


    user = query_db('select * from sport')
    one_user = query_db("select * from sport limit 1", one=True)
    return render_template("sportform.html", sports=user, one_user=one_user, the_title="add new sport")

@app.route("/add_one_musical_instrument", methods=["GET","POST"])
def add_one_musical_instrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musical_instrument (name) values (:name)",hey)
        user = query_db('select * from musical_instrument')

        return render_template("musical_instrumentform.html", musical_instruments=user, one_user=one_user, the_title="add new musical_instrument")


    user = query_db('select * from musical_instrument')
    one_user = query_db("select * from musical_instrument limit 1", one=True)
    return render_template("musical_instrumentform.html", musical_instruments=user, one_user=one_user, the_title="add new musical_instrument")

@app.route("/add_one_rule_of_game", methods=["GET","POST"])
def add_one_rule_of_game():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslessport= query_db("select * from sport")

        one_user = query_db("insert into rule_of_game (sport_id,pic,title,content,points_earned) values (:sport_id,:pic,:title,:content,:points_earned)",hey)
        user = query_db('select * from rule_of_game')

        return render_template("rule_of_gameform.html", rule_of_games=user, one_user=one_user, the_title="add new rule_of_game", touslessport=touslessport)


    touslessport= query_db("select * from sport")

    user = query_db('select * from rule_of_game')
    one_user = query_db("select * from rule_of_game limit 1", one=True)
    return render_template("rule_of_gameform.html", rule_of_games=user, one_user=one_user, the_title="add new rule_of_game", touslessport=touslessport)

@app.route("/add_one_musical_or_technical_rule", methods=["GET","POST"])
def add_one_musical_or_technical_rule():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmusical_instrument= query_db("select * from musical_instrument")

        one_user = query_db("insert into musical_or_technical_rule (musical_instrument_id,title,content,pic,points_earned) values (:musical_instrument_id,:title,:content,:pic,:points_earned)",hey)
        user = query_db('select * from musical_or_technical_rule')

        return render_template("musical_or_technical_ruleform.html", musical_or_technical_rules=user, one_user=one_user, the_title="add new musical_or_technical_rule", touslesmusical_instrument=touslesmusical_instrument)


    touslesmusical_instrument= query_db("select * from musical_instrument")

    user = query_db('select * from musical_or_technical_rule')
    one_user = query_db("select * from musical_or_technical_rule limit 1", one=True)
    return render_template("musical_or_technical_ruleform.html", musical_or_technical_rules=user, one_user=one_user, the_title="add new musical_or_technical_rule", touslesmusical_instrument=touslesmusical_instrument)

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,email,phone,country_id,password) values (:username,:email,:phone,:country_id,:password)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','email','phone','country_id','password']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','email','phone','country_id','password']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','email','phone','country_id','password']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_my_points_earned_sports", methods=["GET","POST"])
def add_one_my_points_earned_sports():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesrules_of_game= query_db("select * from rules_of_game")

        one_user = query_db("insert into my_points_earned_sports (user_id,rules_of_game_id,points_earned) values (:user_id,:rules_of_game_id,:points_earned)",hey)
        user = query_db('select * from my_points_earned_sports')

        return render_template("my_points_earned_sportsform.html", my_points_earned_sportss=user, one_user=one_user, the_title="add new my_points_earned_sports", touslesuser=touslesuser, touslesrules_of_game=touslesrules_of_game)


    touslesuser= query_db("select * from user")

    touslesrules_of_game= query_db("select * from rules_of_game")

    user = query_db('select * from my_points_earned_sports')
    one_user = query_db("select * from my_points_earned_sports limit 1", one=True)
    return render_template("my_points_earned_sportsform.html", my_points_earned_sportss=user, one_user=one_user, the_title="add new my_points_earned_sports", touslesuser=touslesuser, touslesrules_of_game=touslesrules_of_game)

@app.route("/add_one_my_points_earned_music", methods=["GET","POST"])
def add_one_my_points_earned_music():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslestechnical_rule= query_db("select * from technical_rule")

        one_user = query_db("insert into my_points_earned_music (user_id,technical_rule_id,points_earned) values (:user_id,:technical_rule_id,:points_earned)",hey)
        user = query_db('select * from my_points_earned_music')

        return render_template("my_points_earned_musicform.html", my_points_earned_musics=user, one_user=one_user, the_title="add new my_points_earned_music", touslesuser=touslesuser, touslestechnical_rule=touslestechnical_rule)


    touslesuser= query_db("select * from user")

    touslestechnical_rule= query_db("select * from technical_rule")

    user = query_db('select * from my_points_earned_music')
    one_user = query_db("select * from my_points_earned_music limit 1", one=True)
    return render_template("my_points_earned_musicform.html", my_points_earned_musics=user, one_user=one_user, the_title="add new my_points_earned_music", touslesuser=touslesuser, touslestechnical_rule=touslestechnical_rule)

