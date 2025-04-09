import sys

class True2BitProcessor:
    def __init__(self):
        self.registers = [0, 0]  # Two 2-bit registers (0b00 to 0b11)
        self.memory = [0b00, 0b01, 0b10, 0b11]  # 2-bit memory
        self.running = True

    def execute(self, instruction):
        instruction = instruction & 0b11  # Only 2 bits!
        if instruction == 0b00:   # NOP (No Operation)
            pass
        elif instruction == 0b01: # INC (Increment R0)
            self.registers[0] = (self.registers[0] + 1) & 0b11
        elif instruction == 0b10: # DEC (Decrement R0)
            self.registers[0] = (self.registers[0] - 1) & 0b11
        elif instruction == 0b11: # SWAP (Swap R0 and R1)
            self.registers[0], self.registers[1] = self.registers[1], self.registers[0]
        print(f"R0={self.registers[0]}, R1={self.registers[1]}")

    def show_help(self):
        print("\n=== 2-Bit Processor (True 2-Bit!) ===")
        print("Commands (2-bit binary):")
        print("  00: NOP (No Operation)")
        print("  01: INC (R0 += 1)")
        print("  10: DEC (R0 -= 1)")
        print("  11: SWAP (R0 ↔ R1)")
        print("\nShell Commands:")
        print("  echo: Show registers")
        print("  help: Show help")
        print("  exit: Exit\n")

    def run_interactive(self):
        print("True 2-Bit Processor! Enter 2-bit commands (00, 01, 10, 11).")
        print("Tip: 'help' shows options, 'echo' shows registers.\n")
        
        while self.running:
            cmd = input(">> ").strip().lower()
            
            if cmd == "exit":
                print("Program terminated.")
                break
            elif cmd == "echo":
                print(f"R0={self.registers[0]}, R1={self.registers[1]}")
            elif cmd == "help":
                self.show_help()
            else:
                try:
                    instruction = int(cmd, 2)
                    if instruction > 0b11:
                        print("Error: Only 2-bit commands (00, 01, 10, 11) are allowed!")
                    else:
                        self.execute(instruction)
                except ValueError:
                    print("Invalid! Allowed: 2-bit binary or 'echo/help/exit'.")

# Main program
if __name__ == "__main__":
    cpu = True2BitProcessor()
    cpu.run_interactive()
