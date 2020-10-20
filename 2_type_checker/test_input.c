#include <stdio.h>
#include <math.h>
#include "meh.h"

// THIS IS AN UNOFFICIAL TEST CODE.
// AS FAR AS I UNDERSTOOD THAT PROJECT SPECIFICATION,
// THIS CODE SHOULD TRIGGER:
// - WARNINGS ON LINES: 18, 25, 27 and [63 to 70].
// - ERRORS ON LINES: [73 to 80], [146,150,154,158,162,166,170,174,178,182,186,190], [194-199], [201-206], [220-223] and [226-229].

int main() {

    //CORRECT
    int myInt = 10;
    float myFloat = 5.0;

    //WARNING
    int myIntDefinedFloat = 6.0;
    //CORRECT
    int myFloatDefinedInt = 1;
    int willStoreFloatInThisInt;
    //ERROR
    int myIntBlaBla = "whatever";
    //WARNING
    willStoreFloatInThisInt = myFloat;
    //WARNING
    willStoreFloatInThisInt = myFloat + myFloat + myFloat + myFloat;
    
    //CORRECT
    int a,b,c,d,x;
    float e,f,g,h,y;

    x = a + b;
    x = a - b;
    x = a * b;
    x = a / b;
    x = (a + b) + (c + d);
    x = (a - b) - (c - d);
    x = (a * b) * (c * d);
    x = (a / b) / (c / d);

    //CORRECT
    y = e + f;
    y = e - f;
    y = e * f;
    y = e / f;
    y = (e + f) + (g + h);
    y = (e - f) - (g - h);
    y = (e * f) * (g * h);
    y = (e / f) / (g / h);

    //CORRECT
    y = a + h;
    y = a - h;
    y = a * h;
    y = a / h;
    y = (a + b) + (g + h);
    y = (a - b) - (g - h);
    y = (a * b) * (g * h);
    y = (a / b) / (g / h);

    //WARNING
    x = a + h;
    x = a - h;
    x = a * h;
    x = a / h;
    x = (a + b) + (g + h);
    x = (a - b) - (g - h);
    x = (a * b) * (g * h);
    x = (a / b) / (g / h);

    //ERROR
    x = e + a;
    x = e - a;
    x = e * a;
    x = e / a;
    x = (e + f) + (b + a);
    x = (e - f) - (b - a);
    x = (e * f) * (b * a);
    x = (e / f) / (b / a);

    //CORRECT
    if(a < b) {
        printf("foo");
    }

    if(a <= b){
        printf("foo");
    }

    if(a == b) {
        printf("foo");
    }

    if(a != b){
        printf("foo");
    }

    if(a > b) {
        printf("foo");
    }

    if(a >= b){
        printf("foo");
    }

    if(e < f) {
        printf("foo");
    }

    if(e <= f){
        printf("foo");
    }

    if(e == f) {
        printf("foo");
    }

    if(e != f){
        printf("foo");
    }

    if(e > f) {
        printf("foo");
    }

    if(e >= f){
        printf("foo");
    }

    x = a < b;
    x = a <= b;
    x = a == b;
    x = a != b;
    x = a > b;
    x = a >= b;

    y = e < f;
    y = e <= f;
    y = e == f;
    y = e != f;
    y = e > f;
    y = e >= f;

    // ERROR
    if(e < b) {
        printf("foo");
    }

    if(e <= b){
        printf("foo");
    }

    if(e == b) {
        printf("foo");
    }

    if(e != b){
        printf("foo");
    }

    if(e > b) {
        printf("foo");
    }

    if(e >= b){
        printf("foo");
    }

    if(a < f) {
        printf("foo");
    }

    if(a <= f){
        printf("foo");
    }

    if(a == f) {
        printf("foo");
    }

    if(a != f){
        printf("foo");
    }

    if(a > f) {
        printf("foo");
    }

    if(a >= f){
        printf("foo");
    }

    x = e < b;
    x = e <= b;
    x = e == b;
    x = e != b;
    x = e > b;
    x = e >= b;

    y = a < f;
    y = a <= f;
    y = a == f;
    y = a != f;
    y = a > f;
    y = a >= f;

    // CORRECT
    int myIntArray[40];
    float myFloatArray[50];

    myFloatArray[x] = f + e;
    myIntArray[x] = (x + x) * (a / b);
    myIntArray[x + (a*b) - c] = 44;

    x = myIntArray[10];
    myIntArray[15] = (x + a) * b;

    //ERROR
    myFloatArray[y] = x;
    myFloatArray[(y + f) * e] = f;
    int myWrongArray[5.0];
    myIntArray[6.66] = 8;

    //ERROR
    iNeverDefinedThisVariable = x;
    x = iNeverDefinedThisVariable;
    x = "string test";
    int myLastInt = iNeverDefinedThisVariable;
}