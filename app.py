from flask import Flask
from flask_restful import Api
#importa da pasta resources, do arquivo hotel as classes hoteis, hotel
from resources.hotel import Hoteis, Hotel


app = Flask(__name__)

#instanciando a api do restful
api = Api(app)

#adicionanco como recurso da api restful as classes importadas do arquivo hotel
api.add_resource(Hoteis, '/hoteis') 
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

#roda o codigo
if __name__ == '__main__':
    app.run(debug=True)

