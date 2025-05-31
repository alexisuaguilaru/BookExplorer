"""
RecommenderSystem
=================

Module for response requests GET of books 
recommendations and information about of books 
using an app in Flask
"""

from .InformationBooks import GetInformationBook
from .Recommender import GetRecommendations
from .Production import Run_gunicorn