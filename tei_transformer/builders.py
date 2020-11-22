from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):

    @abstractmethod
    def check_valid(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def create_template(self):
        pass

    def check_css(self):
        pass


class HTMLBuilder(Builder):

    def check_valid(self):
        pass

    def transform(self):
        pass

    def check_css(self):
        pass

    def create_template(self):
        pass


class PDFBuilder(Builder):

    def check_valid(self):
        pass

    def transform(self):
        pass

    def create_template(self):
        pass


class DOCXBuilder(Builder):

    def check_valid(self):
        pass

    def transform(self):
        pass

    def create_template(self):
        pass


class JSONBuilder(Builder):

    def check_valid(self):
        pass

    def transform(self):
        pass

    def create_template(self):
        pass