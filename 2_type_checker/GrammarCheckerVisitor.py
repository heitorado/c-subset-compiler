# Generated from antlr4-python3-runtime-4.7.2/src/autogen/Grammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

'''
COMO RESGATAR INFORMAÇÕES DA ÁRVORE

Observe o seu Grammar.g4. Cada regra sintática gea uma função com o nome corespondente no Visitor e
na ordem em que está na gramática. Para deixar na ordem em que você colocou, substitua as funções dentro
de "class GrammarCheckerVisitor(ParseTreeVisitor)" pelas que apareem em autogem/GrammarVisitor.g4 depoi
do make ser rodado. Mas antes algumas mudanças precisam ser feitas em Grammar.g4. Primeiro copie-a do 
projeto1 para o projeto2. Depois adicione o tipo "VOID: 'void'" no lexer e na regra de "type" no parser 
(só "| VOID" aqui). Agora, por causa de conflitos com Python, substitua as regras file por fiile e type 
por type ("make adjust" substitui automaticamente). Use prints temporários para ver se está no caminho
certo.  "make tree" agora desenha a árvore sintática, se quiser vê-la para qualquer input, enquanto "make"
roda este visitor sobre o a árvore gerada a partir de Grammar.g4 alimentada pelo input.


expr = ctx.expression().accept(self)  # entra no nó expression e seus filhos e retorna alguma coisa

for i in range(len(ctx.identifier())): # para cada identficador que este nó possui...
    ident = ctx.identifier()[i].accept(self) # ...pegue o i-ésimo

if ctx.FLOAT() != None: # se houver um FLOAT (em vez de INT ou VOID) neste nó (parser)
    return Type.FLOAT # retorne float
'''

# retorne Type.INT, etc para fazer checagem de tipos
class Type:
    VOID = "void"
    INT = "int"
    FLOAT = "float"
    STRING = "string"

class GrammarCheckerVisitor(ParseTreeVisitor):
    # armazenar da forma 'identificador: tipo'
    ids_defined = {} # armazenar informações necessárias para cada identifier definido

    # Visit a parse tree produced by GrammarParser#fiile.
    def visitFiile(self, ctx:GrammarParser.FiileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#function_definition.
    def visitFunction_definition(self, ctx:GrammarParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#body.
    def visitBody(self, ctx:GrammarParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#if_statement.
    def visitIf_statement(self, ctx:GrammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#else_statement.
    def visitElse_statement(self, ctx:GrammarParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_loop.
    def visitFor_loop(self, ctx:GrammarParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_initializer.
    def visitFor_initializer(self, ctx:GrammarParser.For_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_condition.
    def visitFor_condition(self, ctx:GrammarParser.For_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_step.
    def visitFor_step(self, ctx:GrammarParser.For_stepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variable_definition.
    def visitVariable_definition(self, ctx:GrammarParser.Variable_definitionContext):
        for i in range(len(ctx.array())):
            text = ctx.array(i).identifier().getText()
            self.ids_defined[text] = ctx.tyype().getText()
            #print("Array Definition: ({},{})".format(text, self.ids_defined[text]))
        
        for i in range(len(ctx.identifier())):
            text = ctx.identifier(i).getText()
            token = ctx.identifier(i).IDENTIFIER().getPayload()
            self.ids_defined[text] = ctx.tyype().getText()
            #print("Variable Definition: ({},{})".format(text, self.ids_defined[text]))
            if ctx.expression(i) != None:
                expr_type = self.visitExpression(ctx.expression(i))
                var_type = self.ids_defined.get(text, Type.VOID)
                if expr_type != var_type:
                    if var_type == Type.FLOAT and expr_type == Type.INT:
                        continue
                    elif var_type == Type.INT and expr_type == Type.FLOAT:
                        print("[WARNING]::[This assignment of FLOAT to INT can cause loss of information. But apparently that is not the only thing that is lost here.] ({},{})".format(str(token.line), str(token.column)))
                    else:
                        print("[ERROR]::[Do you know how to define a variable? You can't assign <{}> to <{}>, FYI.] ({},{})".format(expr_type, var_type, str(token.line), str(token.column)))

        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variable_assignment.
    def visitVariable_assignment(self, ctx:GrammarParser.Variable_assignmentContext):
        if ctx.expression() != None:
            expr_type = self.visitExpression(ctx.expression())

            if ctx.identifier() != None: # Identifier
                token = ctx.identifier().IDENTIFIER().getPayload()
                text = ctx.identifier().getText()
                id_type = self.ids_defined.get(text, Type.VOID)

            else: # Array
                token = ctx.array().identifier().IDENTIFIER().getPayload()
                text = ctx.array().identifier().getText()
                id_type = self.ids_defined.get(text, Type.VOID)

            # Check the types of the variable that is receiving the assignment and the value being assigned.
            if not (id_type == expr_type or (id_type == Type.INT and expr_type == Type.FLOAT)):
                #print(str(id_type == Type.INT and expr_type == Type.FLOAT))
                print("[ERROR]::[Oh. My. God. You just tried to assign <{}> to <{}>. Wow.] ({},{})".format(expr_type, id_type, str(token.line), str(token.column)))
            elif id_type == Type.INT and expr_type == Type.FLOAT:
                print("[WARNING]::[This assignment of FLOAT to INT can cause loss of information. But apparently that is not the only thing that is lost here.] ({},{})".format(str(token.line), str(token.column)))
            return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        tyype = Type.VOID
        if len(ctx.expression()) == 0:
            if ctx.integer() != None:
                text = ctx.integer().getText()
                token = ctx.integer().INTEGER().getPayload()
                #print("Integer: '" + text + "' => line: " + str(token.line) + " , col: " + str(token.column))
                tyype = Type.INT
            elif ctx.floating() != None:
                text = ctx.floating().getText()
                token = ctx.floating().FLOATING().getPayload()
                #print("Floating: '" + text + "' => line: " + str(token.line) + " , col: " + str(token.column))
                tyype = Type.FLOAT
            elif ctx.string() != None:
                tyype = Type.STRING
            elif ctx.identifier() != None:
                text = ctx.identifier().getText()
                token = ctx.identifier().IDENTIFIER().getPayload()
                #print("Identifier: '" + text + "' => line: " + str(token.line) + " , col: " + str(token.column))
                #print(self.ids_defined)
                tyype = self.ids_defined.get(text, Type.VOID)
            elif ctx.array() != None:
                text = ctx.array().identifier().getText()
                token = ctx.array().identifier().IDENTIFIER().getPayload()
                tyype = self.ids_defined.get(text, Type.VOID)
                #print("Array Identifier: '" + ctx.array().identifier().getText() + "[]' => line: " + str(token.line) + " , col: " + str(token.column))
                #print("Array type: [{}]".format(tyype))
            elif ctx.function_call() != None:
                #print("Function Call: '" + ctx.function_call().identifier().getText() + "()'")

                for i in range(len(ctx.function_call().expression())):
                    arg_type = self.visit(ctx.function_call().expression(i))
                    #print("arg[" + str(i) + "]")

        elif len(ctx.expression()) == 1:
            if ctx.OP != None:
                text = ctx.OP.text
                token = ctx.OP
                #print("Unary Operator: '" + text + "' => line : " + str(token.line) + ", col: " + str(token.column))
                tyype = self.visit(ctx.expression(0))
            else:
                #print("(")
                tyype = self.visit(ctx.expression(0))
                #print(")")

        elif len(ctx.expression()) == 2:
            text = ctx.OP.text
            token = ctx.OP
            #print("Binary Operator: '" + text + "' => line: " + str(token.line) + " , col: " + str(token.column))
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            if ctx.OP.text in ['<', '<=', '==', '>=', '>', '!=']:
                if left != right:
                    print("[ERROR]::[Good lord, what were you thinking trying to do a '{} {} {}' operation? Please, fix that type error. But do it right this time, yes?] ({},{})".format(left, ctx.OP.text, right, str(token.line), str(token.column)))

            elif ctx.OP.text in ['+', '-', '*', '/']:
                if not(left == right or (left == Type.INT and right == Type.FLOAT)):
                    #print("left = {}".format(left))
                    #print("right = {}".format(right))
                    #print(self.ids_defined)
                    print("[ERROR]::[Good lord, what were you thinking trying to do a '{} {} {}' operation? Please, fix that type error. But do it right this time, yes?] ({},{})".format(left, ctx.OP.text, right, str(token.line), str(token.column)))
            tyype = right
        return tyype


    # Visit a parse tree produced by GrammarParser#array.
    def visitArray(self, ctx:GrammarParser.ArrayContext):
        #token = ctx.identifier().IDENTIFIER().getPayload()
        #print(str(token.line) + "|" + ctx.expression().getText())
        index_type = self.visit(ctx.expression())
        if index_type != Type.INT:
            token = ctx.identifier().IDENTIFIER().getPayload()
            print("[ERROR]::[I tought you knew that an array index should be an INTEGER instead of <{}>.] ({},{})".format(index_type,str(token.line),str(token.column))) 
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#array_literal.
    def visitArray_literal(self, ctx:GrammarParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#function_call.
    def visitFunction_call(self, ctx:GrammarParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arguments.
    def visitArguments(self, ctx:GrammarParser.ArgumentsContext):
        for i in range(len(ctx.identifier())):
            text = ctx.identifier(i).getText()
            self.ids_defined[text] = ctx.tyype(i).getText()
            #print("Function Argument {}: ({},{})".format(i, text, self.ids_defined[text]))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#tyype.
    def visitTyype(self, ctx:GrammarParser.TyypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#integer.
    def visitInteger(self, ctx:GrammarParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#floating.
    def visitFloating(self, ctx:GrammarParser.FloatingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#string.
    def visitString(self, ctx:GrammarParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#identifier.
    def visitIdentifier(self, ctx:GrammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    #del GrammarParser

    #def aggregateResult(self, aggregate:Type, next_result:Type):
        #return next_result if next_result != None else aggregate
