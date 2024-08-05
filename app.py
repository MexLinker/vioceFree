import os
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')  # 渲染一个 HTML 模板

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        file.save(os.path.join('./data', filename))  # 保存文件到指定路径
        # return 'File successfully uploaded'
        return render_template("afterUpload.html")
    return 'No file'

@app.route('/recon')
def recon():
    return render_template("recon.html")

@app.route('/exec', methods=['POST'])
def execute_script():
    # 这里执行你的Python脚本逻辑
    result = your_script_function()

    # 假设脚本执行结果存储在result中
    # 你可以将结果保存到数据库、文件或直接返回给用户
    # 这里我们直接返回给用户
    return f"脚本执行结果: {result}"

def your_script_function():
    # 这里是你的脚本逻辑
    # 例如，进行一些计算或数据处理

    exit_code = os.system('ls -l')
    
    result = exit_code
    
    #result = "这里是脚本执行的结果"
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
