from flask import Flask, jsonify, request, send_file
from flask_restful import Resource, Api, reqparse
import os, io
import json

app = Flask(__name__)
api = Api(app)

# argument parsing
parser = reqparse.RequestParser()
# parser.add_argument('q',help='Pass a sentence to analyse')

@app.route('/event', methods=['GET'])
def get_listings_for_event():
    ticket_id = request.args.get('ticket_id')
    if ticket_id is None:
        ticket_id = "deafult-ticket-id"
    print("ticket_id=" + str(ticket_id))

    f = open('mock_listings_response.json')
    resp = json.load(f)


    f.close()

    return resp


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8501)