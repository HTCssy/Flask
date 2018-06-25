from flask import Blueprint, Flask, request, render_template, jsonify

from apps.ext import images
from apps.utils.image_utils import get_new_image_name

upload_blue = Blueprint('upload', __name__, template_folder='templates', static_folder='static')

def init_upload_img(app:Flask):
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
#单个文件上传
@upload_blue.route('/img/', methods=['GET', 'POST'])
def upload_img():
    if request.method == 'POST':
        img = request.files.get('file_img')
        file_name = images.save(img, name=get_new_image_name(img.filename))
        #  生成可以访问的路径
        # /static/upload/images/xxx.png
        url = images.url(file_name)
        return jsonify({'msg': 'success', 'status': 200, 'url': url})
        #文件上传对象  字典
    elif request.method == 'GET':
        return render_template('upload_img.html')

#多文件
@upload_blue.route('/img/', methods=['GET', 'POST'])
def upload_img():
    if request.method == 'POST':
        files = request.files.getlist('files')
        urls = []
        for image in files:
            file_name = images.save(image, name=get_new_image_name(image.filename))
            url = images.url(file_name)
            urls.append(url)
        # 生成可以访问的路径
        # /static/upload/images/xxx.png
        return jsonify({'msg': 'success', 'status': 200, 'url': urls})
        #文件上传对象  字典
    elif request.method == 'GET':
        return render_template('upload_img.html')