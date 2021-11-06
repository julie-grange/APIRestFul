
from flask import Flask, request
from flask_restful import Api, reqparse

import pandas as pd

app = Flask(__name__)
api = Api(app)

# todo: modifier BD pour répondre au cahier des charges


@app.route("/base/", methods=["GET"])
def getBase():
    data = pd.read_csv("base-carbone.csv", sep=";")  # read CSV
    data = data.to_dict()  # convert dataframe to dictionary

    return {"data": data}, 200  # return data and 200 OK code


@app.route("/base/objects/", methods=["GET"])
def getObjects():
    data = pd.read_csv("base-carbone.csv", sep=";")  # read CSV

    obj = data.Name
    obj = obj.to_dict()

    return {"Object": obj}, 200


@app.route("/base/objects/Id", methods=["GET"])
def getId():
    name = request.args.get("Name")
    data = pd.read_csv("base-carbone.csv", sep=";")  # read CSV
    data_mask = data["Name"] == name
    filtered_data = data[data_mask]
    filtered_data = filtered_data.to_dict()

# todo: gérer les 404

    return {'Id': filtered_data}, 200


@app.route("/base/objects/Id", methods=["POST"])
def postId():
    parser = reqparse.RequestParser()
    parser.add_argument('Name', required=True)  # add args
    parser.add_argument('CO2b', required=True)  # add args
    args = parser.parse_args()  # parse arguments to dictionary

    # create new dataframe containing new values
    new_data = pd.DataFrame({
        "Name": args["Name"],
        "CO2b": args["CO2b"],
    }, index=[0])

    data = pd.read_csv("base-carbone.csv", sep=";")  # read CSV
    data = data.append(new_data, ignore_index=True)  # add the newly provided values
    data.to_csv("base-carbone.csv", index=False)  # save back to CSV
    data = data.to_dict()

    return {"Base mise à jour": data}, 200


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
