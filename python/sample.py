#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Copyright: (C) 2017, Nextpertise B.V.
Author:    Leo Noordergraaf
"""

import NextpertiseAPI as api

USERNAME = 'your username'
PASSWORD = 'your password'

ZIPCODE = 'your zipcode'
HOUSENR = your house number

class MyZipcode(object):
    ZIPCODE_TRANSLATE = {
        'KPNWBA' : 'KPN (WBA)',
        'KPNWEAS': 'KPN (Weas)',
        'EUROFIBER': 'Eurofiber',
        'TELE2': 'Tele2',
        'ADSL' : 'Zakelijk ADSL',
        'VDSL': 'Zakelijk VDSL',
        'SDSL': 'Zakelijk SDSL',
        'SDSL.bis': 'Zakelijk SDSL.bis',
        'Fiber': 'Zakelijk Glasvezel'
    }

    def __init__(self):
        auth = api.AuthPLAIN(USERNAME, PASSWORD)
        self.client = api.BasicBroadband(auth)

    def zipcode(self, zipcode, housenr, housenrext=None):
        # get zipcode data
        data = self.client.zipcode(zipcode, housenr, housenrext)
        
        if 'available' in data:
            # scan all items
            # replace integer speed in kb/s with string and units.
            for k,v in data['available'].items():
                for kk,vv in v.items():
                    if 'max_download' in vv:
                        vv['max_download'] = self._Kb2Mb(vv['max_download'])
                    if 'max_upload' in vv:
                        vv['max_upload'] = self._Kb2Mb(vv['max_upload'])
            
            # scan all items
            # replace text labels present as key in ZIPCODE_TRANSLATE
            # with their values.
            for k,v in data['available'].items():
                for kk,vv in v.items():
                    tk = self._translate(kk)
                    if kk != tk:
                        v[tk] = v[kk]
                        del v[kk]
                tk = self._translate(k)
                if k != tk:
                    data['available'][tk] = data['available'][k]
                    del data['available'][k]
        return data

    def _translate(self, txt):
        if txt in self.ZIPCODE_TRANSLATE:
            return self.ZIPCODE_TRANSLATE[txt]
        return txt

    def _Kb2Mb(self, val):
        val = int(val)
        if val < 1024:
            return '%d Kb' % val
        return '%d Mb' % round(val / 1024)

if __name__ == '__main__':
    client = MyZipcode()
    print(client.zipcode(ZIPCODE, HOUSENR))
