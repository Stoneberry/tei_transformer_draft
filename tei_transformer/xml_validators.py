from abc import ABCMeta, abstractmethod


class Validator(metaclass=ABCMeta):

    @abstractmethod
    def validate(self, data):
        return False


class WellFormValidator(Validator):

    def validate(self, data):
        return False


class SchemaValidator(Validator):

    def load_rng_schema(self):
        pass

    def load_dtd_schema(self):
        pass

    def load_xsd_schema(self):
        pass

    def get_dtd(self):
        pass

    def validate(self, data):
        return False

