import glob
from gherkin.token_scanner import TokenScanner
from gherkin.parser import Parser

def getAllFeatureFiles(path):
    return glob.glob(path + '/**/*.feature', recursive=True)

def parseFeatureFile(feature_file):
    parser = Parser()
    feature = parser.parse(TokenScanner(feature_file))
    return feature

def getAllFeatureNames(path):
    menu = []
    for feature_file in getAllFeatureFiles(path):
        menu.append(parseFeatureFile(feature_file)['feature']['name'])
    return menu

def parseAllFeatureFiles(path):
    feature_list = []
    for feature_file in getAllFeatureFiles(path):
        feature_list.append(parseFeatureFile(feature_file))
    return feature_list