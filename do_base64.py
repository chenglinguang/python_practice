#!/usr/bin/env python3 

#-*- coding:utf-8 -*-

#如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

import base64 


print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))



#自动补齐==
def safe_base64_decode(s):
    return base64.b64decode(s+b'='*(len(s)%4))


b=safe_base64_decode(b'YWJjZA==')
bb=safe_base64_decode(b'YWJjZA')

print(b)
print(bb)






