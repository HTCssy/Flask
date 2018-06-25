from flask import Blueprint, Flask, request, render_template

from apps.ext import images

upload_blue = Blueprint('upload', __name__, template_folder='templates', static_folder='static')

def init_upload(app:Flask):
    app.register_blueprint(upload_blue, url_prefix='/1')
'''
必须是post或者put请求 form-data格式
'''
'''
UploadSet
    save
    参数说明 
        
    url
'''

@upload_blue.route('/img/', methods=['GET', 'POST'])
def upload_img():
    if request.method == 'POST':
        images.save(request.files['img'])
        return '0  . 0'
        #文件上传对象  字典
    elif request.method == 'GET':
        return render_template('upload_img.html')