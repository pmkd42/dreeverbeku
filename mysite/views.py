from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from models import Team, Tournament, User, Standings, MyModel, Max_rounds_t
from flask_app import db
import json
import requests
import random
import csv
import math

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
            mon1_copy = mon1
            mon2_copy = mon2
            mon3_copy = mon3
            mon4_copy = mon4
            mon5_copy = mon5
            mon6_copy = mon6
            mon7_copy = mon7
            mon8_copy = mon8
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
                #print("Safe picks are ",safe_picks)
                available_numbers = [x for x in range(1, 9) if str(x) not in safe_picks]
                #print("Available are ", available_numbers)
                usr_team = Team.query.filter_by(user_id=current_user.id).first()
                if(current_user.banned==0):
                    random_numbers = random.sample(available_numbers, 2)
                    copy_random_numbers = random_numbers
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
                    db.session.commit()
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

            # Perform necessary operations for Form 1
            elif form_type == 'form2':
                dbplayer = User.query.filter_by(first_name=player).first()
                dbplayer.submitted = 1
                db.session.commit()

                usr_team = Team.query.filter_by(user_id=current_user.id).first()
                random_numbers = json.loads(usr_team.round_bans)
                submitted = 1
                player_name = current_user.id
                new_score= int(request.form.get('form-type'))
                standings = Standings.query.first()
                scores = standings.scores
                #print(scores)
                #print(new_score)
                flash("Submitted Bans!", category='error')
                '''for i, entry in enumerate(scores):
                    if entry[0] == player_name:
                        scores[i][1] = new_score
                        break
                    if entry[2] == player_name:
                        scores[i][3] = new_score
                        break'''
                # Update the "scores" column in the table with the modified scores
                standings.scores = scores
                db.session.commit()

                existing_pairings = json.loads(dbplayer.wins)

                # Add the integer value to the pairings
                existing_pairings.append(new_score)

                # Serialize the updated pairings
                serialized_pairings = json.dumps(existing_pairings)

                # Update the wins field in the database
                dbplayer.wins = serialized_pairings

                # Updating total wins and toughness only if the user faces an opponent
                if(dbplayer.first_name != opponent.first_name):
                    dbplayer.total_wins += new_score
                    dbplayer.toughness += new_score

                # Need to update round_wins for users who get a bye also
                if(new_score >=2):
                    dbplayer.round_wins += 1

                already_played = json.loads(dbplayer.already_matched)
                already_played.append(opponent_string)
                ap_ser = json.dumps(already_played)
                dbplayer.already_matched = ap_ser
                db.session.commit()

                oppt = json.loads(opponent.wins)

                db.session.commit()

                #print("Enidhu ", dbplayer.already_matched, dbplayer.wins, dbplayer.total_wins, dbplayer.toughness, dbplayer.round_wins)
                flash("Submitted Scores succesfully!", category='success')
            return render_template("tournament.html", user=current_user, zip=zip, str=str, eval=eval, opponent = opponent, submitted=submitted, stage=stage, ban=show_ban, subm=show_submit, toban1=random_numbers[0], toban2=random_numbers[1], oppban1 = opp_bans[0], oppban2 = opp_bans[1])


@views.route('/next-round-admin', methods=['GET', 'POST'])
@login_required
def nextround():
    '''round_info = Max_rounds_t.query.first()
    max_rounds = round_info.max_rounds
    to_be_round = round_info.current_round + 1
    if(to_be_round > max_rounds):
        return render_template("tournament_load.html", user=current_user)
    else:'''
    if request.method == 'POST':
            from models import MyModel2
            no_more_check_ins = MyModel2(stage2=1)
            db.session.add(no_more_check_ins)
            db.session.commit()

            '''player = current_user.first_name
            dbplayer = User.query.filter_by(first_name=player).first()
            dbplayer.submitted = 0'''
            db.session.query(User).update({User.submitted: 0})
            db.session.query(User).update({User.banned: 0})
            db.session.commit()

            round_info = Max_rounds_t.query.first()
            next_round = round_info.current_round + 1
            round_info.current_round = next_round
            print("Current Round: " + next_round)
            db.session.commit()

            '''latest_entry = Standings.query.order_by(Standings.round.desc()).first()
            if latest_entry:
                # Convert the latest entry to JSON format
                json_data = latest_entry.scores
                json_data = json.dumps(json_data)
            #handle case for round1 in else
            else:
                users = User.query.all()
                user_data = []
                for user in users:
                    user_data.append({
                        'submitted': user.submitted
                # Add other attributes as per your User class
                    })
                json_data = user_data.as_dict()
                json_data = json.dumps(json_data)
            response = requests.post('https://pavanartim.pythonanywhere.com/topmkd', json=json_data)
            pairings = response.json().get('data')
            tourney_ex = Tournament(pairings)
            db.session.add(tourney_ex)
            db.session.commit()

            matrix_size = len(pairings)
            already_played_matrix = [[0] * matrix_size for _ in range(matrix_size)]
            new_round = Standings(already_played = already_played_matrix, scores=pairings)
            matrix_size = len(pairings)
            already_played_matrix = [[0] * matrix_size for _ in range(matrix_size)]
            new_round = Standings(already_played = already_played_matrix, scores=1)
            db.session.add(new_round)
            db.session.commit()'''

            users = User.query.all()
            for user in users:
                # Remove the admin user from tournaments
                if(user.first_name == "admin"):
                    users.remove(user)
                    break
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
                    print(row)
    #create matchups based on master
                pairings = []
                played = set()
                # print(players)
                # Sort players based on toughness first and then based on round wins, to have similar round wins sorted according to toughness (highest to lowest)
                players.sort(key=lambda x: int(x['toughness']), reverse=True)
                players.sort(key=lambda x: int(x['round_wins']), reverse=True)

                while len(players) > 1:
                    print("remaining players:")
                    for player in players:
                        print(player.first_name)
                    current_player = players.pop(0)
                    if(current_player['ign'] not in played):
                        print("for ", current_player['ign'])
                        opponent = None
                        print("already_matched is", current_player['already_matched'])
                        for player in players:
                            if player['ign'] not in current_player['already_matched'] and player['ign'] not in played:
                                opponent = player
                                print("opponent is", opponent)
                                break

                        if opponent is None:
                            players.append(current_player)
                            break

                        pairings.append((current_player['ign'], opponent['ign']))
                        played.add(current_player['ign'])
                        played.add(opponent['ign'])
                    else:
                        for pairing in pairings:
                            if(current_player['ign'] in pairing):
                                print(current_player['ign'], " ge Hingirutte: ",pairing)
                if (len(players) == 1 and players[0]['ign'] not in played):
                    pairings.append((players[0]['ign'], players[0]['ign']))
                with open('/home/dreeverbeku/mysite/pairings.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    print("Writing this to pairings:")
                    for pairing in pairings:
                        print(pairing)
                        writer.writerow(pairing)

    return render_template("nextround.html", user=current_user, stage2=1)

@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    from models import MyModel
    my_model = MyModel.query.first()
    stage = my_model.stage

    if request.method == 'GET':
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

            '''round_info = Max_rounds_t.query.first()
            round_info.current_round = 1
            db.session.commit()'''

            users = User.query.all()
            user_data = []
            for user in users:
                last_user = user
                # Remove the admin user from tournaments
                if(user.first_name == "admin"):
                    users.remove(user)
                else:
                    user_data.append({
                        'ign': user.first_name
            # Add other attributes as per your User class
                    })
            user_data = json.dumps(user_data)

            # Remove the admin user from tournaments
            matrix_size = last_user.id - 1
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
            #top_user = User.query.first()
            #player_count = top_user.id

            # Remove the admin user from tournaments
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
        return render_template("admin.html", user=current_user, current_stage=stage)

@views.route('/delete_user', methods=['POST'])
def delete_user():
    ign = request.json['ign']
    user = User.query.filter_by(first_name=ign).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return 'User deleted successfully'
    return 'User not found'

@views.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    toret = []
        # Write user data rows
    for user in users:
            toret.append([
                user.first_name,
                user.wins,
                user.total_wins,
                user.already_matched,
                user.toughness,
                user.round_wins
            ])
    return jsonify(toret)

@views.route('/update_user', methods=['PUT'])
def update_user():
    ign = request.json['ign']
    user = User.query.filter_by(first_name=ign).first()
    if user:
        if 'total_wins' in request.json:
            total_wins = request.json['total_wins']
            user.total_wins = total_wins
        elif 'wins' in request.json:
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