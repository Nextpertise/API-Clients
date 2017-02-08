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
        
        :param Authenticate auth: The authentication object to use.
        :param bool test: Select between production and test versions of the API.
        """
        
        url = self.TEST_URL if test else self.PROD_URL
        url += self.API_URL
        super(BasicBroadband, self).__init__(auth, url)

    def zipcode(self, zipcode, housenr, housenrext = None):
        """
        The zipcode() method.
        
        Documented at http://api.nextpertise.nl/documentation/broadband/basic/zipcode.html.

        :param str zipcode: Valid Dutch postcode.
        :param int housenr: Must be a valid house number within the zipcode area.
        :param str housenrext: Optional, needed when ``zipcode`` with ``housenr`` are not
            sufficient to uniquely identify a location.
        
        Consult the webpage for the json-schema schemas defining legal input and output format.
        """
        
        return self.call('zipcode', zipcode=zipcode, housenr=housenr, housenrext=housenrext)

