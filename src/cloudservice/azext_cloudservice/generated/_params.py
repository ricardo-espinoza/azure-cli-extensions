# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_three_state_flag,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group,
    validate_file_or_dict
)


def load_arguments(self, _):

    # All "cloud_service_name" miss help
    with self.argument_context('cloud-service role-instance list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Cloud service name.')

    with self.argument_context('cloud-service role-instance show') as c:
        c.argument('role_instance_name', type=str, help='Name of the role instance.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Cloud service name.', id_part='name')

    with self.argument_context('cloud-service role-instance delete') as c:
        c.argument('role_instance_name', type=str, help='Name of the role instance.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Cloud service name.', id_part='name')

    with self.argument_context('cloud-service role-instance rebuild') as c:
        c.argument('role_instance_name', type=str, help='Name of the role instance.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Cloud service name.', id_part='name')

    with self.argument_context('cloud-service role-instance reimage') as c:
        c.argument('role_instance_name', type=str, help='Name of the role instance.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Cloud service name.', id_part='name')

    with self.argument_context('cloud-service role-instance restart') as c:
        c.argument('role_instance_name', type=str, help='Name of the role instance.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Cloud service name.', id_part='name')

    with self.argument_context('cloud-service role-instance show-instance-view') as c:
        c.argument('role_instance_name', type=str, help='Name of the role instance.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Cloud service name.', id_part='name')

    with self.argument_context('cloud-service role-instance show-remote-desktop-file') as c:
        c.argument('role_instance_name', type=str, help='Name of the role instance.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Cloud service name.', id_part='name')

    with self.argument_context('cloud-service role-instance wait') as c:
        c.argument('role_instance_name', type=str, help='Name of the role instance.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Cloud service name.', id_part='name')

    with self.argument_context('cloud-service role list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Cloud service name.')

    with self.argument_context('cloud-service role show') as c:
        c.argument('role_name', type=str, help='Name of the role.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Cloud service name.', id_part='name')

    with self.argument_context('cloud-service list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('cloud-service show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', options_list=['--name', '-n', '--cloud-service-name'], type=str, help='Name '
                   'of the cloud service.', id_part='name')

    with self.argument_context('cloud-service create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', options_list=['--name', '-n', '--cloud-service-name'], type=str, help='Name '
                   'of the cloud service.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('package_url', type=str, help='Specifies a URL that refers to the location of the service package '
                   'in the Blob service. The service package URL can be Shared Access Signature (SAS) URI from any '
                   'storage account. This is a write-only property and is not returned in GET calls.')
        c.argument('configuration', type=str, help='Specifies the XML service configuration (.cscfg) for the cloud '
                   'service.')
        c.argument('configuration_url', type=str, help='Specifies a URL that refers to the location of the service '
                   'configuration in the Blob service. The service package URL  can be Shared Access Signature (SAS) '
                   'URI from any storage account. This is a write-only property and is not returned in GET calls.')
        c.argument('start_cloud_service', arg_type=get_three_state_flag(), help='(Optional) Indicates whether to start '
                   'the cloud service immediately after it is created. The default value is `true`. If false, the '
                   'service model is still deployed, but the code is not run immediately. Instead, the service is '
                   'PoweredOff until you call Start, at which time the service will be started. A deployed service '
                   'still incurs charges, even if it is poweredoff.')
        c.argument('upgrade_mode', arg_type=get_enum_type(['Auto', 'Manual', 'Simultaneous']), help='Update mode for '
                   'the cloud service. Role instances are allocated to update domains when the service is deployed. '
                   'Updates can be initiated manually in each update domain or initiated automatically in all update '
                   'domains. Possible Values are <br /><br />**Auto**<br /><br />**Manual** <br /><br '
                   '/>**Simultaneous**<br /><br /> If not specified, the default value is Auto. If set to Manual, PUT '
                   'UpdateDomain must be called to apply the update. If set to Auto, the update is automatically '
                   'applied to each update domain in sequence.')
        c.argument('extensions', type=validate_file_or_dict, help='List of extensions for the cloud service. Expected '
                   'value: json-string/@json-file.', arg_group='Extension Profile')
        c.argument('load_balancer_configurations', type=validate_file_or_dict, help='The list of load balancer '
                   'configurations for the cloud service. Expected value: json-string/@json-file.', arg_group='Network '
                   'Profile')
        c.argument('id_', options_list=['--id'], type=str, help='Resource Id', arg_group='Network Profile Swappable '
                   'Cloud Service')
        c.argument('secrets', type=validate_file_or_dict, help='Specifies set of certificates that should be installed '
                   'onto the role instances. Expected value: json-string/@json-file.', arg_group='Os Profile')
        c.argument('roles', type=validate_file_or_dict, help='List of roles for the cloud service. Expected value: '
                   'json-string/@json-file.', arg_group='Role Profile')

    with self.argument_context('cloud-service update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', options_list=['--name', '-n', '--cloud-service-name'], type=str, help='Name '
                   'of the cloud service.', id_part='name')
        c.argument('tags', tags_type)

    with self.argument_context('cloud-service delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', options_list=['--name', '-n', '--cloud-service-name'], type=str, help='Name '
                   'of the cloud service.', id_part='name')

    with self.argument_context('cloud-service delete-instance') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', options_list=['--name', '-n', '--cloud-service-name'], type=str, help='Name '
                   'of the cloud service.', id_part='name')
        c.argument('role_instances', nargs='+', help='List of cloud service role instance names. Value of \'*\' will '
                   'signify all role instances of the cloud service.')

    with self.argument_context('cloud-service power-off') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', options_list=['--name', '-n', '--cloud-service-name'], type=str, help='Name '
                   'of the cloud service.', id_part='name')

    with self.argument_context('cloud-service rebuild') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', options_list=['--name', '-n', '--cloud-service-name'], type=str, help='Name '
                   'of the cloud service.', id_part='name')
        c.argument('role_instances', nargs='+', help='List of cloud service role instance names. Value of \'*\' will '
                   'signify all role instances of the cloud service.')

    with self.argument_context('cloud-service reimage') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', options_list=['--name', '-n', '--cloud-service-name'], type=str, help='Name '
                   'of the cloud service.', id_part='name')
        c.argument('role_instances', nargs='+', help='List of cloud service role instance names. Value of \'*\' will '
                   'signify all role instances of the cloud service.')

    with self.argument_context('cloud-service restart') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', options_list=['--name', '-n', '--cloud-service-name'], type=str, help='Name '
                   'of the cloud service.', id_part='name')
        c.argument('role_instances', nargs='+', help='List of cloud service role instance names. Value of \'*\' will '
                   'signify all role instances of the cloud service.')

    with self.argument_context('cloud-service show-instance-view') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', options_list=['--name', '-n', '--cloud-service-name'], type=str, help='Name '
                   'of the cloud service.', id_part='name')

    with self.argument_context('cloud-service start') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', options_list=['--name', '-n', '--cloud-service-name'], type=str, help='Name '
                   'of the cloud service.', id_part='name')

    with self.argument_context('cloud-service wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', options_list=['--name', '-n', '--cloud-service-name'], type=str, help='Name '
                   'of the cloud service.', id_part='name')

    with self.argument_context('cloud-service update-domain list-update-domain') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Name of the cloud service.')

    with self.argument_context('cloud-service update-domain show-update-domain') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Name of the cloud service.', id_part='name')
        c.argument('update_domain', type=int, help='Specifies an integer value that identifies the update domain. '
                   'Update domains are identified with a zero-based index: the first update domain has an ID of 0, the '
                   'second has an ID of 1, and so on.', id_part='child_name_1')

    with self.argument_context('cloud-service update-domain walk-update-domain') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cloud_service_name', type=str, help='Name of the cloud service.', id_part='name')
        c.argument('update_domain', type=int, help='Specifies an integer value that identifies the update domain. '
                   'Update domains are identified with a zero-based index: the first update domain has an ID of 0, the '
                   'second has an ID of 1, and so on.', id_part='child_name_1')