from flask import Flask
from flask_restful import Api
#importa da pasta resources, do arquivo hotel as classes hoteis, hotel
from resources.hotel import Hoteis, Hotel


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#instanciando a api do restful
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

#adicionanco como recurso da api restful as classes importadas do arquivo hotel
api.add_resource(Hoteis, '/hoteis') 
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

#roda o codigo
if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)

