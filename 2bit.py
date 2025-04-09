class True2BitProcessor:
    def __init__(self):
        self.acc = 0  # 2-Bit-Akkumulator
        self.pc = 0    # Program Counter (mehrere Bits für Speicheradressierung)
        self.memory = [0b00, 0b01, 0b10, 0b11]  # 2-Bit-Speicher

    def execute(self, instruction):
        opcode = instruction & 0b11  # Nur 2 Bits!
        if opcode == 0b00:   # NOP
            pass
        elif opcode == 0b01: # INC
            self.acc = (self.acc + 1) & 0b11
        elif opcode == 0b10: # DEC
            self.acc = (self.acc - 1) & 0b11
        elif opcode == 0b11: # HALT
            return False
        return True
