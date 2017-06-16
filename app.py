from cgi import parse_qs
html = """Введите значения в интервале от 0 до 1 в формате '0.1'.<br>
<form method="get">С кредитом?<input name="Answer1"></input><br>
<form method="get">Премиум карта?<input name="Answer2"></input><br>
<form method="get">Экспресс оформление?<input name="Answer3"></input><br>
<form method="get">Накопительная ?<input name="Answer4"></input><br>
<form method="get">С cash back?<input name="Answer5"></input><br>
<form method="get">Доллары?<input name="Answer6"></input><br>
<form method="get">На физическое/юридические лицо?<input name="Answer7"></input><br>
<form method="get">MasterCard?<input name="Answer8"></input><br>
<button>OK</button></form>"""
def calc(x):
    ver_var_Debetovaya = {0:0.1, 1:1, 2:0, 3:0, 6:0, 7:1}
    ver_var_Classic = {0:0.1, 1:1, 2:0, 3:0, 6:1, 7:1}
    ver_var_Bonusnaya = {0:0.3, 1:1, 2:0, 3:0, 6:1, 7:1}
    ver_var_CashBack = {0:0.1, 1:0, 2:1, 3:0, 6:0, 8:1}
    ver_var_Rubls = {0:0.1, 1:0, 2:1, 3:0, 6:1, 8:1}
    ver_var_Na_ur_litso = {0:0.1, 1:0, 2:0, 3:1, 6:0, 7:1}
    ver_var_Korporativnaya = {0:0.1, 1:0, 2:0, 3:1, 6:1, 7:1}
    
    for i in range(0,len(x)-1):
        for j in range(0,len(ver_var_Debetovaya)-1):
            if i==list(ver_var_Debetovaya.keys())[j]:
                Debetovaya = x[i]*list(ver_var_Debetovaya.values())[j]
        for k in range(0,len(ver_var_Classic)-1):
            if i==list(ver_var_Classic.keys())[k]:
                Classic = x[i]*list(ver_var_Classic())[k]
        for l in range(0,len(ver_var_Bonusnaya)-1):
            if i==list(ver_var_Bonusnaya.keys())[l]:
                Bonusnaya = x[i]*list(ver_var_Sams_S7.values())[l]
        for m in range(0,len(ver_var_CashBack)-1):
            if i==list(ver_var_CashBack.keys())[m]:
                CashBack = x[i]*list(ver_var_CashBack.values())[m]
        for n in range(0,len(ver_var_Rubls)-1):
            if i==list(ver_var_Rubls.keys())[n]:
                Rubls = x[i]*list(ver_var_Rubls.values())[n]
        for o in range(0,len(ver_var_Na_ur_litso)-1):
            if i==list(ver_var_Na_ur_litso.keys())[o]:
                Na_ur_litso = x[i]*list(ver_var_Na_ur_litso.values())[o]
        for p in range(0,len(ver_var_Korporativnaya)-1):
            if i==list(ver_var_Korporativnaya.keys())[p]:
                Korporativnaya = x[i]*list(ver_var_Korporativnaya.values())[p]
        
    y=[str(Debetovaya),str(Classic),str(Bonusnaya),str(CashBack),str(Rubls),str(Na_ur_litso),str(Korporativnaya)]
    return y

def wsgi_app(environ, start_response): 
    response_headers = [('Content-type', 'text/html; charset=UTF-8')]
    response_body = html
    status = '200 OK'
    start_response(status, response_headers)
    yield response_body.encode()
    x = []
    good=0
    d = parse_qs(environ['QUERY_STRING'])
    Answer1 = d.get('Answer1',[None])[0]
    Answer2 = d.get('Answer2',[None])[0]
    Answer3 = d.get('Answer3',[None])[0]
    Answer4 = d.get('Answer4',[None])[0]
    Answer5 = d.get('Answer5',[None])[0]
    Answer6 = d.get('Answer6',[None])[0]
    Answer7 = d.get('Answer7',[None])[0]
    Answer8 = d.get('Answer8',[None])[0]
    x.append(Answer1)
    x.append(Answer2)
    x.append(Answer3)
    x.append(Answer4)
    x.append(Answer5)
    x.append(Answer6)
    x.append(Answer7)
    x.append(Answer8)
    if Answer1 and Answer2 and Answer3 and Answer4 and Answer5 and Answer6 and Answer7 and Answer8:
        try:
            for i in range(0,len(x)-1):
                x[i]=float(x[i])
            #y=calc(x)
            response_body=str(x[0])
            start_response(status, response_headers)
            yield response_body.encode()
        except:
            response_body="Пожалуйста, введите корректные значения.<br>"
            start_response(status, response_headers)
            yield response_body.encode()
    
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
