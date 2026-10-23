from dash import Dash, html, request 

app = Dash(__name__)

def get_current_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m",
        "timezone": "Australia/Sydney"
    }

    response = requests.get(url, params=parameters, timeout=10)
    response.raise_for_status()

    weather_data = response.json()
    current_weather = weather_data["current"]

    return {
        "temperature": current_weather["temperature_2m"],
        "humidity": current_weather["relative_humidity_2m"],
        "time": current_weather["time"]
    }

app.layout = html.Div(
    [
        html.H1(
            "Dog Walking Dashboard",
            style={"color": "#2A9D8F"}
        ),
        html.P(
            "The dashboard is running successfully."
        )
    ],
    style={
        "textAlign": "center",
        "fontFamily": "Arial",
        "padding": "50px"
    }
)

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8050
    )
