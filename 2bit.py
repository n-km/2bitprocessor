import sys

class Processor2Bit:
    def __init__(self):
        self.registers = [0, 0]  # Zwei 2-Bit-Register
        self.memory = [0b00, 0b01, 0b10, 0b11]  # Einfacher 2-Bit-Speicher
        self.program_counter = 0
        self.running = True  # Kontrolliert, ob der Prozessor weiterlaufen soll

    def execute(self, instruction):
        opcode = (instruction & 0b1100) >> 2
        reg1 = (instruction & 0b0010) >> 1
        reg2 = instruction & 0b0001

        if opcode == 0b00:  # Addition
            self.registers[reg1] = (self.registers[reg1] + self.registers[reg2]) & 0b11
            print(f"Addition: Register[{reg1}] = {self.registers[reg1]}")
        elif opcode == 0b01:  # Subtraktion
            self.registers[reg1] = (self.registers[reg1] - self.registers[reg2]) & 0b11
            print(f"Subtraktion: Register[{reg1}] = {self.registers[reg1]}")
        elif opcode == 0b10:  # AND
            self.registers[reg1] = self.registers[reg1] & self.registers[reg2]
            print(f"AND: Register[{reg1}] = {self.registers[reg1]}")
        elif opcode == 0b11:  # Load
            self.registers[reg1] = self.memory[reg2]
            print(f"Lade Wert: Register[{reg1}] = {self.registers[reg1]}")
        elif opcode == 0b100:  # Echo
            self.echo(reg1, reg2)
        elif opcode == 0b101:  # Exit
            self.exit()
        elif opcode == 0b110:  # Help
            self.help()
        else:
            print(f"Unbekannter Opcode: {opcode}")

    def echo(self, reg1, reg2):
        """Gibt den Inhalt eines Registers oder einen direkten Wert aus."""
        if reg1 == 0:
            print(f"Echo (Register): {self.registers[reg2]}")
        else:
            print(f"Echo (Wert): {reg2}")

    def exit(self):
        """Stoppt die Ausführung des Programms."""
        print("Programm beendet.")
        self.running = False

    def help(self):
        """Zeigt eine Liste der verfügbaren Kommandos und ihre Beschreibung."""
        print("Verfügbare Kommandos:")
        print("  00: Addition - Addiere zwei Register")
        print("  01: Subtraktion - Subtrahiere ein Register von einem anderen")
        print("  10: AND - Führe eine logische UND-Operation zwischen zwei Registern durch")
        print("  11: Load - Lade einen Wert aus dem Speicher in ein Register")
        print("  100: Echo - Gib den Inhalt eines Registers oder einen direkten Wert aus")
        print("  101: Exit - Beende das Programm")
        print("  110: Help - Zeige diese Hilfe an")

    def run_interactive(self):
        """Interaktiver Modus für manuelle Eingabe von Kommandos."""
        print("Interaktiver Prozessor gestartet. Drücke Strg+C, um das Programm zu beenden.")
        print("Gib eine 4-Bit-Binärzahl ein (z. B. 1100 für Load), oder 'exit', um das Programm zu stoppen.")

        try:
            while self.running:
                user_input = input(">> ").strip()

                if user_input.lower() == "exit":
                    self.exit()
                    break

                # Konvertiere Eingabe in eine Binärzahl
                try:
                    instruction = int(user_input, 2)  # Binäre Eingabe (z. B. "1100")
                    self.execute(instruction)
                    print(f"Aktuelle Register: {self.registers}")
                except ValueError:
                    print("Ungültige Eingabe! Bitte gib eine 4-Bit-Binärzahl ein.")
        except KeyboardInterrupt:
            print("\nProgramm durch Strg+C beendet.")
            sys.exit(0)


# Programm starten
if __name__ == "__main__":
    processor = Processor2Bit()
    processor.run_interactive()
