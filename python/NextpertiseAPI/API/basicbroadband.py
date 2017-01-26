#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Copyright: (C) 2017, Nextpertise B.V.
Author:    Leo Noordergraaf
"""

from NextpertiseAPI.API import ApiBase

class BasicBroadband(ApiBase):
    """
    The basic broadband api.
    
    This API is described at http://api.nextpertise.nl/documentation/broadbandbasic.html.
    It contains stub functions for the API methods of the basic broadband API.
    """
    
    API_URL = '/broadband/basic/v1'

    def __init__(self, auth, test=False):
        """
        Constructor.
        
        Passes the :param:auth authentication object for use as the authentication method.
        
        The :param:test parameter selects between the production and test versions of the API.
        """
        
        url = self.TEST_URL if test else self.PROD_URL
        url += self.API_URL
        super(BasicBroadband, self).__init__(auth, url)

    def zipcode(self, zipcode, housenr, housenrext = None):
        """
        The zipcode() method.
        
        Documented at http://api.nextpertise.nl/documentation/broadband/basic/zipcode.html.
        
        :param:zipcode - Must be a valid Dutch postcode.
        
        :param:housenr - Must be a valid house number within the zipcode area.
        
        :param:housenrext - Optional, needed when :param:zipcode with :param:housenr are not
        sufficient to uniquely identify a location.
        
        Returns the contents of the 'result' key in the json output.
        
        Consult the webpage for the json-schema schemas defining legal input and output format.
        """
        
        return self.call('zipcode', zipcode=zipcode, housenr=housenr, housenrext=housenrext)

