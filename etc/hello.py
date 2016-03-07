bind = "0.0.0.0:8080"
# или через сокет
# bind = "unix:/home/proft/projects/blog/run/blog.socket"
workers = 1
user = "www-data"
group = "www-data"
#logfile = "/home/proft/projects/blog/log/gunicorn.log"
loglevel = "info"
proc_name = "blog"
#pidfile = "/home/proft/projects/blog/gunicorn.pid"
