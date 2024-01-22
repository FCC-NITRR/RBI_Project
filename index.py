from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

#from ipynb.fs.full.TfIdfImplementation import similar_documents

app=Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/")
def home():
    return ("Connected to Backend of RBI Chat Bot")


@app.route("/query",methods=['GET'])
@cross_origin(supports_credentials=True)
def query():
    tokenId=request.args.get('tokenId')
    query=request.args.get('query')
    noOfResult=request.args.get('limit')
    if request.method=='GET':
     
        if tokenId!="":
    #     #result=similar_documents(query,noOfResult)
    #     #return jsonify(result),201
            
            # Below show return is just for testing pupose
            return (query+" "+ tokenId),201
        else:
            return ("Invalid Token Id, Unauthorized access"),401


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)