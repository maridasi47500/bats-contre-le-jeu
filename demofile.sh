
mkdir templates 
python3 scaffold.py sport name
python3 scaffold.py musical_instrument name
python3 scaffold.py rule_of_game sport_id:references pic title content points_earned
python3 scaffold.py musical_or_technical_rule musical_instrument_id:references title content pic points_earned
python3 scaffold.py user username email phone country_id:references password
python3 scaffold.py country name
python3 scaffold.py my_points_earned_sports user_id:references rules_of_game_id:references points_earned
python3 scaffold.py my_points_earned_music user_id:references technical_rule_id:references points_earned
