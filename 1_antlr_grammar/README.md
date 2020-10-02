# Part 1: Parser generation from grammar with ANTLR
## Specifications
### Language Specs:
- **file**: root grammar rule
- **function_definition**: rule that describes the definition of a function
- **arguments**: rule that define the format of the arguments on a function declaration/call
- **body**: rule that describes a statement inside curly brackets
- **statement**: rule that will contain different types of statements
- **if_statement**: rule that defines the format of an 'if'
- **else_statement**: rule that defines the format of an 'else'
- **for_loop**: rule that defines the format of a 'for'
- **for_initializer**: rule that defines the first parameter (initializer) of the 'for' statement
- **for_condition**: rule that defines the second parameter (conditional) of the 'for' statement
- **for_step**: rule that defines the third parameter (step) of the 'for' statement
- **variable_definition**: rule that defines the format of a variable definition
- **variable_assignment**: rule that defines the format of the assignment of a value to a variable
- **expression**: rule that defines the different kinds of expressions present on the language (arithmetic, function call, etc)
- **array**: rule that defines the format of the array declaration
- **array_literal**: rule that defines the format of an array literal
- **function_call**: rule that defines the format of a function call
- **type**: rule that defines the types present on the language

Also, the language should support the types:
- _int_
- _float_
- _string_

It should also support line comments with '//' and block comments with '/* */'.

## Running
```
make < sample_codes/00.c
make < sample_codes/01m.c
make < sample_codes/02.c
```
