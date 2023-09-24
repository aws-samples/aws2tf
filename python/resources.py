def resource_types():
    resource_types=["aws_vpc","aws_subnet","aws_security_group","aws_internet_gateway","aws_nat_gateway","aws_route_table"]
    return resource_types


# problematic: "aws_network_acl"
# Error: use the `aws_default_network_acl` resource instead

