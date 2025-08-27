# .CORAL Framework Compiler / Interpreter (NEMO2)

## Overview

This project provides a **compiler–interpreter hybrid** for the **.CORAL framework**, a system designed to upgrade and extend **NEMOlang** and future `.CORAL`-based DSLs.

Unlike the legacy GNFR (Global Novaxis Framework and Runtime), `.CORAL` introduces:

* **Serialized IR Compilation (SIC)** → programs are compiled into **JSON IR** (via *JsnButler*), rather than bytecode.
* **Interpreter-based execution** → the JSON IR carries program structure and values, but execution is handled by this interpreter itself.
* **Better modularity and abstraction** → easier to adapt for new languages or platforms.
* **Improved documentation and formatting** compared to GNFR.

This repository contains the **reference implementation of .CORAL** for **NEMO 2 and later** (can be modified for your own DSLs).

---

## Features

* **Compilation to JSON IR** (via `JsnButler`)
* **Interpreter execution model**
* **2D tape memory model** (`x_tape` and `y_tape`) with independent pointers
* **SoF (`I`) and EoF (`$`) markers** for program validation
* **Command set** for tape manipulation, arithmetic, branching, I/O, and comments
* **Debug logging** (step counter, outputs stored in IR)
* **Extensible design** → easily add/remove commands or adapt to single-tape languages

---

## File Extensions

`NEMO2` recognizes the following file types by default:

* **`.nec`** — NEMO executable code
* **`.nemoc`** — NEMO code

If another extension is passed, the compiler will raise an error.

---

## Usage

### 1. Writing a Program

A `NEMO2` program must:

* Start with the **SoF marker** `I`
* End with the **EoF marker** `$`

Example:

```
I>AaP$
```

### 2. Running the Compiler

```bash
python3 NEMO2.py program.nec
```

This will:

* Parse the program
* Execute it instruction by instruction
* Generate a serialized JSON IR file named `program.json`

### 3. JSON IR Example

```json
{
  "program_name": "program.nec",
  "legal_file_extensions": [".nec", ".nemoc"],
  "tape": {
    "x_tape": [0, 1, 0, ...],
    "y_tape": [0, 0, 0, ...]
  },
  "pointers": {
    "x_pointer": 1,
    "y_pointer": 0
  },
  "outputs": [
    "A"
  ],
  "debug": {
    "steps_executed": 5
  }
}
```

---

## Command Set

### General

| Symbol  | Action                             |
| ------- | ---------------------------------- |
| `I`     | Program start (SoF marker)         |
| `$`     | Program end (EoF marker)           |
| `&.../` | Open (`&`) and close (`/`) comment |

### Pointer Movement

| Symbol | Action               |
| ------ | -------------------- |
| `>`    | Move X pointer right |
| `<`    | Move X pointer left  |
| `^`    | Move Y pointer up    |
| `~`    | Move Y pointer down  |

### Tape Operations

| Symbol  | Action                               |
| ------- | ------------------------------------ |
| `A / a` | Increment X / Y tape cell            |
| `M / m` | Decrement X / Y tape cell            |
| `C / c` | Remove current cell (X / Y)          |
| `S / s` | Save current cell (X / Y)            |
| `L / l` | Load saved value (X / Y)             |
| `P / p` | Print ASCII of cell (X / Y)          |
| `V / v` | Print raw value (X / Y)              |
| `F / f` | Jump pointer if cell is zero (X / Y) |
| `R / r` | Log current cell value to JSON IR    |

### Arithmetic

| Symbol | Action                       |
| ------ | ---------------------------- |
| `+`    | Add previous + next int      |
| `-`    | Subtract previous - next int |
| `*`    | Square current X cell        |
| `8`    | Square current Y cell        |
| `:`    | Set X cell to following int  |
| `;`    | Set Y cell to following int  |

### Input

| Symbol | Action                 |
| ------ | ---------------------- |
| `%`    | Input integer → X cell |
| `#`    | Input integer → Y cell |

---

## JSON IR Workflow

1. Source code (`.nec` / `.nemoc`) → parsed by `.CORAL`
2. Compiled into **JSON IR** (via JsnButler)
3. JSON IR used for:

   * Debugging
   * Interoperability with other DSLs
   * Program replaying/execution in `.CORAL`/`NEMO2` runtime

---

## Roadmap

* [ ] Expand instruction set
* [ ] Better error reporting & stack traces
* [ ] Cross-language runtime support
* [ ] Optimized IR storage format

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.
