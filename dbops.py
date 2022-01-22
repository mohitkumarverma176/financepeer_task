from database import mongo
import os
import json
from flask import jsonify
import config


def upload_file(req_data):
    print("coming to upload")
    print(req_data)
    files = req_data.files['file']
    cwd_path = os.getcwd()
    cur_path = os.path.join(cwd_path, 'json_file')
    files.save(cur_path)
    with open('json_file') as f:
        data = json.load(f)
    for record in data:
        mongo.db['customer_details'].insert(record)
    return jsonify({'status': 'success', 'message': 'file received'})


def get_data():
    cursor = list(mongo.db[config.COLLECTION_NAME].find({}, {'_id':0}))
    return cursor

