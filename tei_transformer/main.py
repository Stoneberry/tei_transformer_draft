from builders import *


class Director:

    @staticmethod
    def transform_html(builder, data):
        print('Transformation started')

    @staticmethod
    def transform_docs(builder, data):
        print('Transformation started')

    @staticmethod
    def transform_json(builder, data):
        print('Transformation started')

    @staticmethod
    def transform_pdf(builder, data):
        # builder.check_well_formed()
        # builder.check_valid()
        # builder.check_css()
        # builder.create_template()
        # builder.transform()
        print('Transformation started')

    @staticmethod
    def assign_builder(output_format):
        if output_format == "pdf":
            builder = PDFBuilder()
        elif output_format == "docs":
            builder = DOCXBuilder()
        elif output_format == "html":
            builder = HTMLBuilder()
        elif output_format == "json":
            builder = JSONBuilder()
        else:
            raise ValueError('There are only 4 possible formats: pdf, docs, html, json')
        print("Selected builder: {}".format(builder.__class__))
        return builder

    @staticmethod
    def select_construction_method(output_format):
        method_name = "transform_{}".format(output_format)
        print("Selected method: {}".format(method_name))
        return method_name


class Product:

    """
    должны быть атрибуты:
    - schema
    - style
    - template
    """

    def __init__(self, scenario):
        self.set_default_schema(scenario)
        self.set_default_css(scenario)

    @staticmethod
    def load_rng_schema(schema_path):
        schema_doc = etree.parse(schema_path)
        schema = etree.RelaxNG(schema_doc)
        return schema

    @staticmethod
    def load_dtd_schema(schema_string):
        pass

    @staticmethod
    def load_xsd_schema(schema_path):
        """
        ПЕРЕПРОВЕРИТЬ
        :param schema_path:
        :return:
        """
        schema_doc = etree.parse(schema_path)
        schema = etree.XMLSchema(schema_doc)
        return schema

    def set_default_schema(self, scenario):
        schema_path_template = '/data/schema/dtd/{}/{}.dtd'
        schema_path = schema_path_template.format(scenario, scenario)
        self.schema = self.load_dtd_schema(schema_path)

    def set_default_css(self, scenario):
        pass

    def set_schema(self, schema_path):
        pass

    def set_css(self, css):
        pass


if __name__ == '__main__':
    from lxml import etree
    from builders import *

    a = Director()
    method_name = "transform_{}".format('pdf')
    print(dir(a))
    print(a.__class__)
    # print(method_name)
    # a.__getattribute__(method_name)()
    # print(getattr(a, method_name)())
