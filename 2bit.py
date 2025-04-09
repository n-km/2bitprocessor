import sys

class True2BitProcessor:
    def __init__(self):
        self.registers = [0, 0]  # Zwei 2-Bit-Register (0b00 bis 0b11)
        self.memory = [0b00, 0b01, 0b10, 0b11]  # 2-Bit-Speicher
        self.running = True

    def execute(self, instruction):
        instruction = instruction & 0b11  # Nur 2 Bits!
        if instruction == 0b00:   # NOP (No Operation)
            pass
        elif instruction == 0b01: # INC (Inkrementiere R0)
            self.registers[0] = (self.registers[0] + 1) & 0b11
        elif instruction == 0b10: # DEC (Dekrementiere R0)
            self.registers[0] = (self.registers[0] - 1) & 0b11
        elif instruction == 0b11: # SWAP (Tausche R0 und R1)
            self.registers[0], self.registers[1] = self.registers[1], self.registers[0]
        print(f"R0={self.registers[0]}, R1={self.registers[1]}")

    def show_help(self):
        print("\n=== 2-Bit-Prozessor (Echt 2-Bit!) ===")
        print("Befehle (2-Bit-Binär):")
        print("  00: NOP (Keine Operation)")
        print("  01: INC (R0 += 1)")
        print("  10: DEC (R0 -= 1)")
        print("  11: SWAP (R0 ↔ R1)")
        print("\nShell-Kommandos:")
        print("  echo: Zeige Register")
        print("  help: Hilfe")
        print("  exit: Beenden\n")

    def run_interactive(self):
        print("Echter 2-Bit-Prozessor! Gib 2-Bit-Befehle ein (00, 01, 10, 11).")
        print("Tipp: 'help' zeigt Optionen, 'echo' zeigt Register.\n")
        
        while self.running:
            cmd = input(">> ").strip().lower()
            
            if cmd == "exit":
                print("Programm beendet.")
                break
            elif cmd == "echo":
                print(f"R0={self.registers[0]}, R1={self.registers[1]}")
            elif cmd == "help":
                self.show_help()
            else:
                try:
                    instruction = int(cmd, 2)
                    if instruction > 0b11:
                        print("Fehler: Nur 2-Bit-Befehle (00, 01, 10, 11)!")
                    else:
                        self.execute(instruction)
                except ValueError:
                    print("Ungültig! Erlaubt: 2-Bit-Binär oder 'echo/help/exit'.")

# Hauptprogramm
if __name__ == "__main__":
    cpu = True2BitProcessor()
    cpu.run_interactive()
