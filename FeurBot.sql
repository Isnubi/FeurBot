create table guilds
(
    guild_id        varchar(150) not null,
    guild_name      varchar(500) not null,
    welcome_channel varchar(150) null,
    system_channel  varchar(150) null
);

create table users
(
    user_id         varchar(150)         not null
        primary key,
    user_name       varchar(500)         null,
    guild_id        varchar(150)         null,
    user_level      int        default 0 null,
    user_experience int        default 0 null,
    user_money      int                  null,
    `user_is-daily` tinyint(1) default 0 null
);