from bson.json_util import dumps, loads
from flask import Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def hello_world():
    return dumps({'status': True, 'msg': 'Merhaba :)'})


@app.route('/get_genres/', methods=['GET'])
def get_genres():
    """
       Genres.json dosyasındaki tüm kategorileri çekiyoruz
       :return:
    """
    with open('genres.json', 'r', encoding='utf-8') as file:
        all_genres = loads(file.read())
        for a in all_genres:
            a['name'] = secure_filename(a.get('name'))
    if all_genres is not None:
        return dumps({'status': True, 'data': all_genres})
    else:
        return dumps({'status': False, 'err': "Netflix kategorilerini çekemiyorum, üzgünüm :("})


@app.route('/get_genre/<_id>', methods=['GET'])
def get_genre(_id):
    """
         Genres.json dosyasından seçtiğimiz bir adet kategoriyi çekiyoruz
        :param _id:
        :return:
    """
    name = _id
    print(name)
    with open('genres.json', 'r', encoding='utf-8') as file:
        all_genres = loads(file.read())
        for gn in all_genres:
            gn['name'] = secure_filename(gn.get('name'))
            if str(gn.get('name')) == name:
                genre = gn

    if genre is not None:
        return dumps({'status': True, 'data': genre})
    else:
        return dumps({'status': False, 'err': "Netflix kategorisini çekemiyorum, üzgünüm :("})


if __name__ == '__main__':
    app.run(debug=True)
