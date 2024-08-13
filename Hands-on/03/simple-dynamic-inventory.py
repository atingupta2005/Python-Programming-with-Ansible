#!/usr/bin/python3
import sys
import json
import pprint

def get_hosts():
   #myhosts = ["10.0.0.10", "10.0.0.11"]
   myhosts = ["vm-ejcbfdagih-2.eastus2.cloudapp.azure.com", "vm-ifheabjdcg-1.centralus.cloudapp.azure.com"]
   hosts=[]
   
   for ip_address in myhosts:
      hosts.append(ip_address)
   
   return hosts


def main():
   db_group=get_hosts()
   all_groups= { 'db': db_group,
               }
   print(json.dumps(all_groups))

if __name__=="__main__":
   main()
