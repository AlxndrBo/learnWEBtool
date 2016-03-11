mysql -u root -p
mysql -u root -p create user 'pupkin'@'localhost' identified by 'pupkinpwd';
mysql -u root -p create database askdb;
mysql -u root -p grant all on askdb.* to 'test'@'localhost';
