from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import pandas as pd
import os

app = Flask(__name__)
api = Api(app)

# Kullanıcılar sınıfı
class Users(Resource):
    def __init__(self):
        # 'kullanicilar.csv' dosyası yoksa oluşturulur
        if not os.path.exists('kullanicilar.csv'):
            pd.DataFrame(columns=['name', 'age', 'city']).to_csv('kullanicilar.csv', index=False)
        self.data = pd.read_csv('kullanicilar.csv')

    def get(self):
        # Veriyi dictionary formatında döner
        self.data = self.data.to_dict('records')
        return {'data': self.data}, 200

    def post(self):
        # Gelen verileri doğrulamak için argümanları tanımlarız
        data_arg = reqparse.RequestParser()
        data_arg.add_argument("name", type=str, required=True, help="Name is required.")
        data_arg.add_argument("age", type=int, required=True, help="Age is required.")
        data_arg.add_argument("city", type=str, required=True, help="City is required.")

        args = data_arg.parse_args()

        # Yeni veriyi ekler ve CSV'ye kaydeder
        self.data = pd.concat([self.data, pd.DataFrame([args])], ignore_index=True)
        self.data.to_csv("kullanicilar.csv", index=False)

        return {'message': 'Record successfully added.'}, 200

    def delete(self):
        # Ad ile veriyi siler
        name = request.args.get('name')

        if name in self.data['name'].values:
            self.data = self.data[self.data['name'] != name]
            self.data.to_csv('kullanicilar.csv', index=False)
            return {'message': 'Record successfully deleted.'}, 200
        else:
            return {'message': 'Record not found.'}, 404

# Şehirleri döndüren sınıf
class Cities(Resource):
    def get(self):
        # Sadece şehir kolonunu okur
        data = pd.read_csv('kullanicilar.csv', usecols=['city'])
        data = data.to_dict('records')
        return {'data': data}, 200

# Adı sorgulayan sınıf
class Name(Resource):
    def get(self, name):
        # CSV'den tüm veriyi okur
        data = pd.read_csv('kullanicilar.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['name'] == name:
                return {'data': entry}, 200
        return {'message': 'No entry found with this name!'}, 404

# İki sayıyı toplayan endpoint
class Sum(Resource):
    def get(self):
        a = request.args.get('a', type=int)
        b = request.args.get('b', type=int)
        if a is None or b is None:
            return {'message': 'Both parameters a and b are required.'}, 400
        return {'result': a + b}, 200

# İki sayıyı çarpan endpoint
class Multiply(Resource):
    def post(self):
        # Argümanları alır
        data_arg = reqparse.RequestParser()
        data_arg.add_argument("a", type=int, required=True, help="Parameter a is required.")
        data_arg.add_argument("b", type=int, required=True, help="Parameter b is required.")

        args = data_arg.parse_args()
        return {'result': args['a'] * args['b']}, 200

# Ana route
@app.route("/")
def home():
    return "Welcome to the Homework App!", 200

# Flask uygulamasını başlatma
if __name__ == '__main__':
    app.run(port=5000)
