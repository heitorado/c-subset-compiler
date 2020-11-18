python3 antlr4-python3-runtime-4.7.2/src/main.py
define i32 @square(i32 %0) {
  %2 = mul nsw i32 %0, %0
  ret i32 %2
}

define void @splash() {
  ret void
}

define i32 @main() {
  call void @splash()
  %1 = call i32 @square(i32 2)
  ret i32 %1
}

