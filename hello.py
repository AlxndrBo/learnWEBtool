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


def app (environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    resp = environ['QUERY_STRING'].split("&")
    resp = [item+"\r\n" for item in resp]
    return resp
