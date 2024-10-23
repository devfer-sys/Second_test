from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 
productos = [
    {"id": 1, "descripcion": "Fanta", "cantidad": 200, "precio": 10.0, "categoria": "Bebidas", "fecha_vencimiento": "2023-12-31"},
    {"id": 2, "descripcion": "Sprite", "cantidad": 200, "precio": 10.0, "categoria": "Bebidas", "fecha_vencimiento": "2023-12-31"},
    {"id": 3, "descripcion": "Sprite", "cantidad": 200, "precio": 10.0, "categoria": "Bebidas", "fecha_vencimiento": "2023-12-31"}
]

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        nuevo_id = max(producto['id'] for producto in productos) + 1
        nuevo_producto = {
            "id": nuevo_id,
            "descripcion": request.form['descripcion'],
            "cantidad": int(request.form['cantidad']),
            "precio": float(request.form['precio']),
            "categoria": request.form['categoria'],
            "fecha_vencimiento": request.form['fecha_vencimiento']
        }
        productos.append(nuevo_producto)
        return redirect(url_for('index'))
    return render_template('nuevo.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if producto is None:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        producto['descripcion'] = request.form['descripcion']
        producto['cantidad'] = int(request.form['cantidad'])
        producto['precio'] = float(request.form['precio'])
        producto['categoria'] = request.form['categoria']
        producto['fecha_vencimiento'] = request.form['fecha_vencimiento']
        return redirect(url_for('index'))
    
    return render_template('editar.html', producto=producto)

@app.route('/eliminar/<int:id>')
def eliminar_producto(id):
    global productos
    productos = [p for p in productos if p['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)