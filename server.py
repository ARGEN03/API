from flask import Flask, jsonify, request
from main import *
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/get_books/", methods=['GET'])
@swag_from('swagger/get_all_books.yml')

def get_all_books():
    books = get_books()
    return jsonify({'data': books})

@app.route("/create_book/", methods=['POST'])
@swag_from('swagger/create_one_book.yml')
def create_one_book():
    try:
        data = request.get_json()
        book = ItemPydantic(
            title=data.get('title', 'No Title'),
            author=data.get('author', 'No Author'),
            genre=data.get('genre', 'No Genre'),
            created_at=data.get('created_at')
        )
        create_book(book)
        return jsonify({'message': 'Created successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route("/retrieve_book/<int:book_id>/", methods=['GET'])
def retrieve_one_book(book_id):
    book = retrieve_book(book_id)
    if not book:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify({'data': {'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre, 'created_at': book.created_at}})

@app.route("/update_book/<int:book_id>/", methods=['PUT'])
def update_one_book(book_id):
    try:
        data = request.get_json()
        update_book(book_id, data)
        return jsonify({'message': 'Updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/delete_book/<int:book_id>/', methods=['DELETE'])
def delete_one_book(book_id):
    try:
        delete_book(book_id)
        return jsonify({'message': 'Deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
