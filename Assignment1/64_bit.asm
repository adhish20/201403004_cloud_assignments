; Adhish Singla
; 201403004

extern	printf

SECTION .data
	a:	dd	3
fmt:    db "a=%d, b=4, a+b=%d", 10, 0

SECTION .text
	global main
main:

	mov	rax,[a]
	add	rax,4
	mov	rdi,fmt
	mov	rsi,[a]
	mov	rdx,rax
	mov	rax,0
    call    printf

	mov	rax,0
	ret
