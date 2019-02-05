import optparse
import sys
import helpers
from flask import Flask, render_template
app = Flask(__name__)

directory = sys.argv[1]

@app.route('/')
@app.route('/index')
def index():
    features = helpers.parseAllFeatureFiles(directory)[0]
    menu = helpers.getAllFeatureNames(directory)
    return render_template('index.html', features=features, menu=menu)


@app.route('/<feature_name>')
def open_feature(feature_name): 
    menu = helpers.getAllFeatureNames(directory)
    feature_list = helpers.parseAllFeatureFiles(directory)
    for feature in feature_list:
        if feature['feature']['name'] == feature_name:
             return render_template('index.html', features=feature, menu=menu)
    
    return render_template('index.html', features=feature_list[0], menu=menu)

if __name__ == '__main__':
    app.run()