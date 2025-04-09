# True 2-Bit Processor

The **True 2-Bit Processor** is a minimalistic processor simulator designed to demonstrate how a processor with only two registers and 2-bit instructions operates. This project is interactive and allows users to input commands in binary format to observe the behavior of a truly constrained processor.

## Features

- **2 Registers**: Two 2-bit registers (`R0` and `R1`) hold values between `0b00` (0) and `0b11` (3).
- **2-Bit Instructions**: Supports basic operations using a compact 2-bit instruction set.
- **Memory**: Contains a small 2-bit memory array (`[0b00, 0b01, 0b10, 0b11]`).
- **Interactive Shell**: Users can input commands interactively and receive feedback on the state of the processor.
- **Error Handling**: Provides meaningful error messages for invalid inputs.

---

## Instruction Set

The processor supports the following 2-bit instructions:

| **Instruction** | **Binary Code** | **Description**                       |
|------------------|-----------------|---------------------------------------|
| NOP             | `00`            | No operation (does nothing).          |
| INC             | `01`            | Increment `R0` by 1 (wraps at 3).     |
| DEC             | `10`            | Decrement `R0` by 1 (wraps at 0).     |
| SWAP            | `11`            | Swap the values of `R0` and `R1`.     |

The processor also supports the following shell commands:

| **Command** | **Description**                                  |
|-------------|--------------------------------------------------|
| `echo`      | Show the current values of `R0` and `R1`.       |
| `help`      | Display the list of available commands.         |
| `exit`      | Terminate the program.                         |

---

## How to Run

### Prerequisites

- Python 3.6 or higher installed on your system.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/n-km/2bitprocessor.git
   ```


2. Run the processor:

```bash
python 2bit.py
```
Enter commands in the prompt (see Instruction Set above for details).
