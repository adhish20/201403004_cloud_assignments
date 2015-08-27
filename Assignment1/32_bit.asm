; Adhish Singla
; 201403004

extern	printf

SECTION .data
	a:	dd	3
fmt:    db "a=%d, b=4, a+b=%d", 10, 0

SECTION .text
	global main
main:
	
	mov	eax,[a]
	add	eax,4
	mov	edi,fmt
	mov	esi,[a]
	mov	edx,eax
	mov	eax,0
	call    printf

	mov	eax,0
	ret
