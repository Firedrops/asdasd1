from flask import Flask, request, abort

# https://stackoverflow.com/questions/9746303/how-do-i-send-a-post-request-as-a-json/26876308#26876308
import urllib.request
import json 



app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        wh_payload = request.json
        print(wh_payload)
        return 'success', 200

        wh_first_name = wh_payload["customer"][0]["first_name"]
        wh_first_name = wh_payload["customer"][0]["last_name"]
        wh_first_name = wh_payload["customer"][0]["email"]


        # Initialize lists
        wh_items = []
        wh_groups = []


        # Grab items purchased, iteratively
        # https://stackoverflow.com/questions/34818782/iterate-through-nested-json-object-and-get-values-with-python
        for item in wh_payload["line_items"]:
            wh_items.append(item.get("name"))

        # Add to wh_item_groups if wh_items match certain keywords

        for item in wh_items:
            if "ender" in wh_items:
                wh_groups.append("Ender3V2")

            if "Sapphire" in wh_items:
                wh_groups.append("Sapphire Plus")
                
            if "Octoprint" in wh_items:
                wh_groups.append("Octoprint")

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