'''
"""This module contains tests for retrieving movie ratings."""

import pytest
from movie_rating.film_rank import FilmRank
from movie_rating.film_rank import RatingReference

@pytest.fixture
def rater():
    """A fixture to provide IMDB rater object"""
    return FilmRank(RatingReference.IMDB)


def test_1(rater):
    """ Tests the rating of the movie called 'A Separation' """
    assert rater.get_rating("separation") == '8.4/10'


def test_2(rater):
    """ Tests the rating of the movie called 'Shawshank Redemption' """
    assert rater.get_rating("shawshank redemption") == '9.3/10'


def test_3(rater):
    """ Tests the rating of the movie called 'Sixth Sense' """
    assert rater.get_rating("sixth sense") == '8.1/10'

'''

import pytest
from gaf import gaf

def test_1():
    test_gaf = gaf()
    test_gaf.read_gaf("tests/test.gaf")
    len(test_gaf.annotations) > 0
