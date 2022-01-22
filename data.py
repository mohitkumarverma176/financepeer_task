from flask import Blueprint, request, render_template
import dbops

data_blueprint = Blueprint('__data__', __name__)


@data_blueprint.route('/upload_file', methods=['POST'])
def upload_file():
    return dbops.upload_file(request)


@data_blueprint.route('/upload')
def upload():
    return render_template('upload.html')


