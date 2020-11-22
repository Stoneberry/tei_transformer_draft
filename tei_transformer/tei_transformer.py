from main import Director
from lxml import etree


class TEITransformer:

    """
    Интерфейс пакета
    """

    def __init__(self, tei_path, scenario='drama'):
        self.tei = self.__load_tei(tei_path)
        self.scenario = scenario
        self.director = Director()

    def transform(self, output_format='pdf'):
        builder = self.director.assign_builder(output_format)
        method_name = self.director.select_construction_method(output_format)
        getattr(self.director, method_name)(builder, self.tei)

    def transform_custom(self):
        pass

    def __load_tei(self, tei_path):
        tei_doc = etree.parse(tei_path)
        return tei_doc


if __name__ == '__main__':
    transformer = TEITransformer('data/test/afinogenov-mashenka.xml', scenario='drama')
    transformer.transform(output_format='pdf')