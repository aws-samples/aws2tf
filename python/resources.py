def resource_types(type):
    if type == "net":
        net=["aws_vpc","aws_subnet","aws_security_group","aws_internet_gateway","aws_nat_gateway","aws_route_table"]
        return net
    else:
        same=[type]
        return same


# problematic: "aws_network_acl"
# Error: use the `aws_default_network_acl` resource instead

