git config --global user.email "sasha547@ya.ru"
git config --global user.name "AlxndrBo"
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test.conf
sudo ln -sf /home/box/web/hello.py  /usr/lib/python2.7/dist-packages/gunicorn/app/hello.py
sudo /etc/init.d/gunicorn restart
