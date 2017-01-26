#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Nextpertise API Client

The Nextpertise API Client is a sample client for the Nextpertise API.
The API documentation can be found at http://api.nextpertise.nl/documentaion.

This client is provided to give resellers an example how a client library could
be programmed and how the API should be used.

The client consists of two sections: authentication and the actual API.

This client functions with both Python 2 and Python 3.
This client depends on a customized version of the TinyRPC library.
The customized version of TinyRPC is available on the Nextpertise GitHub account.

Copyright: (C) 2017, Nextpertise B.V.
Author:    Leo Noordergraaf
"""

from .Authenticators import *
from .API import *
