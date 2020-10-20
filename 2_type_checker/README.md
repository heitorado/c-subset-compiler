# Part 2: Type checker of C code using Visitor pattern with Python
## Specifications
### The following assignments should be supported:
- int var = FloatExpression
 - This will generate a _warning_ notifying about possible information loss.
- float var = IntExpression

Any other assignment of different types should show a type error.

### The following operations should be supported:

They are in the format [Type1 OPERATOR Type2 -> ResultType]

- int +| - | * | / int -> int
- float + | - | * | / float -> float
- int + | - | * | / float -> float
- int < | <= | == | >= | > | != int -> int
- float < | <= | == | >= | > | != float -> int
- Any other operation with different types should exhibit a type error.

Expressions that are the index of an array must be of type 'int'.
The type errors should indicate the line and cause of the triggered error.


## Running
```
make < test_input.c
```
