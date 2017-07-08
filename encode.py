#! /usr/local/bin/python3

print('A字符的整数表示为：', ord('A'))
print('66对应的字符为：', chr(66))
print('AB以ascii编码的字节为：', 'AB'.encode('ascii'))
print('中文以utf-8编码的字节为：', '中文'.encode('utf-8'))
print('b\'\\xe4\\xb8\\xad\\xe6\\x96\\x87\'的解码为：', b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
