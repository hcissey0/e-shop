create database if not exists eshop_db;

create user if not exists 'eshop_user'@'localhost' identified by 'eshop_pass';

grant all privileges on eshop_db.* to 'eshop_user'@'localhost';

flush privileges;
