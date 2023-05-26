from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from models import Team, Tournament, User, Standings
from flask_app import db
import json
import requests

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    response = requests.get('https://pavanartim.pythonanywhere.com/')
    ban = response.json().get('data')
    ban2 = response.json()
    res = requests.post('https://pavanartim.pythonanywhere.com/topmkd', json=ban2)
    ban3 = res.json().get('data')

    options = ['1','2','3']
    filenames = ['1.png','2.png','3.jpeg']
    from models import MyModel
    my_model = MyModel.query.first()
    if not my_model:
        my_model = MyModel(stage='Welcome')
        db.session.add(my_model)
        db.session.commit()
    stage = my_model.stage
    if request.method == 'POST':
            mon1 = request.form.get('mon1')
            mon2 = request.form.get('mon2')
            mon3 = request.form.get('mon3')
            mon4 = request.form.get('mon4')
            mon5 = request.form.get('mon5')
            mon6 = request.form.get('mon6')

            entered_team = Team.query.filter_by(user_id=current_user.id).first()
            if(entered_team):
                if(mon1):
                    entered_team.mon1 = mon1
                if(mon2):
                    entered_team.mon2 = mon2
                if(mon3):
                    entered_team.mon3 = mon3
                if(mon4):
                    entered_team.mon4 = mon4
                if(mon5):
                    entered_team.mon5 = mon5
                if(mon6):
                    entered_team.mon6 = mon6
                db.session.commit()
                flash('Team changed!', category='success')
            else:
                if mon1 and mon2 and mon3 and mon4 and mon5 and mon6:
                    new_team = Team(mon1=mon1,mon2=mon2,mon3=mon3,mon4=mon4,mon5=mon5,mon6=mon6, user_id=current_user.id)  #providing the schema for the team
                    db.session.add(new_team)
                    db.session.commit()
                    flash('Team added!', category='success')
                else:
                    flash('Trainer, You need 6 Pokemon to begin!', category='error')
    return render_template("home.html", user=current_user, current_stage=stage, options=options, filenames=filenames, zip=zip, str=str, eval=eval, ban=ban, ban3=ban3)


@views.route('/delete-team', methods=['POST'])
def delete_team():
    team = json.loads(request.data) # this function expects a JSON from the INDEX.js file
    teamId = team['teamId']
    team = Team.query.get(teamId)
    if team:
        if team.user_id == current_user.id:
            db.session.delete(team)
            db.session.commit()
    return jsonify({})

@views.route('/tournament', methods=['GET','POST'])
@login_required
def tourney():
    submitted = 0
    #hard code for now

    #move this to admin later

    player = current_user.first_name
    tour = Tournament.query.first()
    pairings = tour.pairings
    for pairing in pairings:
            if pairing[0] == player:
                opponent = pairing[2]
            elif pairing[2] == player:
                opponent = pairing[0]
    opponent_string = opponent
    opponent = User.query.filter_by(first_name=opponent).first()
    #Update already_played matrix
    standings = Standings.query.first()
    matrix = standings.already_played

    # Find the indices of User A and User B based on first_name
    user_a_index = None
    user_b_index = None

    first_name_a = player
    first_name_b = opponent.first_name

    for i, row in enumerate(matrix):
        if row[0] == first_name_a:
            user_a_index = i
        if row[0] == first_name_b:
            user_b_index = i

    # Update the matrix if User A and User B are found
    if user_a_index is not None and user_b_index is not None:
        matrix[user_a_index][user_b_index] = 1
        matrix[user_b_index][user_a_index] = 1

        # Save the updated matrix
    standings.already_played = matrix
    db.session.commit()

    return render_template("tournament.html", user=current_user, zip=zip, str=str, eval=eval, opponent = opponent, submitted=submitted)

    if request.method == 'POST':
        score= request.form.get('score')
        standings = Standings.query.filter_by(user_id=current_user.id).first()
        standings.scores = score
        db.session.commit()
        return render_template("tournament.html", user=current_user, zip=zip, str=str, eval=eval, opponent = opponent, submitted=submitted, score=score)


@views.route('/next-round-admin', methods=['GET', 'POST'])
@login_required
def nextround():
    from models import MyModel2
    no_more_check_ins = MyModel2(stage2=1)
    db.session.add(no_more_check_ins)
    db.session.commit()
    #ready the request params for pavanartim and send, hard-coded for now
    if request.method == 'POST':
        pairings = [
        ["Pmkd42", 10, "Kayne98", 8]
        ]
        #response = requests.get('https://pavanartim.pythonanywhere.com/pairings')
        #pairings = response.json().get('pairings')
        tourney_ex = Tournament(pairings)
        db.session.add(tourney_ex)
        db.session.commit()

        matrix_size = len(pairings)
        already_played_matrix = [[0] * matrix_size for _ in range(matrix_size)]
        new_round = Standings(already_played = already_played_matrix, scores=1)
        db.session.add(new_round)
        db.session.commit()
    return render_template("nextround.html", user=current_user, stage2=1)

@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    from models import MyModel
    my_model = MyModel.query.first()
    stage = my_model.stage

    if request.method == 'GET':
        ign = current_user.first_name
        if (ign == "Pmkd42"):
            return render_template("admin.html", user=current_user, current_stage=stage)
        else:
            flash("Not and Admin!", category='error')
            return redirect("/")
    else:
        stage = request.form.get('my_button')
        if (stage == 'Welcome'):
            stage = 'Battle'
            my_model.stage='Battle'
            db.session.commit()
        else:
            stage = 'Welcome'
            my_model.stage='Welcome'
            db.session.commit()
        return render_template("admin.html", user=current_user, current_stage=stage)

