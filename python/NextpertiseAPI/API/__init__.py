#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
The Nextpertise ApiBase

The API covers various services and products that Nextpertise offers.
Per product group or service a dedicated API is made available.
Based on the access rights granted to your account one or more of these
APIs may not be available to you.

Copyright: (C) 2017, Nextpertise B.V.
Author:    Leo Noordergraaf
"""

from tinyrpc import RPCClient
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.http import HttpPostClientTransport

class ApiBase(object):
    """
    Root class for all API clas tree.
    """
    
    PROD_URL = 'https://api.nextpertise.nl'
    TEST_URL = 'https://api.nextpertise.nl/test'

    auth = None
    header = {}

    def __init__(self, auth, url):
        """
        Constructor.
        
        Uses :param:auth to login and obtain an authentication token.
        This token is expected to be a custom HTTP header.
        The token is passed to the http client to authenticate with.
        
        The :param:url defines which API to access. It is based on
        either the PROD_URL or TEST_URL constants defined in this class.
        """
        
        self.auth = auth

        self.header = auth.login()
        self.client = RPCClient(
            JSONRPCProtocol(),
            HttpPostClientTransport(url, headers=self.header)
        )

    def call(self, method, **kwargs):
        """
        Call the server API method.
        
        Calls the API :param:method with the list of key/value
        pairs in :param:kwargs as its parameters.
        Returns whatever the API method returns.
        """
        
        return self.client.call(method, None, kwargs)

from .basicbroadband import BasicBroadband
