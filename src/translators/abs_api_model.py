from abc import ABC, abstractmethod 

"""
This is an abstract class for the model. It is used to define the methods that the model should have.
"""

class AbsApiModel(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def send_request(self, input):
        pass