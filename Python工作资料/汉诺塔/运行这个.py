#-*- coding:utf-8 -*-
def move(n,a,b,c):
	if n ==1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		print(a,'-->',c)
		move(n-1,b,a,c)
x=int(input('请输入汉诺塔层数：'))
move(x,'A','B','C')