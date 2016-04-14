class TestOop:
    MSG = "ExampleText"

    def test_no_formatter(self, oop_obj):
        assert oop_obj.apply_external_function_with_if(TestOop.MSG) == oop_obj.apply_external_function_no_if(TestOop.MSG)

    def test_with_formatter(self, oop_obj, formatter):
        assert oop_obj.apply_external_function_with_if(TestOop.MSG, formatter) == \
               oop_obj.apply_external_function_no_if(TestOop.MSG, formatter)
