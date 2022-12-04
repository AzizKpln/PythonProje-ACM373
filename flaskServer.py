from flask import Flask, render_template,request
#importing the modules that's written by us for this project
import reqDataPOST
import SimilarGames
class ACM373_Project(object):
    def __init__(self, app, **configs):
        self.app = app
        self.configs(**configs)
    def configs(self, **configs):
        for config, value in configs:
            self.app.config[config.upper()] = value
    def add_endpointGET(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods, *args, **kwargs)
    def add_endpointPOSTGET(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET','POST'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods, *args, **kwargs)
    def run(self, **kwargs):
        #self.app.config['SERVER_NAME'] = 'umutcapar.ml:80'
        #self.app.run(**kwargs)
        self.app.run("0.0.0.0",80,debug=True)
flask_app = Flask(__name__)
app = ACM373_Project(flask_app)

def index():
    if request.method=="GET":
        return render_template("index.html")
    elif request.method=="POST":
        nameOfGame=request.form["gameName"]
        
        
        similarGameSET=SimilarGames.similarGames(str(reqDataPOST.POSTReq(nameOfGame).returnSimilarGames),False).returnGames
        similarGamePrices=SimilarGames.similarGames(str(reqDataPOST.POSTReq(nameOfGame).returnSimilarGames),False).returnPriceAndGames
        imageLinks=SimilarGames.similarGames(str(reqDataPOST.POSTReq(nameOfGame).returnSimilarGames),True).getImageLinks
        
        
        print(similarGameSET,similarGamePrices,imageLinks)
        return render_template("similarGames.html")
app.add_endpointPOSTGET('/', 'action', index, methods=['GET','POST'])
if __name__ == "__main__":
    app.run(debug=True)