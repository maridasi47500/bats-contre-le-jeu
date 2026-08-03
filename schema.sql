CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists sport(
        id integer primary key autoincrement,
        name text
                    );
create table if not exists musical_instrument(
        id integer primary key autoincrement,
        name text
                    );
create table if not exists rule_of_game(
        id integer primary key autoincrement,
        sport_id text,
            pic text,
            title text,
            content text,
            points_earned text
                    );
create table if not exists musical_or_technical_rule(
        id integer primary key autoincrement,
        musical_instrument_id text,
            title text,
            content text,
            pic text,
            points_earned text
                    );
create table if not exists user(
        id integer primary key autoincrement,
        username text,
            email text,
            phone text,
            country_id text,
            password text
                    );
create table if not exists country(
        id integer primary key autoincrement,
        name text
                    );
create table if not exists my_points_earned_sports(
        id integer primary key autoincrement,
        user_id text,
            rules_of_game_id text,
            points_earned text
                    );
create table if not exists my_points_earned_music(
        id integer primary key autoincrement,
        user_id text,
            technical_rule_id text,
            points_earned text
                    );
