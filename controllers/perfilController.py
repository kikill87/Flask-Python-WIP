from app import app
from flask import session,render_template,redirect,url_for, request

@app.route("/perfil",methods = ['POST', 'GET'])
def perfil():
     return render_template('perfil/perfil.html')
     
@app.route("/editarPerfil",methods = ['POST', 'GET'])
def editarPerfil():
     return render_template('perfil/editarperfil.html')