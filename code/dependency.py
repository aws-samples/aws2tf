"""Dependency tracking for aws2tf resource imports."""

import inspect
import context
import logging
from error_handler import handle_error

log = logging.getLogger('aws2tf')


def special_deps(ttft, taddr):
   """
   if ttft == "aws_security_group": 
      print("##### special dep security group") 
      #add_known_dependancy("aws_security_group_rule",taddr) 
      #add_dependancy("aws_security_group_rule",taddr)
   if ttft == "aws_subnet":
      print("##### special dep subnet") 
      #add_known_dependancy("aws_route_table_association",taddr) 
      #add_dependancy("aws_route_table_association",taddr)  
   elif ttft == "aws_vpc": 
      print("##### special dep vpc") 
      #add_known_dependancy("aws_route_table_association",taddr)  
      #add_known_dependancy("aws_subnet",taddr)  
      #add_dependancy("aws_route_table_association",taddr)
      #add_dependancy("aws_vpc_ipv4_cidr_block_association",taddr)
      #add_dependancy("aws_vpc_endpoint", taddr)
   
   if ttft == "aws_vpclattice_service_network":
      print("##### special lattice sn") 
      add_known_dependancy("aws_vpclattice_service",taddr) 
      add_known_dependancy("aws_vpclattice_service_network_vpc_association",taddr) 
      add_known_dependancy("aws_vpclattice_service_network_service_association",taddr)
   """
   return  


def add_known_dependancy(type, id):
    # check if we alredy have it
    pkey=type+"."+id
    if pkey not in context.rdep:
        if context.debug: log.debug("add_known_dependancy: " + pkey)
        context.rdep[pkey]=False
    return


def add_dependancy(type, id):
    # check if we alredy have it
   if id is None: 
      log.warning("WARNING: add_dependancy: id is None")
      return
   try:
   #   if type=="aws_kms_alias" and id=="k-817bb810-7154-4d9b-b582-7dbb62e77876":
   #      raise Exception("aws_kms_alias")
      if type=="aws_glue_catalog_database":
         if ":" not in id: id=context.acc+":"+id
      pkey=type+"."+id
      if pkey not in context.rproc:
         if context.debug: log.debug("add_dependancy: " + pkey)
         context.rproc[pkey]=False
   except Exception as e:
      handle_error(e, str(inspect.currentframe().f_code.co_name), type, id)
   return
