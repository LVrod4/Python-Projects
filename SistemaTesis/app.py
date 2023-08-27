import sqlite3, locale
from flask import Flask, render_template, request
from datetime import date
import datetime

app = Flask(__name__)

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

@app.route('/ConstEst/')
def ConstEst():
    input_value = request.args.get('input_value')
    grado_num = int(request.args.get('grado'))
    grado_sec =int(request.args.get('seccion')) 

    if grado_num == 1:
        grado_num = 'PRIMER GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_num == 2:
        grado_num = 'SEGUNDO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_num == 3:
        grado_num = 'TERCER GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_num == 4:
        grado_num = 'CUARTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_num == 5:
        grado_num = 'QUINTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_num == 6:
        grado_num = 'SEXTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_num == 7:
        grado_num = 'PRIMER AÑO, NIVEL DE EDUCACIÓN MEDIA GENERAL'
    elif grado_num == 8:
        grado_num = 'SEGUNDO AÑO, NIVEL DE EDUCACIÓN MEDIA GENERAL'
    elif grado_num == 9:
        grado_num = 'TERCER AÑO, NIVEL DE EDUCACIÓN MEDIA GENERAL'
    else:
        return "no valid"

    if grado_sec == 1:
        grado_sec = 'A'
    elif grado_sec == 2:
        grado_sec = 'B'
    elif grado_sec == 3:
        grado_sec = 'C'
    elif grado_sec == 4:
        grado_sec = 'D'
    else:
        return "no valid"

    CurrentYear = date.today().year
    PastYear = CurrentYear - 1

    Hour = datetime.datetime.now()
    Hour = Hour.strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE StudCed=?", (input_value,))
    result = cursor.fetchone()

    if result:
        today = date.today()
        return render_template('ConstEst.html', IType=result[0], StudName=result[2], StudLast=result[3],
                               INumber=input_value, today=today, CurrentYear=CurrentYear, PastYear=PastYear, Hour=Hour,
                               grado=grado_num, seccion=grado_sec)
    

    else:
        return "Student not found"

@app.route('/ConstProsec/')
def ConstProsec():
    input_value = request.args.get('input_value')
    grado_actP = int(request.args.get('gradoAP'))
    grado_newP = int(request.args.get('gradoNP'))
    grado_lit = int(request.args.get('literal'))

    if grado_actP == 1:
        grado_actP = 'PRIMER GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_actP == 2:
        grado_actP = 'SEGUNDO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_actP == 3:
        grado_actP = 'TERCER GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_actP == 4:
        grado_actP = 'CUARTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_actP == 5:
        grado_actP = 'QUINTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_actP == 6:
        grado_actP = 'SEXTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    else:
        return "no valid"
    
    if grado_newP == 1:
        grado_newP = 'PRIMER GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_newP == 2:
        grado_newP = 'SEGUNDO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_newP == 3:
        grado_newP = 'TERCER GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_newP == 4:
        grado_newP = 'CUARTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_newP == 5:
        grado_newP = 'QUINTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_newP == 6:
        grado_newP = 'SEXTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_newP == 7:
        grado_newP = 'PRIMER AÑO, NIVEL MEDIA GENERAL'
    else:
        return "no valid"
    
    if grado_lit == 1:
        grado_lit = 'A'
    elif grado_lit == 2:
        grado_lit = 'B'
    elif grado_lit == 3:
        grado_lit = 'C'
    elif grado_lit == 4:
        grado_lit = 'D'
    else:
        return "no valid"
    
    CurrentYear = date.today().year
    PastYear = CurrentYear - 1

    Hour = datetime.datetime.now()
    Hour = Hour.strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE StudCed=?", (input_value,))
    result = cursor.fetchone()

    if result:
        today = date.today()
        return render_template('ConstProsecPrim.html', IType=result[0], StudName=result[2], StudLast=result[3], INumber=input_value, 
                               today=today, CurrentYear=CurrentYear, PastYear=PastYear, Hour=Hour, 
                               gradoAP=grado_actP, gradoNP=grado_newP, literal=grado_lit)
    else:
        return "Student not found"

@app.route('/ConstRetP/')
def ConstRetP():
    input_value = request.args.get('input_value')
    grado_reten = int(request.args.get('gradoRETE'))

    if grado_reten == 1:
        grado_reten = 'PRIMER GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_reten == 2:
        grado_reten = 'SEGUNDO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_reten == 3:
        grado_reten = 'TERCER GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_reten == 4:
        grado_reten = 'CUARTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_reten == 5:
        grado_reten = 'QUINTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif grado_reten == 6:
        grado_reten = 'SEXTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    else:
        return "no valid"
        
    CurrentYear = date.today().year
    PastYear = CurrentYear - 1

    Hour = datetime.datetime.now()
    Hour = Hour.strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE StudCed=?", (input_value,))
    result = cursor.fetchone()

    if result:
        today = date.today()
        return render_template('ConstRetP.html', IType=result[0], StudName=result[2], StudLast=result[3], INumber=input_value, 
                               today=today, CurrentYear=CurrentYear, PastYear=PastYear, Hour=Hour, 
                               gradoRETE=grado_reten)
    else:
        return "Student not found"

@app.route('/ConstCond/')
def ConstCond():
    input_value = request.args.get('input_value')
       
    CurrentYear = date.today().year
    PastYear = CurrentYear - 1

    Hour = datetime.datetime.now()
    Hour = Hour.strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE StudCed=?", (input_value,))
    result = cursor.fetchone()

    if result:
        today = date.today()
        return render_template('ConstCond.html', IType=result[0], StudName=result[2], StudLast=result[3], INumber=input_value, 
                               today=today, CurrentYear=CurrentYear, PastYear=PastYear, Hour=Hour)
    else:
        return "Student not found"

@app.route('/ConstReti/')
def ConstReti():
    input_value = request.args.get('input_value')
    ret_grad = int(request.args.get('grado'))
    ret_raz =int(request.args.get('razon')) 

    if ret_grad == 1:
        ret_grad = 'PRIMER GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif ret_grad == 2:
        ret_grad = 'SEGUNDO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif ret_grad == 3:
        ret_grad = 'TERCER GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif ret_grad == 4:
        ret_grad = 'CUARTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif ret_grad == 5:
        ret_grad = 'QUINTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif ret_grad == 6:
        ret_grad = 'SEXTO GRADO, NIVEL DE EDUCACIÓN PRIMARIA'
    elif ret_grad == 7:
        ret_grad = 'PRIMER AÑO, NIVEL DE EDUCACIÓN MEDIA GENERAL'
    elif ret_grad == 8:
        ret_grad = 'SEGUNDO AÑO, NIVEL DE EDUCACIÓN MEDIA GENERAL'
    elif ret_grad == 9:
        ret_grad = 'TERCER AÑO, NIVEL DE EDUCACIÓN MEDIA GENERAL'
    else:
        return "no valid"

    if ret_raz == 1:
        ret_raz = 'CAMBIO DE RESIDENCIA'
    elif ret_raz == 2:
        ret_raz = 'PROBLEMAS DE SALUD'
    elif ret_raz == 3:
        ret_raz = 'PROBLEMAS FAMILIARES'
    else:
        return "no valid"

    CurrentYear = date.today().year
    PastYear = CurrentYear - 1

    Hour = datetime.datetime.now()
    Hour = Hour.strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE StudCed=?", (input_value,))
    result = cursor.fetchone()

    if result:
        today = date.today()
        return render_template('ConstRet.html', IType=result[0], StudName=result[2], StudLast=result[3], INumber=input_value, 
                               today=today, CurrentYear=CurrentYear, PastYear=PastYear, Hour=Hour,
                               grado=ret_grad, razon=ret_raz)
    else:
        return "Student not found"

@app.route('/StudData/')
def StudData():
    input_value = request.args.get('input_value')

    Hour = datetime.datetime.now()
    Hour = Hour.strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE StudCed=?", (input_value,))
    result = cursor.fetchone()

    if result:
        today = date.today()
        return render_template('StudData.html', IType=result[0], StudName=result[2], StudLast=result[3], INumber=input_value, 
                               StudB=result[4], StudSt=result[5], StudCt=result[6], RepVE=result[7], RepCed=result[8], 
                               RepN=result[9], RepL=result[10], RepTlf=result[11], RepD=result[12],
                               today=today, Hour=Hour)
    else:
        return "Student not found"
    
if __name__ == '__main__':
    app.run(port=8080)