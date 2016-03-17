from .context import unique


def test_feature_table_input_short():
    assert unique.get_unique_feature(r"data\sample.gdb\test_table",
                                     "FIELD_SHORT") == {27299: 12, 72: 10,
                                                        -25652: 16, -15411: 7,
                                                        3214: 9, 9263: 13,
                                                        1142: 5, 15032: 11,
                                                        -1989: 10, -13861: 7}
