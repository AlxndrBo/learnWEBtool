mysql -u root -p
create user 'pupkin'@'localhost' identified by 'pupkinpwd';
create database askdb;
grant all on askdb.* to 'test'@'localhost';
