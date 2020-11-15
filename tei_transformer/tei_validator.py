from xml_validators import WellFormValidator, SchemaValidator


CRV = WellFormValidator()
SMV = SchemaValidator()


class TeiTransformer:

    def __init__(self):
        pass

    @staticmethod
    def check_if_valid(data):
        crv_verdict = CRV.validate(data)
        smv_verdict = SMV.validate(data)
        final_verdict = crv_verdict + smv_verdict
        return final_verdict
