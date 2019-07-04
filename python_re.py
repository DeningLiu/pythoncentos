#/usr/bin/python3.6
# -*- coding=utf-8 -*-
# write by Darin

import re

str1 = 'GE6/1                    down     down     192.168.56.3    --'

result = re.match('\s*(\w.*\d)\s+(\w*)\s+(\w*)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(--|\w*)',str1).groups()

print(result)
print('-'*80)
print('%-7s : %s'%('接口',result[0]))
print('%-7s : %s'%('物理',result[1]))
print('%-7s : %s'%('协议',result[2]))
print('%-7s : %s'%('地址',result[3]))
print('%-7s : %s'%('描述',result[4]))


if __name__ == '__main__':
    pass