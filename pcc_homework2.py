# -*- coding: utf-8 -*-

import os

def main():
	print "Hello World!"

	print "这是来自PCC的问候！"

	foo(5, 10)

	print '=' * 10
	print '这将直接执行：'+ os.getcwd()

	counter = 0
	counter += 1

	food = ["苹果", "杏仁", "李子", "梨"]
	for i in food:
		print '我就是爱吃：' + i

	print "数到10："
	for i in range(10):
		print i

def foo(param1,secondeParam):
	result = param1 + secondeParam
	print "%s 加 %s 等于 %s" % (param1, secondeParam, result)
	if result < 50:
		print "小于50哟"
	else:
		print "大于50哈"
	return result

if __name__ == '__main__':
	main()