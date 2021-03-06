from bson import ObjectId
from bson.json_util import dumps
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Projeyi sıfırdan açacaksanız ilk olarak stuff_db.py dosyası çalıştırılmalıdır.

# MongoDB bağlantımızı yapıyoruz
# Bağlanabilmemiz için bilgisayarınızda MongoDB'nin yüklü olması gerekir
client = MongoClient('localhost', 27017)
db = client.netflix_genres


@app.route('/')
def hello_world():
    return dumps({'status': True, 'msg': 'Merhaba :)'})


@app.route('/get_genres/', methods=['GET'])
def get_genres():
    """
        Veri tabanındaki tüm kategorileri çekiyoruz
        :return:
    """
    all_genres = db.genres.find()
    if all_genres is not None:
        return dumps({'status': True, 'data': all_genres})
    else:
        return dumps({'status': False, 'err': "Netflix kategorilerini çekemiyorum, üzgünüm :("})


@app.route('/get_genre/<_id>', methods=['GET'])
def get_genre(_id):
    """
        Veri tabanından seçtiğimiz bir adet kategoriyi çekiyoruz
        :param _id:
        :return:
    """
    genre = db.genres.find_one({'_id': ObjectId(_id)})
    if genre is not None:
        return dumps({'status': True, 'data': genre})
    else:
        return dumps({'status': False, 'err': "Netflix kategorisini çekemiyorum, üzgünüm :("})


if __name__ == '__main__':
    app.run(debug=True)
