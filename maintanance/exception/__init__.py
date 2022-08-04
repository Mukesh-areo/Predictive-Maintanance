import os 
import sys

class maintananceException(Exception):

    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message=maintananceException.get_detailed_error_message(error_message=error_message,
                                                error_detail=error_detail) # initializing error message & error details
                                                       
    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        """
        error_message:Exception object
        error_detail:object of sys module
        """
        _,_ , exec_tb=error_detail.exc_info()
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno # to identify the error line
        file_name=exec_tb.tb_frame.f_code.co_filename #to identify the path of the errord file name

        error_message = f"""
        Error occured in script: 
        [ {file_name} ] at 
        try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] 
        error message: [{error_message}]
        """
        
    def __str__(self):
        return self.error_message  # to execute the error message

    def __repr__(self)-> str:
        return maintananceException.__name__.str()
