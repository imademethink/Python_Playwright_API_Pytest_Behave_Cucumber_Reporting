from abc import ABC, abstractmethod

class BaseAPIPrep(ABC):
    @abstractmethod
    def prep_header(self):
        pass

    @abstractmethod
    def prep_body(self):
        pass

    @abstractmethod
    def prep_api_call(self):
        pass

    @abstractmethod
    def prep_response_validate(self):
        pass
