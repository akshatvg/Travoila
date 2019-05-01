from flask import Flask,request
from flask_cors import CORS,cross_origin
app = Flask(__name__)
cors=CORS(app)

queue = []
RFID = []
count = 0

if __name__ == '__main__':
    app.run()

@app.route('/')
@cross_origin()
def hello():
    return "Server Working Fine!!!" 


@app.route('/airportInfo/<string:name>')
@cross_origin()
def airportInfo(name):
    return "Airport Info : You requested for %s" % name 

@app.route('/onlineShopping/<string:item>')
@cross_origin()
def onlineShopping(item):
    return "This page displays items for %s" % item

@app.route('/minors/<int:tag_no>')
@cross_origin()
def minors(tag_no):
    return "Details for minor with %s" % tag_no + " is : "+ "None"

@app.route("/checkQueueStatus", methods=["POST"])
@cross_origin()
def checkQueueStatus():
    global queue
    if len(queue)==0:
        return "Empty"
    else:
        return queue[0][0]

@app.route('/addToQueue',methods=['POST'])
@cross_origin()
def addQueue():
    global queue,count
    if request.method=='POST':
       a=request.form['RFID']
       if a in RFID:
           return "Barcode scanned multiple times!!"
       else:
           RFID.append(a)
           count+=1
           m=[a,count]
           queue.append(m)
           print(queue)
           return "User added successfully to queue! Your token no is %d" % count
    else:
        return "Error"

@app.route('/updateQueue',methods = ['POST'])
@cross_origin()
def updateQueue():
    global queue
    print(queue)
    if len(queue)!=0:
        print(queue.pop(0))
    else:
        return("Queue is empty")
    return "Queue updated successfully!"
