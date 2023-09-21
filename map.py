from ipyleaflet import Map, Marker, Popup
from ipywidgets import HTML
from point import Point


class GCMap(Map):
    karlsruhe = (49.02, 08.41)

    def __init__(self, center=karlsruhe, zoom=14):
        self.map = Map(center=center, zoom=zoom)

    def display_marker(self, point: Point, msg: str = ''):
        message = HTML()
        message.value = f'{Point} \n {msg}'

        marker = Marker(location=(point.latitude, point.longitude), draggable=False)
        self.map.add_layer(marker)
        marker.popup = message

