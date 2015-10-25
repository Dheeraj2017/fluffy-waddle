from flask import Flask,render_template,request;
#Import variables stored in app.py
from app import app;

@app.route('/')
def index():
        import subprocess
        cmd = subprocess.Popen(['ps'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout,error = cmd.communicate()
        process = stdout.splitlines()

        cmd1 = subprocess.Popen(['uptime'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout1,error1 = cmd1.communicate()
        uptime = stdout1.splitlines()

        cmd2 = subprocess.Popen(['cal'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout2,error2 = cmd2.communicate()
        cal = stdout2.splitlines()

        cmd3 = subprocess.Popen(['date'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout3,error3 = cmd3.communicate()
        date = stdout3.splitlines()

        return render_template('view.html', process=process, uptime=uptime,cal=cal,date=date)
~                                                                                                 
