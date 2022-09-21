create database FeurBot;

create user 'FeurBot'@'localhost' identified by 'FeurBot';
grant all privileges on FeurBot.* to 'FeurBot'@'localhost';
flush privileges;

use FeurBot;

create table guilds
(
    guild_id        varchar(150) not null
        primary key,
    guild_name      varchar(500) not null,
    welcome_channel varchar(150) null,
    system_channel  varchar(150) null
);

create table users
(
    user_id         varchar(150)         not null
        primary key,
    user_name       varchar(500)         not null,
    guild_id        varchar(150)         not null,
    user_level      int        default 1 not null,
    user_experience int        default 0 not null,
    user_money      int        default 100 not null,
    `user_is-daily` tinyint(1) default 1 not null
);

create table pnj
(
    guild_id   varchar(150) not null,
    channel_id varchar(150) not null,
    pnj_id     int not null auto_increment
        primary key,
    pnj_name   varchar(150) not null,
    pnj_image  varchar(500) null
);