@
@ Assembler program to print "Hello World!"
@ to stdout.@
@ R0-R2- parameters to linux function service
@ R7- linux function number
@

.global _start

@ Provide program starting@ address to linker
@ Set up the parameters to print hello world
@ and then call Linux to do it.

_start: 
    mov R0, #1                  @ 1 = StdOut 
    ldr R1, =helloworld         @ string to print, Load Register R1 with adress of string helloworld 
    mov R2, #13                 @ length of our string, Move number 13 into Register 2
    mov R7, #4                  @ linux write system call, Move number 4 into Register R7 
    svc 0                       @ Call linux to print, send control to interupt handler in linux kernel and interpret Register 

@ Set up the parameters to exit the program
@ and then call Linux to do it.

    mov R0, #0                  @ Use 0 return code
    mov R7, #1                  @ Service command code 1

                                @ terminates this program
    svc 0                       @ Call linux to terminate

.data                                   @ Data Section

helloworld: .ascii "Hello World!\n"     @ Ascii - Text - Data 
