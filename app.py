import pyodbc
from flask import Flask, render_template

app = Flask(__name__)

# Configura la conexión a la base de datos Access
conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\LUIS\Documents\VS CODE\Parcial\Parcial.accdb')


@app.route('/')
def index():
    # Consulta SQL para seleccionar los datos de la primera tabla
    cursor1 = conn.cursor()
    cursor1.execute('SELECT * FROM Cursos')
    data1 = cursor1.fetchall()

    # Consulta SQL para seleccionar los datos de la segunda tabla
    cursor2 = conn.cursor()
    cursor2.execute('SELECT * FROM Estudiantes')
    data2 = cursor2.fetchall()

    # Cierra las conexiones
    cursor1.close()
    cursor2.close()
    conn.close()

    # Renderiza un template HTML con los datos de ambas tablas
    return render_template('reporte.html', data1=data1, data2=data2)


if __name__ == '__main__':
    app.run(debug=True)
