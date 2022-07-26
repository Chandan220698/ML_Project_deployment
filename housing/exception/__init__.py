import os
import sys

class HousingException(Exception):  ## Inheritence of Exception class
    
    def __init__(self, error_message:Exception, error_detail:sys) -> None:
        super().__init__(error_message)   ## error message to __init__ of super class i.e. Exception class 
        self.error_message = HousingException.getDetailedErrorMessage(error_message=error_message,
                                                                      error_detail=error_detail
                                                                     )

    @staticmethod
    def getDetailedErrorMessage(error_message:Exception, error_detail:sys)->str:
        '''
        error_message: Exception object
        error_details: Object of sys module
        '''
        _,_ ,exec_tb = error_detail.exc_info()

        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"Error occured in scrip: [{file_name}] at line no [{line_number}] error message: [{error_message}]"

        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return HousingException.__name__.str()