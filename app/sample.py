#!/usr/bin/python
# -*- coding: utf8 -*-


# 32비트 unsigned 형으로 변환하는 함수 정의
def unsigned32(n):
  return n & 0xFFFFFFFF

# 본격적인 프로그램 시작

from zlib import crc32
import binascii
import base58

# 테스트용 문자열 정의
s = "한글테스트!!"
s = s.encode()

# 문자열의 CRC32 계산
#result = unsigned32(crc32(s))
result = binascii.crc32(s)

# 16진수로 출력
print (result)
print ("%08X" % (result))
# 출력 결과: DB1720A5

#print (base58.b58encode(str(result)))