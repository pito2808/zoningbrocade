#!/usr/bin/env python3

import os
import sys
import yaml
import pprint

fc_port = {}
with open('./zoning.yaml') as f :
    fc_port = yaml.load(f)

print(fc_port['initiators'])
print(fc_port['targets'])

#{'gtnbs_es002_vmhba2': '50:01:43:80:28:14:59:9e', 'gtnbs_es001_vmhba2': '50:01:43:80:28:14:58:b4', 'gtnbs_es004_vmhba2': '50:01:43:80:28:14:59:d0'}
#{'gtnbs_st001_ctrlb_1a': '50:0a:09:81:98:44:80:06', 'gtnbs_st001_ctrla_1a': '00:0a:09:81:88:44:80:06'}

initiators_dict = fc_port['initiators']
targets_dict = fc_port['targets']
cfg_name = fc_port['cfgname']
zone_list = []
# alicreate
for i in initiators_dict:
    print('alicreate "{}","{}"'.format(i.replace('-','_'),initiators_dict[i]))
for t in targets_dict:
    print('alicreate "{}","{}"'.format(t.replace('-','_'),targets_dict[t]))

print('\n\n')

for i in initiators_dict:
    for t in targets_dict:
        #print(i,initiators_dict[i], t )
        initiator = i.replace('-','_')
        target = t.replace('-','_')
        zone_name = initiator +'_'+ target
        print('zonecreate "{}","{};{}"'.format(zone_name, initiator, target ))
        zone_list.append(zone_name)

print('\n\n')

n = len(zone_list)
i = 0
list_str =''
for z in zone_list:
    list_str = list_str + z
    i += 1
    if i != n:
        list_str = list_str + ';'

print('cfgcrate "{}","{}"'.format(cfg_name,list_str))
print('\n\n')

for z in zone_list:
    print('cfgadd "{}","{}"'.format(cfg_name, z))

print('\n\n')
print('cfgenable', cfg_name)
