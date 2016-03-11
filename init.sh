git config --global user.email "sasha547@ya.ru"
git config --global user.name "AlxndrBo"
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#=======================================================
cd /home/box/web
sudo gunicorn -D -b 0.0.0.0:8080 hello:app
cd /home/box/web/ask
sudo gunicorn -D -b 0.0.0.0:8000 ask.wsgi
#sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test.conf
#sudo ln -sf /home/box/web/hello.py  /usr/lib/python2.7/dist-packages/gunicorn/app/hello.py
#sudo /etc/init.d/gunicorn restart
#=======================================================
#mysql -u root -p
#mysql -u root -p create user 'pupkin'@'localhost' identified by 'pupkinpwd';
#mysql -u root -p create database askdb;
#mysql -u root -p grant all on askdb.* to 'test'@'localhost';
#=======================================================
