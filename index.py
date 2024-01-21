from flask import Flask, request, jsonify

#from ipynb.fs.full.TfIdfImplementation import similar_documents

app=Flask(__name__)


@app.route("/")
def home():
    return ("Connected to Backend of RBI Chat Bot")


@app.route("/query",methods=['GET'])
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
    app.run(debug=True)