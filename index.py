from flask import Flask, request, jsonify
import requests
import xmltodict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def convert_xml_to_json():
    # Check if the 'url' query parameter is set
    url = request.args.get('url')
    if url:
        # Get the URL of the XML feed from the 'url' query parameter
        xml_feed_url = url

        # Load the XML feed with the requests library
        response = requests.get(xml_feed_url)

        # Convert the XML feed to a Python dictionary
        data_dict = xmltodict.parse(response.content)

        # Convert the Python dictionary to JSON
        json_data = jsonify(data_dict)

        # Return the JSON
        return json_data
    else:
        # If the 'url' query parameter is not set, return an error message
        return 'Error: No URL specified', 400

if __name__ == '__main__':
    app.run(debug=True)
