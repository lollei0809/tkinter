from temp_convert_func import temperature_converter


def test_temperature_converter():
    class PtempDataType():
        assert temperature_converter("n", "R", "K") == "ERROR: temp must be a number"
        assert temperature_converter(180, "C", "F") == 356.00  # allows ints
        assert temperature_converter(180.00, "C", "F") == 356.00  # allows floats

    class AbsoluteZero():
        assert temperature_converter(-1, "K", "F") == "ERROR: temp can't be less than 0K (Absolute zero)"
        assert temperature_converter(-500, "F", "C") == "ERROR: temp can't be less than −459.67°F (Absolute zero)"
        assert temperature_converter(-300, "C", "R") == "ERROR: temp can't be less than -273.15°C (Absolute zero)"
        assert temperature_converter(-1, "R", "K") == "ERROR: temp can't be less than 0°R (Absolute zero)"
    class negatives():
        assert temperature_converter(-450, "F", "C") == -267.78
        assert temperature_converter(-250, "C", "R") == 41.67

