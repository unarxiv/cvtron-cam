import os
from flask import Flask
from flask import Response

from vendor.raspberry import Camera

app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/cam')
def cam_feed():
    return Response(gen(Camera()),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ '__main__':
    app.run(host='0.0.0.0', threaded=True, port=12399)