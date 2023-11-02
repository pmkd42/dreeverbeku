from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from models import Team, Tournament, User, Standings, MyModel, Max_rounds_t
from flask_app import db
import json
import requests
import random
import csv
import math
from ast import literal_eval
from datetime import datetime

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    response = requests.get('https://pavanartim.pythonanywhere.com/')
    ban = response.json().get('data')
    ban2 = response.json()

    shadow_1 = 0
    shadow_2 = 0
    shadow_3 = 0
    shadow_4 = 0
    shadow_5 = 0
    shadow_6 = 0
    shadow_7 = 0
    shadow_8 = 0

    with open("/home/dreeverbeku/mysite/monlist.txt", "r") as file:
        content = file.read()
    options = eval(content)
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
            mon7 = request.form.get('mon7')
            mon8 = request.form.get('mon8')

            entered_team = Team.query.filter_by(user_id=current_user.id).first()
            if(entered_team):
                if(mon1):
                    if("shadow" in mon1):
                        entered_team.mon1_shadow = 1
                        shadow_1=1
                    else:
                        entered_team.mon1_shadow = 0
                    mon1 = mon1.replace("_shadow", "")
                    mon1 = mon1.replace("tapu_", "tapu-")
                    entered_team.mon1 = mon1
                if(mon2):
                    if("shadow" in mon2):
                        entered_team.mon2_shadow = 1
                        shadow_2=1
                    else:
                        entered_team.mon2_shadow = 0
                    mon2 = mon2.replace("_shadow", "")
                    mon2 = mon2.replace("tapu_", "tapu-")
                    entered_team.mon2 = mon2
                if(mon3):
                    if("shadow" in mon3):
                        entered_team.mon3_shadow = 1
                        shadow_3=1
                    else:
                        entered_team.mon3_shadow = 0
                    mon3 = mon3.replace("_shadow", "")
                    mon3 = mon3.replace("tapu_", "tapu-")
                    entered_team.mon3 = mon3
                if(mon4):
                    if("shadow" in mon4):
                        entered_team.mon4_shadow = 1
                        shadow_4=1
                    else:
                        entered_team.mon4_shadow = 0
                    mon4 = mon4.replace("_shadow", "")
                    mon4 = mon4.replace("tapu_", "tapu-")
                    entered_team.mon4 = mon4
                if(mon5):
                    if("shadow" in mon5):
                        entered_team.mon5_shadow = 1
                        shadow_5=1
                    else:
                        entered_team.mon5_shadow = 0
                    mon5 = mon5.replace("_shadow", "")
                    mon5 = mon5.replace("tapu_", "tapu-")
                    entered_team.mon5 = mon5
                if(mon6):
                    if("shadow" in mon6):
                        entered_team.mon6_shadow = 1
                        shadow_6=1
                    else:
                        entered_team.mon6_shadow = 0
                    mon6 = mon6.replace("_shadow", "")
                    mon6 = mon6.replace("tapu_", "tapu-")
                    entered_team.mon6 = mon6
                if(mon7):
                    if("shadow" in mon7):
                        entered_team.mon7_shadow = 1
                        shadow_7=1
                    else:
                        entered_team.mon7_shadow = 0
                    mon7 = mon7.replace("_shadow", "")
                    mon7 = mon7.replace("tapu_", "tapu-")
                    entered_team.mon7 = mon7
                if(mon8):
                    if("shadow" in mon8):
                        entered_team.mon8_shadow = 1
                        shadow_8=1
                    else:
                        entered_team.mon8_shadow = 0
                    mon8 = mon8.replace("_shadow", "")
                    mon8 = mon8.replace("tapu_", "tapu-")
                    entered_team.mon8 = mon8
                db.session.commit()
                flash('Team changed!', category='success')
            else:
                if mon1 and mon2 and mon3 and mon4 and mon5 and mon6 and mon7 and mon8:
                    if("shadow" in mon1):
                        shadow_1 = 1
                    if("shadow" in mon2):
                        shadow_2 = 1
                    if("shadow" in mon3):
                        shadow_3 = 1
                    if("shadow" in mon4):
                        shadow_4 = 1
                    if("shadow" in mon5):
                        shadow_5 = 1
                    if("shadow" in mon6):
                        shadow_6 = 1
                    if("shadow" in mon7):
                        shadow_7 = 1
                    if("shadow" in mon8):
                        shadow_8 = 1
                    mon1 = mon1.replace("_shadow", "")
                    mon1 = mon1.replace("tapu_", "tapu-")
                    mon2 = mon2.replace("_shadow", "")
                    mon2 = mon2.replace("tapu_", "tapu-")
                    mon3 = mon3.replace("_shadow", "")
                    mon3 = mon3.replace("tapu_", "tapu-")
                    mon4 = mon4.replace("_shadow", "")
                    mon4 = mon4.replace("tapu_", "tapu-")
                    mon5 = mon5.replace("_shadow", "")
                    mon5 = mon5.replace("tapu_", "tapu-")
                    mon6 = mon6.replace("_shadow", "")
                    mon6 = mon6.replace("tapu_", "tapu-")
                    mon7 = mon7.replace("_shadow", "")
                    mon7 = mon7.replace("tapu_", "tapu-")
                    mon8 = mon8.replace("_shadow", "")
                    mon8 = mon8.replace("tapu_", "tapu-")

                    entered_team = Team(mon1=mon1,mon2=mon2,mon3=mon3,mon4=mon4,mon5=mon5,mon6=mon6,mon7=mon7,mon8=mon8, mon1_shadow=shadow_1,
                    mon2_shadow=shadow_2, mon3_shadow=shadow_3, mon4_shadow=shadow_4, mon5_shadow=shadow_5, mon6_shadow=shadow_6, mon7_shadow=shadow_7, mon8_shadow=shadow_8,user_id=current_user.id)  #providing the schema for the team
                    db.session.add(entered_team)
                    db.session.commit()
                    flash('Team added!', category='success')
                else:
                    flash('Trainer, You need 8 Pokemon to begin!', category='error')
    entered_team = Team.query.filter_by(user_id=current_user.id).first()
    if(entered_team):
        return render_template("home.html", user=current_user, current_stage=stage, options=options, filenames=filenames, zip=zip, str=str, eval=eval, ban=ban, shadow_1=entered_team.mon1_shadow,
        shadow_2=entered_team.mon2_shadow,shadow_3=entered_team.mon3_shadow,shadow_4=entered_team.mon4_shadow,shadow_5=entered_team.mon5_shadow,shadow_6=entered_team.mon6_shadow,shadow_7=entered_team.mon7_shadow,shadow_8=entered_team.mon8_shadow)
    else:
        return render_template("home.html", user=current_user, current_stage=stage, options=options, filenames=filenames, zip=zip, str=str, eval=eval, ban=ban, shadow_1=0,
        shadow_2=0,shadow_3=0,shadow_4=0,shadow_5=0,shadow_6=0,shadow_7=0,shadow_8=0)

def make_team_small():
    users = User.query.all()
    for user in users:
        team = Team.query.filter_by(user_id=user.id).first()
        if team:
            if team.mon1:
                team.mon1 = team.mon1.lower()
            if team.mon2:
                team.mon2 = team.mon2.lower()
            if team.mon3:
                team.mon3 = team.mon3.lower()
            if team.mon4:
                team.mon4 = team.mon4.lower()
            if team.mon5:
                team.mon5 = team.mon5.lower()
            if team.mon6:
                team.mon6 = team.mon6.lower()
            if team.mon7:
                team.mon7 = team.mon7.lower()
            if team.mon8:
                team.mon8 = team.mon8.lower()
        db.session.commit()


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
    my_model = MyModel.query.first()
    stage = my_model.stage
    #hard code for now
    if (stage == 'Welcome'):
        return render_template("tournament_load.html", stage=stage, user=current_user)
    if (stage == 'Battle'):
        player = current_user.first_name
        filename = '/home/dreeverbeku/mysite/pairings.csv'
        pairings = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                pairings.append(row)
        #set yourelf as opponent to avoid crashing
        opponent = player
        for pairing in pairings:
                if pairing[0] == player:
                    opponent = pairing[1]
                    break
                elif pairing[1] == player:
                    opponent = pairing[0]
                    break
        opponent_string = opponent
        opponent = User.query.filter_by(first_name=opponent).first()
        dbplayer = User.query.filter_by(first_name=player).first()
        if(dbplayer.submitted):
            submitted = dbplayer.submitted
        else:
            dbplayer.submitted = 0
            submitted = 0
            db.session.commit()
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
        my_model = MyModel.query.first()
        stage = my_model.stage

        banned = current_user.banned
        if(banned == 0):
            show_ban = 1
            show_submit=0
        else:
            show_ban=0
            show_submit=1
        opp_bans = [0,0]
        random_numbers = [0,0]
        if request.method == 'GET':
            usr_team = Team.query.filter_by(user_id=current_user.id).first()
            try:
                random_numbers = json.loads(usr_team.round_bans)
            except:
                random_numbers = [0,0]
            opp_team = Team.query.filter_by(user_id=opponent.id).first()
            try:
                opp_bans = json.loads(opp_team.round_bans)
            except:
                opp_bans = [0,0]
            if(current_user.banned==0):
                random_numbers = [0,0]
                opp_bans = [0,0]
            return render_template("tournament.html", user=current_user, zip=zip, str=str, eval=eval, opponent = opponent, submitted=submitted, stage=stage, ban=show_ban, subm=show_submit, toban1=random_numbers[0], toban2=random_numbers[1], oppban1 = opp_bans[0], oppban2 = opp_bans[1])

        if request.method == 'POST':
            form_type = request.form.get('form_type')
            if form_type == 'form1':
                safe_picks = request.form['selectedImages']
                available_numbers = [x for x in range(1, 9) if str(x) not in safe_picks]
                usr_team = Team.query.filter_by(user_id=current_user.id).first()
                if(current_user.banned==0):
                    random_numbers = random.sample(available_numbers, 2)
                    roundb = []
                    if 1 in random_numbers:
                        usr_team.mon1_safe = 1
                        roundb.append(1)
                    if 2 in random_numbers:
                        usr_team.mon2_safe = 1
                        roundb.append(2)
                    if 3 in random_numbers:
                        usr_team.mon3_safe = 1
                        roundb.append(3)
                    if 4 in random_numbers:
                        usr_team.mon4_safe = 1
                        roundb.append(4)
                    if 5 in random_numbers:
                        usr_team.mon5_safe = 1
                        roundb.append(5)
                    if 6 in random_numbers:
                        usr_team.mon6_safe = 1
                        roundb.append(6)
                    if 7 in random_numbers:
                        usr_team.mon7_safe = 1
                        roundb.append(7)
                    if 8 in random_numbers:
                        usr_team.mon8_safe = 1
                        roundb.append(8)
                    dbplayer = User.query.filter_by(first_name=player).first()
                    dbplayer.banned = 1
                    usr_team.round_bans = json.dumps(roundb)
                    db.session.commit()
                else:
                    random_numbers = json.loads(usr_team.round_bans)
                    opp_team = Team.query.filter_by(user_id=opponent.id).first()
                    try:
                        opp_bans = json.loads(opp_team.round_bans)
                    except:
                        opp_bans = [0,0]

                show_ban = 0
                show_submit = 1
                #flash("Submitted Bans!", category='error')
                message = str(random_numbers[0]) + " and " + str(random_numbers[1]) + " are banned"
                flash(message, category='error')

            # Perform necessary operations for Form 2
            elif form_type == 'form2':
                dbplayer = User.query.filter_by(first_name=player).first()
                dbplayer.submitted = 1
                db.session.commit()

                usr_team = Team.query.filter_by(user_id=current_user.id).first()
                random_numbers = json.loads(usr_team.round_bans)
                submitted = 1
                new_score= int(request.form.get('form-type'))
                flash("Submitted Bans!", category='error')

                # Update the "scores" column in the table with the modified scores

                already_played = json.loads(dbplayer.already_matched)
                played = 0
                if(opponent_string in already_played):
                    played = 1
                if(played == 0):
                    existing_pairings = json.loads(dbplayer.wins)

                    # Add the integer value to the pairings
                    existing_pairings.append(new_score)

                    # Serialize the updated pairings
                    serialized_pairings = json.dumps(existing_pairings)

                    # Update the wins field in the database
                    dbplayer.wins = serialized_pairings

                    already_played.append(opponent_string)
                    ap_ser = json.dumps(already_played)
                    dbplayer.already_matched = ap_ser

                    # Updating total wins and toughness only if the user faces an opponent
                    if(dbplayer.first_name != opponent.first_name):
                        dbplayer.total_wins += new_score
                        dbplayer.toughness += new_score

                    # Need to update round_wins for users who get a bye also
                    if(new_score >=2):
                        dbplayer.round_wins += 1

                    db.session.commit()
                    print(dbplayer.first_name, " :Submitted wins: ", new_score)
                    flash("Submitted Scores succesfully!", category='success')

                else:
                    flash("Already Submitted Scores!", category='error')

            return render_template("tournament.html", user=current_user, zip=zip, str=str, eval=eval, opponent = opponent, submitted=submitted, stage=stage, ban=show_ban, subm=show_submit, toban1=random_numbers[0], toban2=random_numbers[1], oppban1 = opp_bans[0], oppban2 = opp_bans[1])


@views.route('/next-round-admin', methods=['GET', 'POST'])
@login_required
def nextround():
    if request.method == 'GET':
        users = User.query.all()
        print("Not Submitted")
        for user in users:
            # Remove the unset user from tournaments
            if(user.team_set == 0):
                continue
            elif user.submitted == 0:
                print(user.first_name)

    if request.method == 'POST':
            from models import MyModel2
            no_more_check_ins = MyModel2(stage2=1)
            db.session.add(no_more_check_ins)
            db.session.commit()

            db.session.query(User).update({User.submitted: 0})
            db.session.query(User).update({User.banned: 0})
            db.session.query(Team).update({Team.round_bans: '[0,0]'})
            db.session.commit()

            round_info = Max_rounds_t.query.first()
            next_round = round_info.current_round + 1
            round_info.current_round = next_round
            print("Current Round: ")
            print(next_round)
            db.session.commit()

            all_users = User.query.all()
            users = []
            for user in all_users:
                # Remove the unset users from tournaments
                if(user.team_set == 1):
                    users.append(user)
            file_path = '/home/dreeverbeku/mysite/master_match.csv'
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)

                # Write the header row
                writer.writerow(['ign', 'wins', 'total_wins', 'already_matched', 'toughness', 'round_wins'])

                # Write user data rows
                for user in users:
                    writer.writerow([
                        user.first_name,
                        user.wins,
                        user.total_wins,
                        user.already_matched,
                        user.toughness,
                        user.round_wins
                    ])
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                players = []
                for row in reader:
                    players.append(row)
                #create matchups based on master
                pairings = []
                played = set()
                # Sort players based on toughness first and then based on round wins, to have similar round wins sorted according to toughness (highest to lowest)
                players.sort(key=lambda x: int(x['toughness']), reverse=True)
                players.sort(key=lambda x: int(x['round_wins']), reverse=True)

                while len(players) > 1:
                    current_player = players.pop(0)
                    if(current_player['ign'] not in played):
                        opponent = None
                        for player in players:
                            if player['ign'] not in current_player['already_matched'] and player['ign'] not in played:
                                opponent = player
                                break

                        if opponent is None:
                            players.append(current_player)
                            break

                        pairings.append((current_player['ign'], opponent['ign']))
                        played.add(current_player['ign'])
                        played.add(opponent['ign'])

                if (len(players) == 1 and players[0]['ign'] not in played):
                    pairings.append((players[0]['ign'], players[0]['ign']))

                with open('/home/dreeverbeku/mysite/pairings.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    print("Writing this to pairings:")
                    for pairing in pairings:
                        print(pairing)
                        writer.writerow(pairing)

            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                players = []
                for row in reader:
                    players.append(row)
            leader = "/home/dreeverbeku/mysite/leader.csv"
            players.sort(key=lambda x: int(x['toughness']), reverse=True)
            players.sort(key=lambda x: int(x['round_wins']), reverse=True)
            with open(leader, 'w') as lead:
                writer = csv.writer(lead)
                writer.writerow(["IGN", "Wins", "TieBreakerScore"])
                for player in players:
                    ign = player["ign"]
                    toughness = player["toughness"]
                    wins = player["round_wins"]
                    row = [ign,wins,toughness]
                    writer.writerow(row)

    return render_template("nextround.html", user=current_user, stage2=1)


@views.route('/admin_update', methods=['GET', 'POST'])
@login_required
def admin_update():
    if request.method == 'GET':
        users = User.query.all()
        user_list = []
        for user in users:
            if user.team_set == 1:
                user_list.append([
                    user.first_name,
                    user.wins,
                    user.email,
                    user.total_wins,
                    user.already_matched,
                    user.toughness,
                    user.round_wins
                    ])
        ign = current_user.first_name
        if (ign == "Pmkd42" or ign == "admin"):
            return render_template("admin_update.html", json_data=user_list, user=current_user)
        else:
            flash("Not an Admin!", category='error')
            return redirect("/")


@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    from models import MyModel
    my_model = MyModel.query.first()
    stage = my_model.stage

    if request.method == 'GET':
        users = User.query.all()
        userc = 0
        for user in users:
            entered_team = Team.query.filter_by(user_id=user.id).first()
            if(entered_team and entered_team.round_bans and user.team_set == 1):
                userc = userc + 1
                print(user.first_name)
        print("Total Set Users :")
        print(userc)
        ign = current_user.first_name
        if (ign == "Pmkd42" or ign == "admin"):
            return render_template("admin.html", user=current_user, current_stage=stage)
        else:
            flash("Not an Admin!", category='error')
            return redirect("/")
    else:
        stage = request.form.get('my_button')
        if (stage == 'Welcome'):
            stage = 'Battle'
            my_model.stage='Battle'
            db.session.commit()
            db.session.query(User).update({User.submitted: 0})
            db.session.query(User).update({User.banned: 0})
            db.session.query(User).update({User.wins: '[]'})
            db.session.query(User).update({User.round_wins: 0})
            db.session.query(User).update({User.total_wins: 0})
            db.session.query(User).update({User.toughness: 0})
            db.session.query(User).update({User.already_matched: '[]'})
            db.session.commit()

            all_users = User.query.all()
            user_data = []
            userc = 0
            users = []
            for user in all_users:
                entered_team = Team.query.filter_by(user_id=user.id).first()
                # Remove the users who have not set a team
                if(entered_team and entered_team.mon1 and entered_team.mon2 and entered_team.mon3 and entered_team.mon4 and entered_team.mon5 and entered_team.mon6 and entered_team.mon7 and entered_team.mon8):
                    set_user = User.query.filter_by(first_name=user.first_name).first()
                    print(set_user.first_name)
                    set_user.team_set = 1
                    db.session.commit()
                    user_data.append({
                        'ign': user.first_name
                        # Add other attributes as per your User class
                    })
                    users.append(user)
                    userc = userc + 1
            user_data = json.dumps(user_data)

            matrix_size = userc
            already_played_matrix = [[0] * matrix_size for _ in range(matrix_size)]
            already_played_matrix = json.dumps(already_played_matrix)
            standing_zero = Standings(scores=user_data, already_played=already_played_matrix)
            db.session.add(standing_zero)
            db.session.commit()

            random.shuffle(users)
            # Create pairings
            pairings = []
            for i in range(0, len(users), 2):
                pair = [users[i].first_name]
                if i + 1 < len(users):
                    pair.append(users[i + 1].first_name)
                else:
                    # Pair the remaining user with themselves
                    pair.append(users[i].first_name)
                pairings.append(pair)

            # Write pairings to CSV
            filename = '/home/dreeverbeku/mysite/pairings.csv'
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for pairing in pairings:
                    print(pairings)
                    writer.writerow(pairing)
            file_path = '/home/dreeverbeku/mysite/master_match.csv'
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)

                # Write the header row
                writer.writerow(['ign', 'wins', 'total_wins', 'already_matched', 'toughness', 'round_wins'])

                # Write user data rows
                for user in users:
                    writer.writerow([
                        user.first_name,
                        user.wins,
                        user.total_wins,
                        user.already_matched,
                        user.toughness,
                        user.round_wins
                    ])

            player_count = matrix_size
            print("count is:", player_count)
            # We are currently running one round less for tournaments with floor logic. Instead we need to use ceil for the proper number of rounds.
            round_count = math.ceil((math.log2(player_count)))
            print("no. of rounds is ", round_count)
            round_count = Max_rounds_t(max_rounds=round_count, current_round=1)
            db.session.add(round_count)
            db.session.commit()

            # Return the CSV file as a response
            with open(filename, 'r') as file:
                csv_data = file.read()
            json_data = {
                'round': int(0),
                'standings': user_data,
                'already_played': already_played_matrix
            }
            response = requests.post('https://pavanartim.pythonanywhere.com/topmkd', json=json_data)

            pairings = response.json().get('data')
            tourney_ex = Tournament(pairings)
            db.session.add(tourney_ex)
            db.session.commit()

            already_played = response.json().get('data')
            standing_1 = Standings(already_played, pairings)
            db.session.add(standing_1)
            db.session.commit()

        else:
            stage = 'Welcome'
            my_model.stage='Welcome'
            db.session.commit()
            db.session.query(Team).update({Team.mon1: None})
            db.session.query(Team).update({Team.mon2: None})
            db.session.query(Team).update({Team.mon3: None})
            db.session.query(Team).update({Team.mon4: None})
            db.session.query(Team).update({Team.mon5: None})
            db.session.query(Team).update({Team.mon6: None})
            db.session.query(Team).update({Team.mon7: None})
            db.session.query(Team).update({Team.mon8: None})
            db.session.query(User).update({User.team_set: 0})
            db.session.commit()
        return render_template("admin.html", user=current_user, current_stage=stage)

@views.route('/delete_user', methods=['POST'])
def delete_user():
    email1 = request.json['email']
    user = User.query.filter_by(email=email1).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return 'User deleted successfully'
    return 'User not found'

@views.route('/get_detailed_users', methods=['GET'])
def get_detailed_users():
    users = User.query.all()
    toret = []
    toret.append([
            "user.first_name",
            "user.wins",
            "user.email",
            "user.total_wins",
            "user.already_matched",
            "user.toughness",
            "user.round_wins",
            "user.submitted",
            "user.banned",
            "user.team_set"
            ])
    toret.append([
            "team.id(PK)",
            "team.round_bans",
            "mons",
            "team.user_id(FK)"
            ])
        # Write user data rows
    for user in users:
        toret.append([
            user.first_name,
            user.wins,
            user.email,
            user.total_wins,
            user.already_matched,
            user.toughness,
            user.round_wins,
            user.submitted,
            user.banned,
            user.team_set
            ])
        if user.teams:
            team1 = Team.query.filter_by(user_id=user.id).first()
            toret.append([
            team1.id,
            team1.round_bans,
            team1.mon1,
            team1.mon1_shadow,
            team1.mon2,
            team1.mon2_shadow,
            team1.mon3,
            team1.mon3_shadow,
            team1.mon4,
            team1.mon4_shadow,
            team1.mon5,
            team1.mon5_shadow,
            team1.mon6,
            team1.mon6_shadow,
            team1.mon7,
            team1.mon7_shadow,
            team1.mon8,
            team1.mon8_shadow,
            team1.user_id
            ])
        else:
            toret.append(["No team set"])
    return jsonify(toret)

@views.route('/get_leaderboard', methods=['GET'])
def get_leaderboard():
    # Query all users and sort by round_wins (ascending)
    # Then, sort by toughness (ascending) as a secondary sort
    users = User.query.order_by(User.round_wins.desc(), User.toughness.desc()).all()
    user_data = []
    user_data.append([
        "first_name",
        "toughness",
        "round_wins"
        ])
    for user in users:
        user_data.append([
            user.first_name,
            user.toughness,
            user.round_wins
        ])
    return jsonify(user_data)

@views.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    toret = []
    toret.append([
            "user.first_name",
            "user.wins",
            "user.email",
            "user.total_wins",
            "user.already_matched",
            "user.toughness",
            "user.round_wins"
            ])
        # Write user data rows
    for user in users:
        toret.append([
            user.first_name,
            user.wins,
            user.email,
            user.total_wins,
            user.already_matched,
            user.toughness,
            user.round_wins
            ])
        if user.teams:
            team1 = Team.query.filter_by(user_id=user.id).first()
            toret.append('round_bans - ')
            toret.append(team1.round_bans)
            print((type(team1.round_bans)))
        else:
            toret.append([])
    return jsonify(toret)

@views.route('/take_snapshot', methods=['GET'])
def take_snapshot():
    # Create a list to store data from the database
    snapshot_data = {
        'teams': [],
        'users': []
    }
    teams = Team.query.all()
    for team in teams:
            team_data = {
                "id": team.id,
                "mon1": team.mon1,
                "mon1_shadow": team.mon1_shadow,
                "mon1_safe": team.mon1_safe,
                "mon2": team.mon2,
                "mon2_shadow": team.mon2_shadow,
                "mon2_safe": team.mon2_safe,
                "mon3": team.mon3,
                "mon3_shadow": team.mon3_shadow,
                "mon3_safe": team.mon3_safe,
                "mon4": team.mon4,
                "mon4_shadow": team.mon4_shadow,
                "mon4_safe": team.mon4_safe,
                "mon5": team.mon5,
                "mon5_shadow": team.mon5_shadow,
                "mon5_safe": team.mon5_safe,
                "mon6": team.mon6,
                "mon6_shadow": team.mon6_shadow,
                "mon6_safe": team.mon6_safe,
                "mon7": team.mon7,
                "mon7_shadow": team.mon7_shadow,
                "mon7_safe": team.mon7_safe,
                "mon8": team.mon8,
                "mon8_shadow": team.mon8_shadow,
                "mon8_safe": team.mon8_safe,
                "round_bans": team.round_bans,
                "date": str(team.date),  # Convert date to string
                "user_id": team.user_id
            }
            snapshot_data['teams'].append(team_data)

    users = User.query.all()
    for user in users:
            user_data = {
                "id": user.id,
                "email": user.email,
                "password": user.password,
                "first_name": user.first_name
                # Add other User fields as needed
            }
            snapshot_data['users'].append(user_data)

    # Save the snapshot data to a JSON file
    with open('/home/dreeverbeku/mysite/snapshot.json', 'w') as json_file:
        json.dump(snapshot_data, json_file, indent=4)

@views.route('/make_all_zero', methods=['GET'])
def make_all_zero():
            db.session.query(User).update({User.submitted: 0})
            db.session.query(User).update({User.banned: 0})
            db.session.query(Team).update({Team.round_bans: '[0,0]'})
            db.session.commit()

@views.route('/repopulate_db', methods=['GET'])
def repopulate_db():
    # Read the snapshot data from the JSON file
    with open('/home/dreeverbeku/mysite/snapshot.json', 'r') as json_file:
        snapshot_data = json.load(json_file)

        # Repopulate the database with the snapshot data for Team
        for team_data in snapshot_data['teams']:
            team_data['date'] = datetime.strptime(team_data['date'], '%Y-%m-%d %H:%M:%S')
            print(type(team_data['date']))
            team = Team(**team_data)
            db.session.add(team)

        # Repopulate the database with the snapshot data for User
        for user_data in snapshot_data['users']:
            user = User(**user_data)
            db.session.add(user)

        db.session.commit()

@views.route('/get_wronged_users', methods=['GET'])
def get_wronged_users():
    toret = []
    users = User.query.all()
    for user in users:
        entered_team = Team.query.filter_by(user_id=user.id).first()
        if(entered_team.round_bans):
            print(user.first_name)
            print(entered_team.round_bans)
    return jsonify(toret)

@views.route('/get_not_submitted_users', methods=['GET'])
def get_not_submitted_users():
    users = User.query.all()
    not_submitted_teams = []
    for user in users:
        if not user.teams:
            not_submitted_teams.append([user.first_name,user.email])
    return jsonify(not_submitted_teams)

@views.route('/get_double_submitted_users', methods=['GET'])
def get_double_submitted_users():
    round_num = int(request.json['round_num'])
    users = User.query.all()
    double_submitted_teams = []
    double_submitted_teams.append([
            "user.first_name",
            "user.wins",
            "user.total_wins",
            "user.already_matched",
            "user.toughness",
            "user.round_wins"
            ])
    for user in users:
        if len(literal_eval(user.already_matched)) > round_num:
            print(user.first_name, len(literal_eval(user.already_matched)), user.already_matched)
            double_submitted_teams.append([
                user.first_name,
                user.wins,
                user.total_wins,
                user.already_matched,
                user.toughness,
                user.round_wins
                ])
    return jsonify(double_submitted_teams)


@views.route('/get_score_not_submitted_users', methods=['GET'])
def get_score_not_submitted_users():
    round_num = int(request.json['round_num'])
    users = User.query.all()
    score_not_submitted_teams = []
    score_not_submitted_teams.append([
            "user.first_name",
            "user.wins",
            "user.total_wins",
            "user.already_matched",
            "user.toughness",
            "user.round_wins"
            ])
    for user in users:
        if len(literal_eval(user.already_matched)) < round_num:
            print(user.first_name, len(literal_eval(user.already_matched)), user.already_matched)
            score_not_submitted_teams.append([
                user.first_name,
                user.wins,
                user.total_wins,
                user.already_matched,
                user.toughness,
                user.round_wins
                ])
    return jsonify(score_not_submitted_teams)

@views.route('/update_user', methods=['PUT'])
def update_user():
    ign = request.json['ign']
    user = User.query.filter_by(first_name=ign).first()
    if user:
        if 'total_wins' in request.json:
            total_wins = request.json['total_wins']
            user.total_wins = total_wins
        if 'wins' in request.json:
            wins = request.json['wins']
            user.wins = wins
        if 'already_matched' in request.json:
            already_matched = request.json['already_matched']
            user.already_matched = already_matched
        if 'toughness' in request.json:
            toughness = request.json['toughness']
            user.toughness = toughness
        if 'round_wins' in request.json:
            round_wins = request.json['round_wins']
            user.round_wins = round_wins
        if 'banned' in request.json:
            banned = request.json['banned']
            user.banned = banned
        if 'reset_bans' in request.json:
            reset_bans = request.json['reset_bans']
            team1 = Team.query.filter_by(user_id=user.id).first()
            new_roundb = [0,0]
            team1.round_bans = json.dumps(new_roundb)
            team1.mon1_safe = 0
            team1.mon2_safe = 0
            team1.mon3_safe = 0
            team1.mon4_safe = 0
            team1.mon5_safe = 0
            team1.mon6_safe = 0
            team1.mon7_safe = 0
            team1.mon8_safe = 0
        db.session.commit()
        return 'User replaced successfully'
    return 'User not found'

@views.route('/new_user', methods=['POST'])
def new_user():
    ign = request.json['ign']
    total_wins = request.json['total_wins']
    wins = request.json['wins']
    already_matched = request.json['already_matched']
    toughness = request.json['toughness']
    round_wins = request.json['round_wins']
    mon1 = request.json['mon1']
    mon1_shadow = request.json['mon1_shadow']
    mon2 = request.json['mon2']
    mon2_shadow = request.json['mon2_shadow']
    mon3 = request.json['mon3']
    mon3_shadow = request.json['mon3_shadow']
    mon4 = request.json['mon4']
    mon4_shadow = request.json['mon4_shadow']
    mon5 = request.json['mon5']
    mon5_shadow = request.json['mon5_shadow']
    mon6 = request.json['mon6']
    mon6_shadow = request.json['mon6_shadow']
    mon7 = request.json['mon7']
    mon7_shadow = request.json['mon7_shadow']
    mon8 = request.json['mon8']
    mon8_shadow = request.json['mon8_shadow']
    submitted = request.json['submitted']
    banned = request.json['banned']
    new_user = User(first_name=ign, mon1=mon1, mon1_shadow = mon1_shadow, mon2=mon2, mon2_shadow = mon2_shadow,
                mon3=mon3, mon3_shadow = mon3_shadow, mon4=mon4, mon4_shadow = mon4_shadow, mon5=mon5, mon5_shadow = mon5_shadow,
                mon6=mon6, mon6_shadow = mon6_shadow, mon7=mon7, mon7_shadow = mon7_shadow, mon8=mon8, mon8_shadow = mon8_shadow,
                wins=wins, already_matched=already_matched, total_wins=total_wins,toughness=toughness,round_wins=round_wins, submitted=submitted,banned=banned).first()
    db.session.add(new_user)
    try:
        db.session.commit()
        return 'User added successfully'
    except Exception as e:
        db.session.rollback()
        return f'Error occurred: {str(e)}'