from . import api
from flask import make_response, request,jsonify
from utils.timezone_converter_utils import convert_timestamp_with_coordinates
from utils.csv_file_parser import retrieve_converted_time_by_id, retrieve_all_converted_time,\
    add_collection_by_id, update_all_column_by_id,delete_collection_by_id

@api.route("/time-converter", methods=["GET"])
def get_converted_time():

    """ Returns a localtime from timeconverter/?lat= &lng= &timestamp """

    lat, lng, timestamp = request.args.get('lat'), request.args.get('lng'),  request.args.get('timestamp')

    if lat and lng and timestamp:
        try:
            time = convert_timestamp_with_coordinates(float(lat), float(lng), int(timestamp))
            res = make_response(jsonify({'local-time': time}), 200)
            return res
        except:
            res = make_response(jsonify({'error': "Not Acceptable"}), 406)
            return res

    res = make_response(jsonify({"error": "Not found"}), 404)
    return res

@api.route("/time-converter/all", methods=["GET"])
def get_all_converted_time():

    """ Returns a collection from stock ?member= """
    ret_list = retrieve_all_converted_time()

    if len(ret_list) >0:

        res = make_response(jsonify(ret_list), 200)
        return res

    res = make_response(jsonify({"error": "Not found"}), 404)
    return res

@api.route("/time-converter/<id>", methods=["GET"])
def get_converted_time_by_id(id):

    """ Returns a collection from stock ?member= """
    if id:
        ret_list = retrieve_converted_time_by_id(id)

        if len(ret_list) >0:
            res = make_response(jsonify({id:ret_list[0]}), 200)
            return res

    res = make_response(jsonify({"error": "Not found"}), 404)
    return res


@api.route("/time-converter/add/", methods=["POST"])
def add_collection():

    """
    Renders a template if request method is GET.
    Creates a collection if request method is POST
    and if collection doesn't exist
    """

    id = request.args.get('id')
    lat, lng, timestamp = request.args.get('lat'), request.args.get('lng'), request.args.get('timestamp')

    if id and lat and lng and timestamp and request.method == "POST":
        try:
            new_row = {'id': [id], 'lat': [float(lat)], 'lng': [float(lng)], 'timestamp_utc': [int(timestamp)]}
        except:
            res = make_response(jsonify({'error': "Not Acceptable"}), 406)
            return res

        ret_list = add_collection_by_id(id, new_row)

        if len(ret_list) > 0:
            res = make_response(jsonify({"status": "successful created"}), 201)
            return res
        else:
            res = make_response(jsonify({"error": "id already exist"}), 404)
            return res

    res = make_response(jsonify({"error": "Not found"}), 404)
    return res


@api.route("/time-converter/<id>/", methods=["PUT"])
def put_collection(id):
    """ Replaces or creates a collection """

    if id and request.method == "PUT":
        lat, lng, timestamp = request.args.get('lat'), request.args.get('lng'), request.args.get('timestamp')

        if lat and lng and timestamp:
            try:
                new_row = {'id': [id], 'lat': [float(lat)], 'lng': [float(lng)], 'timestamp_utc': [int(timestamp)]}
            except:
                res = make_response(jsonify({'error': "Not Acceptable"}), 406)
                return res

            ret_status = update_all_column_by_id(id, new_row)

            if ret_status:
                res = make_response(jsonify({"status": "successful updated all"}), 201)
                return res
            else:
                res = make_response(jsonify({"status": "successful created new"}), 201)
                return res

    res = make_response(jsonify({"error": "Not found"}), 404)
    return res


@api.route("/time-converter/<id>", methods=["DELETE"])
def delete_member(id):

    """ If the collection exists and the member exists, delete it """
    if id and request.method == "DELETE":
       ret_status = delete_collection_by_id(id)

       if ret_status:
           res = make_response(jsonify({"status": "successful delete"}), 202)
           return res


    res = make_response(jsonify({"error": "Not found"}), 404)
    return res