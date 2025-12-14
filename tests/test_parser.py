from register_map_codegen import parse_registers


def test_basic_register_parsing():
    sample_text = """
    { "CTRL",   0x00, RW, 1 },
    { "STATUS", 0x01, RO, 1 },
    """

    regs = parse_registers(sample_text)

    assert len(regs) == 2
    assert regs[0]["name"] == "CTRL"
    assert regs[0]["address"] == "0x00"
    assert regs[0]["access"] == "RW"
    assert regs[0]["length"] == 1

    assert regs[1]["name"] == "STATUS"
    assert regs[1]["access"] == "RO"
