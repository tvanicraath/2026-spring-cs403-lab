class LiteralEntry:
    # Structure: { literal_string: {'length': int, 'address': int or None} }
    def __init__(self, literal: str, address: int = None):
        self.length = self.calculate_len(literal)
        self.address = address
    
    @staticmethod
    def calculate_len(literal: str) -> int:
        if literal.startswith("=C'"):
            # Character string: 1 byte per character
            # Example: =C'EOF' -> length 3
            content = literal[3:-1]
            return len(content)
        elif literal.startswith("=X'"):
            # Hex string: 1 byte per 2 hex digits
            # Example: =X'05' -> length 1
            content = literal[3:-1]
            return (len(content) + 1) // 2  # Round up for odd length
        elif literal.startswith("=W'"):
            # Word literal: Standard SIC word is 3 bytes (24 bits)
            return 3
        raise ValueError(f"Invalid literal format: {literal}")
        

class LitTab:
    def __init__(self):
        self.literals = {}
        
    def add_literal(self, literal: str) -> None:
        # Called during Pass 1: Adds a literal (e.g., =C'EOF') without an address.
        pass # Implement this method
        
    def assign_addresses(self, current_locctr: int) -> int:
        # Called when Assembler hits LTORG or END.
        # Logic: Assigns addresses to unassigned literals.
        # Returns: The new value of LOCCTR after allocation.
        
        pass # Implement this method
        
    def get_address(self, literal: str) -> int:
        # Called during Pass 2: Returns the assigned address.
        # Raises KeyError if literal not found.
        # Raises ValueError if address not assigned yet.
        
        pass # Implement this method