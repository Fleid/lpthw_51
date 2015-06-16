# -*- coding: utf-8 -*-

from nose.tools import *
from bin.app import app
from tests.tools import assert_response


def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status = "404")
    
    # test our first GET request to /hello
    # On check qu'on reçoit bien un 200 quand on tape sur une URL correcte
    resp = app.request("/hello")
    assert_response(resp)
    
    # make sure default values work for the form
    # On test qu'on reçoit bien la valeur par défaut quand on POST en vide
    resp = app.request("/hello", method ="POST")
    assert_response(resp,contains="Nobody")
    
    # test that we get expected values
    payload = {'name' : 'Zed', 'greet':'Hola'}
    resp = app.request("/hello", method="POST", data=payload)
    assert_response(resp, contains="Zed")
    