from flask import Flask, render_template
app = Flask(__name__)

# display an 8x8 checkerboard
# display an 8x4 checkerboard
# display an x by y checkerboard
# SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>")
@app.route('/')
@app.route('/<int:row>')
@app.route('/<int:row>/<int:column>')
@app.route('/<int:row>/<int:column>/<string:color1>')
@app.route('/<int:row>/<int:column>/<string:color1>/<string:color2>')
def custom_checkerboard(row = 8, column = 8, color1 = 'red', color2 = 'black'):
    return render_template('index.html', row=row, column=column, color1=color1, color2=color2)



if __name__=="__main__":
    app.run(debug=True)