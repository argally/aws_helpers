#!/usr/bin/env python

import requests
import click

SAMPLE_API_KEY = '0a7887d62cdf29ca7e43944c28934ed4'


def current_weather(location, api_key=SAMPLE_API_KEY):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(url, params=query_params)

    return response.json()['main']['temp']


@click.command()
@click.argument('location')
@click.option(
    '--api-key', '-a',
    help='your API key for the OpenWeatherMap API',
)
def main(location, api_key):
    """
    A little weather tool that shows you the current weather in a LOCATION of
    your choice. Provide the city name and optionally a two-digit country code.
    Here are two examples:

    1. London,UK

    2. Canmore

    You need a valid API key from OpenWeatherMap for the tool to work. You can
    sign up for a free account at https://openweathermap.org/appid.
    """
    weather = current_weather(location, api_key)
    print("The temperature in {} right now: {} C.".format(location, weather))


if __name__ == "__main__":
    main()
