from flask import Flask, request, abort

# https://stackoverflow.com/questions/9746303/how-do-i-send-a-post-request-as-a-json/26876308#26876308
import urllib.request
import json 



app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200

        body = {'data': [
                    {
                "first_name": wh_first_name,
                "last_name": wh_last_name,
                "email": wh_email,
                "message": "ideagen3D is trialing a new knowledge base, please join us here for more updated guides, and please leave feedback!"
                "group": wh_groups
                    }
                        ]
                }

        myurl = "http://academy.ideagen.tech/api/user/invite"

        req = urllib.request.Request(myurl)
        req.add_header('API-Key', 'rsFh0DbzscYDVq7KxCaF1X1annGut50bjy3s8uNCAG2/nfiiuH56')

        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
        req.add_header('Content-Length', len(jsondataasbytes))
        response = urllib.request.urlopen(req, jsondataasbytes)



    else:
        abort(400)