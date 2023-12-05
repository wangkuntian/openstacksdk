# Copyright (c) 2023 UnionTech
# All rights reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from openstack import resource


class RGPortForwarding(resource.Resource):
    name_attribute = "router_gateway_port_forwarding"
    resource_name = "router gateway port forwarding"
    resource_key = 'gateway_port_forwarding'
    resources_key = 'gateway_port_forwardings'
    base_path = '/routers/%(router_id)s/gateway_port_forwardings'

    allow_create = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource.QueryParameters(
        'internal_port_id', 'external_port', 'protocol'
    )

    # Properties
    #: The ID of Router
    router_id = resource.URI('router_id')
    #: The ID of internal port
    internal_port_id = resource.Body('internal_port_id')
    #: The internal IP address
    internal_ip_address = resource.Body('internal_ip_address')
    #: The router gateway IP address
    gw_ip_address = resource.Body('gw_ip_address')
    #: The internal TCP/UDP/other port number
    internal_port = resource.Body('internal_port', type=int)
    #: The external TCP/UDP/other port number
    external_port = resource.Body('external_port', type=int)
    #: The protocol
    protocol = resource.Body('protocol')
