from flask import Blueprint, render_template, request, redirect, url_for, flash
from data import fetch_data, parser
from operation import operation

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def results_view():
    url = fetch_data.UrlBuilderHouse().build_url(
        limit="40",
        area_min="25",
        price_min="600",
    )
    x = parser.Parser(fetch_data.FetchData(url).fetch_data())
    d = x.data_parser()

    # for data in operation.return_newest_offers(d):
    #     print(data)
    # print(operation.return_newest_offers(d))
    # print(url)
    # print(operation.return_cheapest_offer(d))
    return render_template('results.html', data_list=d)
