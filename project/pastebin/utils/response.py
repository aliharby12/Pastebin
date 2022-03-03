from rest_framework.response import Response
from rest_framework import status
from collections import OrderedDict        
from typing import Union,Optional
        

class SuccessResponse : 
    """
    handle the success response
    """
    @staticmethod
    def _render(data:list=[],message:Optional[str]=None,status_code:Optional[int]=None) -> Response:    
        if not message : 
            message = 'Success'
        if not status_code :
            status_code = status.HTTP_200_OK
        return Response(OrderedDict([
            ('message', message),
            ('data', data),
            ('error' , False )
    ]),status=status_code)



class ErrorResponse : 
    """
    handle the error response
    """
    @staticmethod
    def _render(data:list=[],message:Optional[str]=None,status_code:Optional[int]=None) -> Response :
        if not message : 
            message = 'Bad request'
        if not status_code :
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(OrderedDict([
            ('message', message),
            ('data', data),
            ('error' , True )
    ]),status=status_code)
        
        