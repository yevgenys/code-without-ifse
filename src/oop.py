class Formatters:
    class NoFormatter:
        def format(self, param):
            return param

    class SomeFormatting:
        def format(self, param):
            return "*" + param + "*"


class OopExample:
    def apply_external_function_with_if(self, param1, formatter=None):
        if formatter:
            return formatter.format(param1)
        return param1

    def apply_external_function_no_if(self, param1, formatter=Formatters.NoFormatter()):
        return formatter.format(param1)
