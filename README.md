

# 🐟 NEMO Interpreter (Python DSL)

**Version:** 1.0.0  
NEMO is a **Python-dependent domain-specific language (DSL)** designed for simple 2D memory manipulation and I/O operations.  
It runs on top of Python and provides a minimal, single-character instruction set for interacting with **two separate memory tapes that act like seperate languages** as it is also 
a **Meta-paradigm** language meaning it acts as Multi-paradigm before runtime then becomes paradigm during execution.

---

## 📜 Overview

NEMO is implemented entirely in Python and provides:
- Two integer tapes (`x_tape` and `y_tape`) representing horizontal and vertical memory.
- Two independent pointers (`x_pointer`, `y_pointer`) to navigate and modify values.
- An instruction set for memory operations, arithmetic, I/O, and conditional jumps.


This DSL can be used for:
- Lightweight algorithm prototyping.
- Educational demos of pointer/memory-based execution.
- Scriptable 2D data manipulation inside Python.
- Numeric value defininition for objects inside Python

---

## 🚀 Features

- Dual tapes for X and Y dimensions (that act like microlangs seperate).
- Independent pointer movement in both dimensions.
- Integer and character I/O support.
- Save/Load registers for temporary storage.
- Conditional branching based on tape values.
- Python API for running NEMO code from within Python scripts.

---

## 📦 Installation

```bash
git clone https://github.com/MOHAPY24/NEMO_lang.git
```
in python
```python
from nemo_lang import NEMO
```

---

## 🖋 Syntax & Commands

A valid NEMO program:

* **Must start** with `I`
* **Must end** with `$`

| Command | Description                                         |
| ------- | --------------------------------------------------- |
| `I`     | Start of program                                    |
| `$`     | End of program                                      |
| `A`     | Increment current X cell                            |
| `a`     | Increment current Y cell                            |
| `M`     | Decrement current X cell                            |
| `m`     | Decrement current Y cell                            |
| `!`     | Reset current X cell                                |
| `c`     | Reset current Y cell                                |
| `>`     | Move `x_pointer` right                              |
| `<`     | Move `x_pointer` left                               |
| `^`     | Move `y_pointer` up                                 |
| `~`     | Move `y_pointer` down                               |
| `P`     | Print X cell as a character                         |
| `p`     | Print Y cell as a character                         |
| `V`     | Print X cell as an integer                          |
| `v`     | Print Y cell as an integer                          |
| `%`     | Input integer into X cell                           |
| `#`     | Input integer into Y cell                           |
| `S`     | Save current X cell to register                     |
| `s`     | Save current Y cell to register                     |
| `L`     | Load saved value into X cell                        |
| `l`     | Load saved value into Y cell                        |
| `+`     | Add two surrounding digits and store in X cell      |
| `-`     | Subtract two surrounding digits and store in X cell |
| `X`     | Multiply two surrounding digits and store in X cell |
| `D`     | Divide two surrounding digits and store in X cell   |
| `*`     | Square current X cell                               |
| `8`     | Square current Y cell                               |
| `F`     | Jump X pointer if current X cell == 0               |
| `f`     | Jump Y pointer if current Y cell == 0               |
| `&`     | Start comment mode                                  |
| `/`     | End comment mode                                    |
| `R`     | Return y_Cell                                       |
| `r`     | Return x_Cell                                       |
| `T`     | Return x_Tape                                       |
| `t`     | Return y_Tape                                       |

---


## 🛠 Example Usage


```python
# Create interpreter with 10x10 tapes
n = NEMO(10, 10)

code = "I:8*AAAAAAAAAPAP$" # Prints HI
# Load program
n.add(code)

# Run it
n.run()
```

**Output:**

```NEMO
Hi
```

---

## ⚠ Notes & Limitations

* NEMO runs **inside Python** — it is not a standalone language.
* The memory size is fixed at initialization.
* Out-of-bounds pointer movement raises `MemoryError`.
* Code parsing is **linear** — no separate compilation step.

---

## 📄 License

MIT License — free to use, modify, and distribute.
