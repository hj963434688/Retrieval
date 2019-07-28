from flask import Flask, request
from network import NNService
import operate as op
from config import *

nn_service = NNService(k=K)

app = Flask(__name__)


@app.route('/image', methods=['get', 'post'])
def image():
    try:
        url = request.values.get('url')  # 获取参数
        num = request.values.get('num')
        tag = request.values.get('tag')
        res = op.retrieval_ing(url, nn_service, num=int(num), tag=int(tag))
        print(res)
        print('search done')
        pass

    except Exception as identifier:
        print(identifier)
        return b'500'
        pass
    return res


@app.route('/image/add', methods=['get', 'post'])
def add():
    try:
        url = request.values.get('url')
        id_ = request.values.get('id')
        tag = request.values.get('tag')

        msg = op.insert_img(url, nn_service, id_, tag=int(tag))
        print('insert done')
        pass

    except Exception as identifier:
        print(identifier)
        return b'500'
        pass
    return msg


@app.route('/image/delete', methods=['get', 'post'])
def delete():
    try:
        url = request.values.get('url')
        tag = request.values.get('tag')
        msg = op.delete_img(url, nn_service, tag=int(tag))
        print('delete done')
        pass

    except Exception as identifier:
        print(identifier)
        return b'500'
        pass
    return msg


if __name__ == '__main__':
    # app.config['JSON_AS_ASCII'] = False
    app.run(host='', port='9999', debug=True)
    # test = ''
    # s = ret.retrieval_ing(test, nn_service)
    # print(s)
    # print(op.insert_img(test, nn_service, tag=1))
    # print(op.delete_img(test, nn_service, tag=1))
