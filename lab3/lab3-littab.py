from littab import LitTab

def main():
    print("--- LAB 3: TESTING LITTAB ---")

    lt = LitTab()
    print("Adding literals...")
    lt.add_literal("=C'EOF'")  # Length 3
    lt.add_literal("=X'05'")   # Length 1
    lt.add_literal("=C'EOF'")  # Should be ignored (duplicate)
    lt.add_literal("=W'420'") # Length 3
    lt.add_literal("=X'CAFEBABE'") # Length 4

    # Check addresses before assignment
    try:
        addr_eof = lt.get_address("=C'EOF'")
        raise AssertionError("Address should not be assigned yet")
    except ValueError:
        pass
    
    # Simulate LTORG or END
    current_locctr = 0x3000
    print(f"Simulating LTORG at address {current_locctr:X}...")

    new_locctr = lt.assign_addresses(current_locctr)
    print(f"New LOCCTR: {new_locctr:X}")
    assert new_locctr == 0x3000 + 3 + 1 + 3 + 4, "LOCCTR calculation error"

    addr_eof = lt.get_address("=C'EOF'")
    assert addr_eof == 0x3000, "Address of =C'EOF' incorrect"
    addr_w420 = lt.get_address("=W'420'")
    assert addr_w420 == 0x3004, "Address of =W'420' incorrect"

    # Check address of non-existent literal
    try:
        lt.get_address("=C'NOTEXIST'")
        raise AssertionError("Expected ValueError for non-existent literal")
    except KeyError:
        pass


if __name__ == "__main__":
    main()