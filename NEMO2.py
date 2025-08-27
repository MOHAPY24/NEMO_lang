# !/usr/bin/env python3
# Compiler/Interperter for the .CORAL framework based on NEMOlang ment to upgrade NEMOlang and future .CORAL languages
# The .CORAL framework is not a seperate language on its own and is based on the stock NEMOlang/GNFR (Global Novaxis Framework and Runtime) and is made to replace the weaker and floppy established stock framework built from Novaxis (GNFR) that was improperly ported.
# The .CORAL framework improves documentation, format, modular-ability, abstract-ability and replacing an outdated interperter (GNFR) to a Serialized IR Compiler (SIC)
# .CORAL doesnt compile into a runnable bytecode. Instead it compiles into serialized intermediate repersentation (IR) expressed in JSON. This JSON or most properly named JsnButler is used by the runtime to carry
# Values, Program structure and such over to the main runtime/language (for DSL purposes) but execution is handled by this so called "interperter" itself, not the JSON. In other words,
# .CORAL uses compilation into a serialized IR plus interperted execution.
# This version/file of .CORAL is used for the NEMO language for new versions from NEMO2 and future. (edit this with your language name/platform)
# If your creating a language with the framework, edit everything at your will and follow the rules of the MIT License in the LICENSE file.
# .CORAL Version 0.0.1



import json # to compile down to
import sys # to grab flags and file to be compiled

x_tape = [0] * 100 # define xtape
y_tape =[0] * 100 # define ytape (delete if your not making a 2d tape)
tape = [x_tape, y_tape] # define general tape (also delete if your not making a 2d tape)
xptr = 0 # define x pointer
yptr = 0 # define y pointer (delete this too if your not making a 2d tape)
comment_mode = False # for comments
try: # prevent IndexError / Troubleshoot if doesnt work :(
    filenamer = sys.argv[1]
except IndexError:
    raise FileNotFoundError(f"The passed file argument does not exist or was not put in as an argument.")
rcode = "" # code to be compiled/interperted, passed through by sys.argv[1]
legalfes = [".nec", ".nemoc"] # define the legal file extensions to be used, if file used with incorrect extension it wont run and will raise a FileNotFoundError
cjson = { # define basic json output skeletion, used to interop between languages and for IR
    "program_name": f'{filenamer}', # Name of the file
    "legal_file_extensions": legalfes, # Legal file extensions defined up ^^
    "tape": {
        "x_tape": x_tape, # x tape (currently 0, gets updated at end)
        "y_tape": y_tape # y tape (also currently 0 and gets updated at end (remove if not making 2d tape))
    },
    "pointers": {
        "x_pointer": xptr, # x pointer (currently 0, gets updated at end)
        "y_pointer": yptr  # y pointer (currently 0, also gets updated at end (remove if not making 2d tape))
    },
    "outputs": [
            # any outputs will be put here

    ],
    "debug": { # Debug options, add more here if wanted
        "steps_executed": 0, # how much commands ran
    }
} 

if legalfes[0] in filenamer: # if .nec is in the filename remove .nec to make a plain filename (edit the legalfes tape to add your file extensions)
    filenamew = filenamer.replace(legalfes[0], '')
elif legalfes[1] in filenamer: # if .nemoc is in the filename remove .nemoc to make a plain filename (edit the legalfes tape to add your file extensions)
    filenamew = filenamer.replace(legalfes[1], '')
else:
    raise FileNotFoundError(f"file '{filenamer}' does not have a valid file extension") # Raise FileNotFoundError if filename does not have a proper filename

file1 = open(filenamer, "r")
rcode = file1.read().strip() # open file, read code and store it in rcode/runtime code


if rcode.startswith("I") != True: # check if rcode has the SoF marker/initiliser I, otherwise raise RuntimeError (edit to fit your custom SoF or delete)
    raise RuntimeError("Code not properly initilized with 'I' at SoF.")
elif rcode.endswith("$") != True: # check if rcode has the EoF marker/ender $, otherwise raise RuntimeError (edit to fit your custom EoF or delete)
    raise RuntimeError("Code not properly closed with '$' at EoF.")
# Check if code contains SoF and EoF markers


for cmd in rcode.strip(): # for every char in code stripped (meaning the code doesnt have newlines or whitespaces) (if your reading by line make rcode.strip() to rcode.strip().splitlines())
    if cmd == "I": # I already has a function so means we can just skip it
        continue
    elif cmd == "$": # $ already has a function so means we can just skip it
        continue
    elif cmd == "!": # if command is ! remove current cell x_tape and move xptr back one
        if comment_mode:
             continue
        else:
            tape.remove(tape[tape.index(cmd)])
            xptr -= 1
    elif cmd == "%": # if command is % take user input and store in current xcell
        if comment_mode:
            continue
        else:
            tape[0][xptr] = int(input(">> "))
    elif cmd == "#": # if command is # take user input and store in current ycell
        if comment_mode:
            continue
        else:
            tape[1][yptr] = int(input(">> "))
    elif cmd == ":": # if command is : take the next int after it and make it the current cell value in xcell
        if comment_mode:
            continue
        else:
            u = int(rcode[rcode.index(cmd) + 1])
            tape[0][xptr] = u
    elif cmd == ";" : # if command is ; take the next int after anf make it current cell value in ycell
        if comment_mode:
            continue
        else:
            c = rcode[rcode.index(cmd) + 1]
            tape[1][yptr] = c
    elif cmd == ">": # if command is > move x pointer by one/ to the right
        if comment_mode:
            continue
        else:
            xptr += 1
    elif cmd == "<": # if command is < move y pointer minus one / to the left
        if comment_mode:
            continue
        else:
            xptr -= 1
    elif cmd == "^": # if command is ^ move y pointer up / plus one
        if comment_mode:
            continue
        else:
            yptr += 1
    elif cmd == "~": # if command is ~ move y_pointer down / minus one
        if comment_mode:
            continue
        else:
            yptr -= 1
    elif cmd == "*": # if command is * square current cell in x tape
        if comment_mode:
            continue
        else:
            tape[0][xptr] = tape[0][xptr] * tape[0][xptr]
    elif cmd == "8": # if command is 8 square current cell in y tape
        if comment_mode:
            continue
        else:
            tape[1][yptr] = tape[1][yptr] * tape[1][yptr]
    elif cmd == "&": # if command is & start comments
        if comment_mode:
            continue
        else:
            comment_mode == True
    elif cmd == "+": # if command is + add the int from before and int infront together
        if comment_mode:
            continue
        else:
            a = int(rcode[rcode.index(cmd) -1])
            b = int(rcode[rcode.index(cmd) +1])
            tape[0][xptr] = a + b
    elif cmd == "-": # if command is - subtract the int from before and the int infront together
        if comment_mode:
            continue
        else:
            a = int(rcode[rcode.index(cmd) -1])
            b = int(rcode[rcode.index(cmd) +1])
            tape[0][xptr] = a-b
    elif cmd == "/": # if command is / end comment
        comment_mode = False

    elif cmd == cmd.lower(): # check if the command is lower case (means it manipulates the y_tape) (delete if your not using case-sensitivity or a 2d tape)
        if cmd == "a": # if command is lower a add one to current cell in y_Tape and append one cell into the y_tape to prevent underflow
            if comment_mode: # this checks if comments are open, if yes dont run this, else run
                continue
            else:
                tape[1][yptr] += 1
                tape[1].append(0)
        elif cmd == "m": # if command is lower m subtract one from current cell in Y_tape 
            if comment_mode:
                continue
            else:
                tape[1][yptr] -= 1
        elif cmd == "c": # if command is lower c remove current cell from Y_tape and move pointer back one
            if comment_mode:
                continue
            else:
                tape[1].remove(tape[1][yptr])
                yptr -= 1
        elif cmd == "s": # if command is lower s save current cell value as ysave
            if comment_mode:
                continue
            else:
                ysave = tape[1][yptr]
        elif cmd == "s": # if command is lower s save current cell value as ysave
            if comment_mode:
                continue
            else:
                ysave = tape[1][yptr]
        elif cmd == "l": # if command is lower l load ysave into current cell
            if comment_mode:
                continue
            else:
                tape[1][yptr] = ysave
        elif cmd == "p": # if command is lower p print ascii of current value in current cell and store output in cjson
            if comment_mode:
                continue
            else:
                print(chr(tape[1][yptr]), end='')
                cjson["outputs"] += f"{chr(tape[1][yptr])}"
        elif cmd == "v": # if command is lower v print raw cell value and store output in cjson
            if comment_mode:
                continue
            else:
                print(tape[1][yptr])
                cjson["outputs"] += {tape[1][yptr]}
        elif cmd == "f": # if command is lower f if current cell == 0 go to n cell
            if comment_mode:
                continue
            else:
                i = rcode[rcode.index(cmd) + 1]
                if tape[1][yptr] == 0:
                    if i.isdigit():
                        yptr = int(i)
                    else:
                        raise SyntaxError(f"cannot go to ycell {i} as it is not a valid inttype")
        elif cmd == "r": # if command is lower r in json log current cell val
            if comment_mode:
                continue
            else:
                cjson["outputs"] += {tape[1][yptr]}
    elif cmd == cmd.capitalize(): # check if the command is capital case (means it manipulates the x_tape (delete if not using 2d tape or not using case sensitivity))
        if cmd == "A": # if command is capital A add one to current cell in x_Tape and append one cell into the x_tape to prevent underflow
            if comment_mode:
                continue
            else:
                tape[0][xptr] += 1
                tape[0].append(0)
        elif cmd == "M": # if command is capital M subtract one from current cell in Y_tape 
            if comment_mode:
                continue
            else:
                tape[0][xptr] -= 1
        if cmd == "C": # if command is capital C remove current cell from X_tape and move pointer back one
            if comment_mode:
                continue
            else:
                tape[0].remove(tape[0][xptr])
                xptr -= 1
        elif cmd == "S": # if command is capital S save current cell value as xsave
            if comment_mode:
                continue
            else:
                xsave = tape[0][xptr]
        elif cmd == "L": # if command is capital L load xsave into current cell
            if comment_mode:
                continue
            else:
                tape[0][xptr] = xsave
        elif cmd == "P": # if command is capital P print ascii of current value in current cell and store output in cjson
            if comment_mode:
                continue
            else:
                print(chr(tape[0][xptr]), end='')
                cjson["outputs"] += f"{chr(tape[0][xptr])}"
        elif cmd == "V": # if command is capital V print raw cell value and store output in cjson
            if comment_mode:
                continue
            else:
                print(tape[0][xptr])
                cjson["outputs"] += {tape[0][xptr]}
        elif cmd == "F": # if command is capital F if current cell == 0 go to n cell
            if comment_mode:
                continue
            else:
                i = rcode[rcode.index(cmd) + 1]
                if tape[0][xptr] == 0:
                    if i.isdigit():
                        xptr = int(i)
                    else:
                        raise SyntaxError(f"cannot go to xcell {i} as it is not a valid inttype")
        elif cmd == "R": # if command is capital R in json log current cell val
            if comment_mode:
                continue
            else:
                cjson["outputs"] += tape[0][xptr]

    cjson["debug"]["steps_executed"] += 1




        
            
with open(f"{filenamew}.json", "w") as f: # open json file if doesnt exist it will make a new one with the same filename as your main code
    cjson["tape"] = { # add updated tapes

    "x_tape": x_tape,
    "y_tape": y_tape # delete if your not using 2d tapes

},
    cjson["pointers"] = { # add updated pointers

        "x_pointer": xptr,
        "y_pointer": yptr # delete if your not using 2d tapes
},
    
    f.write(json.dumps(cjson)) # insert json values into json file
    file1.close() # properly close first file
    f.close() # properly close json file