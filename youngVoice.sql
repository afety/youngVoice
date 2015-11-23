create database young_voice;
use young_voice;
create table article(id int not null primary key auto_increment, typeId int, title text, author varchar(32), content text, publishTime int, updateTime int);
create table admin(id int not null primary key auto_increment, username varchar(32), password varchar(32), lastTime int, lastIp varchar(20));
create table notice(id int not null primary key auto_increment, author varchar(32), title text, content text, publishTime int, updateTime int);
create table question(id int not null primary key auto_increment, title text, content text, state int, answered int, reply text, replyTime int, anwser varchar(32));
