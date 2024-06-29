

'''
python History : 

Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation.

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, 
including structured (particularly procedural), object-oriented and functional programming. 
It is often described as a "batteries included" language due to its comprehensive standard library.

Guido van Rossum began working on Python in the late 1980s as a successor to the 
ABC programming language and first released it in 1991 as Python 0.9.0.
Python 2.0 was released in 2000. Python 3.0, released in 2008, 
was a major revision not completely backward-compatible with earlier versions.
Python 2.7.18, released in 2020, was the last release of Python 2.

'''

'''
How does the Python interpreter work? 

1. When we run source code (a file with a .py extension), 
the lexer (a component of the Python interpreter) divides the line of code 
into tokens (a process known as lexing). 

2. The parser (another component of the Python interpreter) uses these tokens to 
construct a structure called an "Abstract Syntax Tree", which depicts the relationship 
between these tokens (a process known as parsing). 

3. If an error occurs during the parsing stage, the Python interpreter will stop the 
translation and display an error message (syntax error). 

4. If no errors are found, the compiler (another Python interpreter component) converts 
the Abstract Syntax Tree into intermediate language code,
also known as byte code (a compiled version is known as byte code). 

5. This byte code is saved in a file called ".pyc," which is the same as the name of the source code 
file. 

6. Bytecode is a platform-independent representation of source code at a low level. 

7. The Python Virtual Machine (PVM) (another Python interpreter component) loads 
the bytecode (along with the inputs and library modules) into the Python runtime 
and converts it to machine-executable code (0's and 1's in binary). 

8. It displays an error message if an error occurs (a runtime error). 
It prints the output if no errors occur during execution.


'''