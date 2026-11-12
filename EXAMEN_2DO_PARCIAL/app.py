from flask import Flask, flash, redirect, render_template, request, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'TuNuevaClaveSegura_42!'
app.config['MYSQL_DB'] = 'crud_calificaciones'

app.secret_key = 'mysecretkey'


mysql = MySQL(app)



@app.route('/')
def index():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_calificaciones')
    conCalificaciones = con.fetchall()
    con.close()
    print(conCalificaciones)
    return render_template('index.html', listCalificaciones=conCalificaciones)



@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        alumno = request.form['txtAlumno']
        matricula = request.form['txtMatricula']
        materia = request.form['txtMateria']
        calificacion = request.form['txtCalificacion']
        print(alumno, matricula, materia, calificacion)

        con = mysql.connection.cursor()
        con.execute(
            'INSERT INTO tb_calificaciones(alumno, matricula, materia, calificacion) VALUES(%s,%s,%s,%s)',
            (alumno, matricula, materia, calificacion))
        mysql.connection.commit()
        con.close()

    flash('La calificación fue agregada correctamente!')
    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_calificaciones WHERE id=%s', (id,))
    consultarId = con.fetchone()
    con.close()
    return render_template('editarCalificacion.html', Calif=consultarId)



@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        alumno = request.form['txtAlumno']
        matricula = request.form['txtMatricula']
        materia = request.form['txtMateria']
        calificacion = request.form['txtCalificacion']

        con = mysql.connection.cursor()
        con.execute(
            'UPDATE tb_calificaciones SET alumno=%s, matricula=%s, materia=%s, calificacion=%s WHERE id=%s',
            (alumno, matricula, materia, calificacion, id))
        mysql.connection.commit()
        con.close()

    flash('Se actualizó la calificación de ' + alumno)
    return redirect(url_for('index'))



@app.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar(id):
    con = mysql.connection.cursor()
    if request.method == 'POST':
        alumno = request.form['txtAlumno']
        con.execute('DELETE FROM tb_calificaciones WHERE id=%s', (id,))
        mysql.connection.commit()
        con.close()
        flash('Se eliminó la calificación de ' + alumno)
        return redirect(url_for('index'))

    con.execute('SELECT * FROM tb_calificaciones WHERE id=%s', (id,))
    consultarId = con.fetchone()
    con.close()
    return render_template('eliminarCalificacion.html', Calif=consultarId)



if __name__ == '__main__':
    app.run(debug=True)