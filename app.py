from flask import Flask

AI=Flask(__name__)

@AI.route('/first')
def first():
    return '<h1>This is first flask view function</h1>'

@AI.route('/second')
def second():
    return '<h1>This is second flask view function</h1>'



if __name__=='__main__':
    AI.run(debug=True,host='192.168.11.30',port=3000)