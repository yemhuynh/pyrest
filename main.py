from flask import Flask, jsonify, request, send_file
from flask_restful import Resource, Api, reqparse
import os, io


app = Flask(__name__)
api = Api(app)

# argument parsing
parser = reqparse.RequestParser()
# parser.add_argument('q',help='Pass a sentence to analyse')

@app.route('/event', methods=['GET'])
def get_listings_for_event():
    ticket_id = request.args.get('ticket_id')
    print("ticket_id=" + str(ticket_id))

    return {
        "foo" : "bar"
    }


if __name__ == "__main__":
    app.run(debug=True, port=8501)