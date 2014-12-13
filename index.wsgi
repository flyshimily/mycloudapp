import sae
import web
from model import *

urls = (
    '/', 'hello'
)
app = web.application(urls, globals())
class hello:        
    def GET(self):
        print web.input()
        return "GET hello world"
    def POST(self):
        print web.input()
        return "POST hello world"


def application(environ, start_response):
    start_response('200 ok', [('content-type', 'text/plain')])

    con = Connect()
    #res = Exec(con, 'insert into Students_Information(Student_ID) value(12346)')
    datas=Exec(con, 'SELECT * FROM  `Students_Information`')
    #for data in datas:
     #   print data
    urls = (
            '/', 'hello'
            )
    app = web.application(urls, globals())
    class hello:        
        def GET(self):
            print web.input()
            return "GET hello world"
        def POST(self):
            print web.input()
            return "POST hello world"
    #print cursor.rowcount,"rows in tatal"
    #a=hello()
    return str(datas)

    
 
