""" Project: Mini Weather API """

from flask import Flask, jsonify, request


app = Flask(__name__)

weather_data = {
    "new_york" : {"temprature": 22, "condition": "Sunny"},
    "london": {"temprature": 15, "condition": "Cloudy"},
    "tokyo": {"temprature": 28, "condition": "Clear"},
    "sydney": {"temprature": 18, "conditon": "Rainy"}
}

# root endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Mini Weather API!"})

# get weather for all cities
@app.route('/weather', methods = ['GET'])
def get_all_weather():
    return jsonify(weather_data)

# get weather for a specific city
@app.route('/weather/<city>', methods = ['GET'])
def get_weather_by_city(city):
    city = city.lower()
    if city in weather_data:
        return jsonify({city: weather_data[city]})
    return jsonify({"error": "City not found"}), 404

# add new weather data
@app.route('/weather', methods = ['POST'])
def add_city_weather():
    data = request.json
    city = data.get('city', '').lower()
    temprature = data.get('temprature')
    condition = data.get('condition')

    if not city or not temprature or not condition:
        return jsonify({'error': 'Missing city, temprature or condition'}), 400
    
    weather_data[city] = {"temprature": temprature, "condition": condition}
    return jsonify({"message": f"weather for {city} added successfully"}), 201

if __name__ == "__main__":
    app.run(debug= True)

