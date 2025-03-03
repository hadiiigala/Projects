create database music_album_management_system;
use music_album_management_system;
create table Song
(
S_id int primary key NOT NULL,
S_name varchar(30) NOT NULL,
S_releasedate varchar(30) NOT NULL,
S_language varchar(30),
S_duration int NOT NULL
);
desc Song;
create table Label
(
L_id int primary key NOT NULL,
L_legacy int,
L_count int NOT NULL,
L_name varchar(30) NOT NULL
);
desc Label;
create table Movies
(
M_id int primary key NOT NULL,
M_name varchar(30) NOT NULL,
M_duration int,
M_location varchar(30)
);
desc Movies;
create table Albums
(
A_id int primary key NOT NULL,
A_name varchar(30) NOT NULL,
A_releasedate varchar(30) NOT NULL,
A_NoOfSongs int NOT NULL
);
desc Albums;
create table Lyrics
(
Ly_rhyme varchar(30),
Ly_language varchar(30) primary key NOT NULL,
Ly_pov varchar(30)
);
desc Lyrics;
create table Tracks
(
T_id int primary key NOT NULL,
T_count int NOT NULL
);
desc Tracks;
create table Singer
(
Si_name varchar(30) NOT NULL,
Si_age int NOT NULL,
Si_gender varchar(30) NOT NULL,
Si_rank int NOT NULL,
Si_id int primary key NOT NULL
);
desc Singer;
create table Genre
(
G_id int NOT NULL,
G_type varchar(30) NOT NULL primary key
);
desc Genre;
create table Composer
(
C_name varchar(30) NOT NULL,
C_age int NOT NULL,
C_gender varchar(30) NOT NULL,
C_id int NOT NULL primary key
);
desc Composer;
create table Reviews
(
R_rating int NOT NULL,
R_date varchar(30) NOT NULL,
R_id int NOT NULL primary key
);
desc Reviews;
create table Purchase
(
P_amount int(30) NOT NULL,
P_duration int NOT NULL check(P_duration<=12),
P_mode varchar(30) NOT NULL,
P_id int NOT NULL primary key
);
desc Purchase;
alter table Purchase
add L_id int;
alter table Purchase
add constraint fk_Purchase_Label foreign key(L_id) references Label(L_id);
alter table Movies
add L_id int;
alter table Movies
add constraint fk_Movies_Label foreign key(L_id) references Label(L_id);
alter table Song
add L_id int;
alter table Song
add constraint fk_Song_Label foreign key(L_id) references Label(L_id);
alter table Lyrics
add S_id int;
alter table Lyrics
add constraint fk_Lyrics_Song foreign key(S_id) references Song(S_id);
alter table Albums
add S_id int;
alter table Albums
add constraint fk_Albums_Song foreign key(S_id) references Song(S_id);
alter table Tracks
add S_id int;
alter table Tracks
add constraint fk_Tracks_Song foreign key(S_id) references Song(S_id);
alter table Genre
add S_id int;
alter table Genre
add constraint fk_Genre_Song foreign key(S_id) references Song(S_id);
alter table Genre
add Si_id int;
alter table Genre
add constraint fk_Genre_Singer foreign key(Si_id) references Singer(Si_id);
alter table Reviews
add S_id int;
alter table Reviews
add constraint fk_Reviews_Song foreign key(S_id) references Song(S_id);
alter table Reviews
add G_id int;
alter table Reviews
add constraint fk_Reviews_Genre foreign key(G_id) references Genre(G_id);
alter table Reviews
add M_id int;
alter table Reviews
add constraint fk_Reviews_Movies foreign key(M_id) references Movies(M_id);
alter table Reviews
add A_id int;
alter table Reviews
add constraint fk_Reviews_Albums foreign key(A_id) references Albums(A_id);
alter table Reviews
add P_id int;
alter table Reviews
add constraint fk_Reviews_Purchase foreign key(P_id) references Purchase(P_id);
alter table Reviews
add T_id int;
alter table Reviews
add constraint fk_Reviews_Tracks foreign key(T_id) references Tracks(T_id);
-- Insert correct number of values into Song table
insert into Song (S_id, S_name, S_releasedate, S_language, S_duration)
values (1, 'Popular', '20jan', 'English', 4);
insert into Song (S_id, S_name, S_releasedate, S_language, S_duration)
values (2, 'Vele', '21feb', 'Hindi', 3);
insert into Song (S_id, S_name, S_releasedate, S_language, S_duration)
values (3, 'TrueStories', '3march', 'Punjabi', 2);
select * from Song;
-- Deleting record with S_id=2
delete from Song where S_id=2;
select * from Song;
-- Update Song duration
update Song set S_duration = 5 where S_id=1;
select * from Song;
-- Update Song language
update Song set S_language = 'Mix' where S_id=1;
select * from Song;
-- Insert into Movies
insert into Movies values (401, 'Avatar', 201, 'USA');
insert into Movies values (103, 'Stree', 120, 'India');
select * from Movies;
-- Delete all movies
delete from Movies;
select * from Movies;