# Importamos las herramientas necesarias de Flask
from flask import Flask, render_template, redirect

# Creamos la instancia de la aplicación
app = Flask(__name__)

# Permitimos recargar las plantillas HTML al modificarlas
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def home():
    return "¡Hola, Jesus Lopez Cruz!"

@app.route("/guardar")
def guardar():
    print("EJECUTANDO LA RUTA GUARDAR CORRECTA")
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return redirect("/login")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
