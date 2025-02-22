from flask import Flask, request, jsonify, render_template
import googlemaps

app = Flask(__name__)

# Load the Google Maps API key
with open("Google Maps Platform API key.txt", "r") as API:
    APIKey = API.read().strip()

Maps = googlemaps.Client(key=APIKey)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_distance', methods=['POST'])
def get_distance():
    start_destination = request.form['start']
    end_destination = request.form['end']

    # Calculate distance using API
    try:
        distance_data = Maps.directions(start_destination, end_destination)
        km_distance = distance_data[0]['legs'][0]['distance']['text']
        hrs_mins_duration = distance_data[0]['legs'][0]['duration']['text']
        response = {
            'distance': km_distance,
            'duration': hrs_mins_duration
        }
    except Exception as e:
        response = {
            'error': str(e)
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)