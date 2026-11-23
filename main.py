from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        promedio = (nota1 + nota2 + nota3) / 3

        asistencia = int(request.form['asistencia'])

        if asistencia >= 75 and promedio >= 40:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        return render_template(
            'ejercicio1.html',
            nota1=nota1,
            nota2=nota2,
            nota3=nota3,
            asistencia=asistencia,
            promedio=f'El promedio es {promedio}.',
            estado=estado
        )
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        nombres = [nombre1, nombre2, nombre3]

        nombre_mas_grande = nombre1
        for nombre in nombres:
            if len(nombre_mas_grande) < len(nombre):
                nombre_mas_grande = nombre

        mensaje1 = f'El nombre con mayor cantidad de caracteres es "{nombre_mas_grande}".'
        mensaje2 = f'El nombre tiene {len(nombre_mas_grande)} caracteres.'

        return render_template(
            'ejercicio2.html',
            nombre1=nombre1,
            nombre2=nombre2,
            nombre3=nombre3,
            mensaje1=mensaje1,
            mensaje2=mensaje2,
        )
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run()