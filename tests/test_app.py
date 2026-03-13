import sys
import os
import pytest
from dash.testing.application_runners import import_app

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


def test_header_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header is not None


def test_graph_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    dropdown = dash_duo.find_element("#region-filter")
    assert dropdown is not None