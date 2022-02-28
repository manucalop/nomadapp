from abc import ABC, abstractmethod
import pandas as pd


class Filters(ABC):

    def __init__(self, location, radius, gmaps):
        self.location = location
        self.radius = radius
        self.gmaps = gmaps

    @abstractmethod
    def api_request(self):
        pass

    @staticmethod
    def json_to_table(query_json):
        query_df = pd.DataFrame()
        query_df['Name'] = list(map(lambda name: name['name'], query_json['results']))
        query_df['latitude'] = list(map(lambda lat: lat['geometry'].get('location').get('lat'), query_json['results']))
        query_df['longitude'] = list(map(lambda long: long['geometry'].get('location').get('lng'), query_json['results']))
        # query_df['status'] = list(map(lambda status: status['business_status'], query_json['results']))
        # query_df['rating'] = list(map(lambda status: status['rating'], query_json['results']))
        return query_df


class Coworking(Filters):
    def api_request(self):
        query_json = self.gmaps.places('coworking', location=self.location, radius=self.radius)
        return query_json


class Education(Filters):
    '''primary_school, secondary_school, university, school'''
    def api_request(self):
        query_json = self.gmaps.places(location=self.location, type='secondary_school', radius=self.radius)
        return query_json

class Food_and_Drinks(Filters):
    '''bar, restaurant, night club, cafe'''
    def api_request(self):
        restaurants_request = self.gmaps.places(location=self.location, type='restaurante', radius=self.radius)
        return restaurants_request

class Leisure(Filters):
    '''zoo, gym, casino, art_gallery, amusement_park, movie_theater, museum'''
    def api_request(self):
        restaurants_request = self.gmaps.places(location=self.location, type='restaurante', radius=self.radius)
        return restaurants_request


