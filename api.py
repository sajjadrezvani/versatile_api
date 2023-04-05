from flask import Flask, send_file, render_template , request, session 
from werkzeug.utils import secure_filename
from collector import collector
import os
import webbrowser
from threading import Timer

PEOPLE_FOLDER = os.path.join('static', 'logo')
app = Flask(__name__, static_url_path='/assets')


# app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
# full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'TNM.jpg')

app.secret_key = os.urandom(20)

@app.route('/') 
def upload_file():
   return render_template('login.html'  ,percent = 0 ) #,  user_image = full_filename)

@app.route('/run', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      file = request.files['file']                       # file name
      file.save(secure_filename(file.filename))
      firstBox = request.form['firstCode']              # form first code 
      secBox = request.form['secondCode']
      checkbox='off'
      if request.form.get('check'):                      
         checkbox = request.form['check']                # form check
      final_file = collector(file.filename,checkbox, firstBox,secBox)
      print(final_file,'>>>>>>',checkbox, '>>>>',firstBox,secBox)
      session['out_name'] = final_file
      return render_template('login.html' ,percent = 100 ) #,  user_image = full_filename)

@app.route('/download')
def download_file():
   path = session['out_name']
   full_path = os.path.join(os.getcwd(),path)
   print(full_path)

   return send_file(full_path, as_attachment=True)

def open_browser():
   webbrowser.open_new('http://127.0.0.1:5000/')


if __name__ == "__main__":
   Timer(1, open_browser).start()
   app.run(debug=True,port=5000, use_reloader=False)

