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
        
        The authenticator is expected to provide an authentication
        token. This token is expected to be a custom HTTP header.
        The token is passed to the HTTP client to authenticate with.
        
        :param Authenticate auth: The authentication object to use.
        :param str url: Defines which API to access.
        :rtype: None
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
        
        Calls the API ``method`` with the list of key/value
        pairs in ``kwargs`` as its parameters.
        Returns whatever the API method returns.
        
        :param str method: Name of the remote function to call.
        :param dict kwargs: Dict with key/value pairs that are the
            named parameters for the method call.
        """
        
        return self.client.call(method, None, kwargs)

from .basicbroadband import BasicBroadband
from .broadband import Broadband
