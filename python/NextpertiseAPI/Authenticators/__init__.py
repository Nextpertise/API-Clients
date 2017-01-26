#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Authentication.

The methods and means are explained on 
http://api.nextpertise.nl/documentation/authenticate.html.

Copyright: (C) 2017, Nextpertise B.V.
Author:    Leo Noordergraaf
"""

import sys
import base64

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

class Authenticate(object):
    """
    Root of the authentication class.
    
    Stores the username/password combination and
    defines the login() and logout() functions.
    """
    
    isLoggedin = False
    _username = None
    _password = None

    def __init__(self, username, password):
        """
        Constructor.
        
        Keeps a local copy of the provided username and password.
        Currently all authentication methods can be defined as
        relying on a username/password combination for authentication.
        
        Moreover, all authentication methods convert this username/password
        pair in various ways into an HTTP header and value.
        """
        
        self.isLoggedin = False
        self._username = username
        self._password = password

    def login(self):
        """
        The login() function.
        
        Login uses the stored username and password to construct 
        a key/value pair defining an HTTP header and value.
        
        This function must be overridden in descendent classes.
        """
        
        raise NotImplemented()

    def logout(self):
        """
        Logout in its simplest form does nothing.
        """
        
        self.isLoggedin = False

class AuthAPIKEY(Authenticate):
    """
    AuthAPIKEY implements the API KEY authentication.
    
    See http://api.nextpertise.nl/documentation/authenticate.html#using-the-api-key-authentication.
    """
    
    def login(self):
        """
        This version of the login() function returns the username itself as the HTTP
        header and the password as its value.
        """
        
        self.isLoggedin = True
        return {self._username: self._password}

class AuthPLAIN(Authenticate):
    """
    AuthPLAIN implements the HTTP Basic authentication.
    
    See http://api.nextpertise.nl/documentation/authenticate.html#using-the-http-basic-authentication.
    """
    
    def login(self):
        """
        This version of the login() function returns the standard 'Authorization' HTTP key with the
        encoded username/password combination.
        """
        
        return  {
            'Authorization': self._assemble(self._username, self._password)
        }

    def _assemble(self, username, password):
        """
        Create the HTTP basic authentication value from username and password
        according to https://tools.ietf.org/html/rfc1945#section-10.2.
        """
        
        arg = username + ':' + password

        if PY2:
            return 'Basic ' + base64.b64encode(arg)
        else:
            return 'Basic ' + base64.b64encode(arg.encode()).decode()

