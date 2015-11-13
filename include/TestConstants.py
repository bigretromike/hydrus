import collections
import HydrusConstants as HC
import HydrusTags
import os
import random
import threading
import weakref
import HydrusData

tinest_gif = '\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\xFF\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00\x3B'

class FakeHTTPConnectionManager():
    
    def __init__( self ):
        
        self._fake_responses = {}
        
    
    def Request( self, method, url, request_headers = None, body = '', return_everything = False, return_cookies = False, report_hooks = None, temp_path = None ):
        
        if request_headers is None: request_headers = {}
        if report_hooks is None: report_hooks = []
        
        ( response, size_of_response, response_headers, cookies ) = self._fake_responses[ ( method, url ) ]
        
        if temp_path is not None:
            
            with open( temp_path, 'wb' ) as f: f.write( response )
            
            response = 'path written to temporary path'
            
        
        if return_everything: return ( response, size_of_response, response_headers, cookies )
        elif return_cookies: return ( response, cookies )
        else: return response
        
    
    def SetResponse( self, method, url, response, size_of_response = 100, response_headers = None, cookies = None ):
        
        if response_headers is None: response_headers = {}
        if cookies is None: cookies = []
        
        self._fake_responses[ ( method, url ) ] = ( response, size_of_response, response_headers, cookies )
        
    
class FakeWebSessionManager():
    
    def GetCookies( self, *args, **kwargs ): return { 'session_cookie' : 'blah' }
    