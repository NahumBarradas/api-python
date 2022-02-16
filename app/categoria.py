from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://nahum_dbserver:nahum@192.168.10.3:3306/bdpythonapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# USAR NOMBRES CONCRETOS
marshmallow = Marshmallow(app)

#Creación de tabla
class Categoria(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))
    
    def __init__(self, cat_nom, cat_desp):
        self.cat_nom = cat_nom
        self.cat_desp = cat_desp

db.create_all()

#Esquema categoría
class CategoriaSchema(marshmallow.Schema):
    class Meta:
        fields = ('cat_id', 'cat_nom', 'cat_desp')

#Una sola respuesta
categoria_schema = CategoriaSchema()

#Muchas respuestas
categorias_schema = CategoriaSchema(many=True)

#GET
@app.route('/categoria', methods=['GET'])
def get_categorias():
    all_categorias = Categoria.query.all()
    result = categorias_schema.dump(all_categorias)
    return jsonify(result)

#GET por id
@app.route('/categoria/<id>', methods=['GET'])
def get_categorias_x_id(id):
    una_categoria = Categoria.query.get(id)
    return categoria_schema.jsonify(una_categoria)

#POST
@app.route('/categoria', methods=['POST'])
def insert_categoria():
    cat_nom = request.json['cat_nom']
    cat_desp = request.json['cat_desp']
    nuevo_registro = Categoria(cat_nom, cat_desp)
    db.session.add(nuevo_registro)
    db.session.commit()
    return categoria_schema.jsonify(nuevo_registro)

#PUT
@app.route('/categoria/<id>', methods=['PUT'])
def update_categoria(id):
    actualizarcategoria = Categoria.query.get(id)
    cat_nom = request.json['cat_nom']
    cat_desp = request.json['cat_desp']
    actualizarcategoria.cat_nom = cat_nom
    actualizarcategoria.cat_desp = cat_desp
    db.session.commit()
    return categoria_schema.jsonify(actualizarcategoria)

#DELETE
@app.route('/categoria/<id>', methods=['DELETE'])
def delete_categoria(id):
    eliminarcategoria = Categoria.query.get(id)
    db.session.delete(eliminarcategoria)
    db.session.commit()
    return categoria_schema.jsonify(eliminarcategoria)

#Mensaje de bienvenida
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message':'Bienvenido a mi servidor'})

if __name__ == '__main__':
    app.run(debug=True)