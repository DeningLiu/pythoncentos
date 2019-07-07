#/usr/bin/python3.6
# -*- coding=utf-8 -*-
# write by Darin

import re


str2 = '166   54a2.74f7.2f8e    DYNAMYIC           Gi1/0/11'


result2 = re.match('\s*(\d{1,4})\s+(\w{1,4}\.\w{1,4}\.\w{1,4})\s+(\w+)\s+(.*)\s*',str2).groups()

print(result2)
print('-'*80)
print('%-10s : %s'%('VLAN ID',result2[0]))
print('%-10s : %s'%('MAC',result2[1]))
print('%-10s : %s'%('Type',result2[2]))
print('%-10s : %s'%('Interface',result2[3]))
print('-'*80)



if __name__ == '__main__':
    pass