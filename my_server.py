from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Main Page of our Dashboard"""

    return render_template("charts.html")


@app.route('/python-packeges.json')
def melon_types_data():
    """Return data about packages popularity."""

    data_dict = {
                "labels": [
                    "Pandas",
                    "SciPy",
                    "NumPy"
                ],
                "datasets": [
                    {
                        "data": [500, 50, 100],
                        "backgroundColor": [
                            "green",
                            "red",
                            "#FFCE56"
                        ],
                        "hoverBackgroundColor": [
                            "#FF6384",
                            "#36A2EB",
                            "#FFCE56"
                        ]
                    }]
            }
    return jsonify(data_dict)


@app.route('/python-times.json')
def melon_times_data():
    """Return time series data of packages popularity."""

    data_dict = {
        "labels": ["January", "February", "March", "April", "May", "June", "July"],
        "datasets": [
            {
                "label": "Python",
                "fill": True,
                "lineTension": 0.5,
                "backgroundColor": "rgba(220,220,220,0.2)",
                "borderColor": "rgba(220,220,220,1)",
                "borderCapStyle": 'butt',
                "borderDash": [],
                "borderDashOffset": 0.0,
                "borderJoinStyle": 'miter',
                "pointBorderColor": "rgba(220,220,220,1)",
                "pointBackgroundColor": "#fff",
                "pointBorderWidth": 1,
                "pointHoverRadius": 5,
                "pointHoverBackgroundColor": "#fff",
                "pointHoverBorderColor": "rgba(220,220,220,1)",
                "pointHoverBorderWidth": 2,
                "pointRadius": 3,
                "pointHitRadius": 10,
                "data": [65, 59, 80, 81, 56, 55, 40],
                "spanGaps": False},
            {
                "label": "Java Script",
                "fill": True,
                "lineTension": 0.5,
                "backgroundColor": "rgba(151,187,205,0.2)",
                "borderColor": "rgba(151,187,205,1)",
                "borderCapStyle": 'butt',
                "borderDash": [],
                "borderDashOffset": 0.0,
                "borderJoinStyle": 'miter',
                "pointBorderColor": "rgba(151,187,205,1)",
                "pointBackgroundColor": "#fff",
                "pointBorderWidth": 1,
                "pointHoverRadius": 5,
                "pointHoverBackgroundColor": "#fff",
                "pointHoverBorderColor": "rgba(151,187,205,1)",
                "pointHoverBorderWidth": 2,
                "pointHitRadius": 10,
                "data": [28, 48, 40, 19, 86, 27, 90],
                "spanGaps": False}
        ]
    }
    return jsonify(data_dict)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
