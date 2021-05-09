from flask import Flask,render_template, jsonify, request,redirect, url_for
from flask_cors import CORS
import platform
import socket 
import os
import sys
import re
from requests import get

app = Flask(__name__)
CORS(app)

def my_ip_location(my_ip):
    reader = geolite2.reader()
    location = reader.get(my_ip)

    #geolite database dict values and fine tunning
    a=(location['city']['names']['en'])
    b=(location['continent']['names']['en'])
    c=(location['country']['names']['en'])
    d=(location['location'])
    e=(location['postal'])
    f=(location['registered_country']['names']['en'])
    g=(location['subdivisions'][0]['names']['en'])

    print('''city: %s\ncontinent: %s\ncountry: %s\nlocation: %s\npostal: %s\nregistered_country: %s\nsubdivisions: %s\n'''
     % (a,b,c,d,e,f,g))

@app.route("/")
def get_bot_response():
    system_data = platform.uname()
    os_name = str(system_data.system)
    if os_name.lower()=="windows" :
        hostname = socket.gethostname() # returns hostname
        ip_address = socket.gethostbyname(hostname)  # returns IPv4 address with respect to hostname
        fqdn = socket.getfqdn('www.google.com') # returns fully qualified domain name for name
        ip = get('https://api.ipify.org').text
        
        machine = str(system_data.machine)
        processor = str(system_data.processor)
        release = str(system_data.release)
        version = str(system_data.version)
        hostname = str(hostname)
        pvt_ip = str(socket.gethostbyname_ex(hostname)[-1][-1])
        public_ip = str(ip)

    data ={
        'fqdn' : fqdn,
        'machine': machine,
        'processor' :processor,
        'release' : release,
        'version' : version,
        'hostname' : hostname,
        'pvt_ip' :pvt_ip,
        'public_ip' : public_ip,
        'os_name': os_name,
    }
    return render_template('index.html',data=data)
    



if __name__ == '__main__':
    app.run()
    