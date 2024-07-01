import flask
import data

app = flask.Flask(__name__)


@app.route("/")
def main_page():
    tours = [(i, data.tours[i]) for i in range(1, 4)]
    return flask.render_template("index.html", 
                                title="Путешествия", 
                                tours=tours,
                                menu=data.departures)


@app.route("/<city>")
def tour_view(city: str) -> None:
    citys = [(key, value) for key, value in data.tours.items() if value.get('departure') == city]
    filter_city = [value for value in data.tours.values() if value.get('departure') == city]
    return flask.render_template("tours.html",
                                title=data.departures.get(city),
                                citys=citys,
                                menu=data.departures,
                                city_tour=data.departures.get(city),
                                filter_city=filter_city)
                                

@app.route("/<city>/<int:id>")
def detail_view(city: str, id: int) -> None:
    return flask.render_template('tour.html', 
                                title=data.departures.get(city),
                                menu=data.departures,
                                city=data.tours.get(id))

if __name__ == "__main__":
    app.run(debug=True)
