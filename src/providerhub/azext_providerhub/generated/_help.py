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

from knack.help_files import helps

helps['providerhub'] = """
    type: group
    short-summary: Manage resources with ProviderHub
"""

helps['providerhub custom-rollout'] = """
    type: group
    short-summary: Manage custom rollout with providerhub
"""

helps['providerhub custom-rollout list'] = """
    type: command
    short-summary: "Gets the list of the custom rollouts for the given provider."
    examples:
      - name: CustomRollouts_ListByProviderRegistration
        text: |-
               az providerhub custom-rollout list --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub custom-rollout show'] = """
    type: command
    short-summary: "Gets the custom rollout details."
    examples:
      - name: CustomRollouts_Get
        text: |-
               az providerhub custom-rollout show --provider-namespace "Microsoft.Contoso" --rollout-name \
"canaryTesting99"
"""

helps['providerhub custom-rollout create'] = """
    type: command
    short-summary: "Create the rollout details."
    parameters:
      - name: --canary
        long-summary: |
            Usage: --canary regions=XX

            Multiple actions can be specified by using more than one regions=XX argument.
    examples:
      - name: CustomRollouts_CreateOrUpdate
        text: |-
               az providerhub custom-rollout create --canary regions="eastus2euap" regions="centraluseuap" --provider-namespace \
"Microsoft.Contoso" --rollout-name "eastus2euapShoeBoxTesting"
"""

helps['providerhub default-rollout'] = """
    type: group
    short-summary: Manage default rollout with providerhub
"""

helps['providerhub default-rollout list'] = """
    type: command
    short-summary: "Gets the list of the rollouts for the given provider."
    examples:
      - name: DefaultRollouts_ListByProviderRegistration
        text: |-
               az providerhub default-rollout list --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub default-rollout show'] = """
    type: command
    short-summary: "Gets the default rollout details."
    examples:
      - name: DefaultRollouts_Get
        text: |-
               az providerhub default-rollout show --provider-namespace "Microsoft.Contoso" --rollout-name \
"2021week20"
"""

helps['providerhub default-rollout create'] = """
    type: command
    short-summary: "Create the rollout details."
    parameters:
      - name: --canary
        long-summary: |
            Usage: --canary skip-regions=XX

            skip-regions: Required. The canary skip regions.

      - name: --rest-of-the-world-group-two --row2
        long-summary: |
            Usage: --rest-of-the-world-group-two wait-duration=XX

            wait-duration: Required. The rest of the world group two wait duration.

    examples:
      - name: DefaultRollouts_CreateOrUpdate
        text: |-
               az providerhub default-rollout create \
                --provider-namespace "Microsoft.Contoso" --rollout-name "2021week20" \
                --canary skip-regions="eastus2euap" \
                --rest-of-the-world-group-two wait-duration="PT2H"
"""

helps['providerhub default-rollout delete'] = """
    type: command
    short-summary: "Deletes the rollout resource. Rollout must be in terminal state."
    examples:
      - name: DefaultRollouts_Delete
        text: |-
               az providerhub default-rollout delete --provider-namespace "Microsoft.Contoso" --rollout-name \
"2021week20"
"""

helps['providerhub default-rollout stop'] = """
    type: command
    short-summary: "Stops or cancels the rollout, if in progress."
    examples:
      - name: DefaultRollouts_Stop
        text: |-
               az providerhub default-rollout stop --provider-namespace "Microsoft.Contoso" --rollout-name \
"2021week20"
"""

helps['providerhub manifest'] = """
    type: group
    short-summary: Manage with providerhub manifest operations
"""

helps['providerhub manifest checkin'] = """
    type: command
    short-summary: "Checkin the manifest."
    parameters:
      - name: --arm-manifest-location --baseline-arm-manifest-location --location
        long-summary: |
            Usage: --location "EastUS2EUAP"

    examples:
      - name: CheckinManifest
        text: |-
               az providerhub manifest checkin --location "EastUS2EUAP" --environment "Prod" \
--provider-namespace "Microsoft.Contoso"
"""

helps['providerhub manifest generate'] = """
    type: command
    short-summary: "Generates the manifest for the given provider."
    examples:
      - name: GenerateManifest
        text: |-
               az providerhub manifest generate --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub notification-registration'] = """
    type: group
    short-summary: Manage notification registration with providerhub
"""

helps['providerhub notification-registration list'] = """
    type: command
    short-summary: "Gets the list of the notification registrations for the given provider."
    examples:
      - name: NotificationRegistrations_ListByProviderRegistration
        text: |-
               az providerhub notification-registration list --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub notification-registration show'] = """
    type: command
    short-summary: "Gets the notification registration details."
    examples:
      - name: NotificationRegistrations_Get
        text: |-
               az providerhub notification-registration show --name "testNotificationRegistration" --provider-namespace \
"Microsoft.Contoso"
"""

helps['providerhub notification-registration create'] = """
    type: command
    short-summary: "Create a notification registration."
    parameters:
      - name: --notification-endpoints
        long-summary: |
            Usage: --notification-endpoints notification-destination=XX locations=XX


            Multiple actions can be specified by using more than one --notification-endpoints argument.
    examples:
      - name: NotificationRegistrations_CreateOrUpdate
        text: |-
               az providerhub notification-registration create --name "testNotificationRegistration" --included-events \
"*/write" "Microsoft.Contoso/employees/delete" --message-scope "RegisteredSubscriptions" --notification-endpoints \
locations="" locations="East US" notification-destination="/subscriptions/00000000-0000-0000-0000-000000000000/resource\
Groups/mgmtexp-eastus/providers/Microsoft.EventHub/namespaces/unitedstates-mgmtexpint/eventhubs/armlinkednotifications"\
 --notification-endpoints locations="North Europe" notification-destination="/subscriptions/00000000-0000-0000-0000-000000000000\
   /resourceGroups/mgmtexp-northeurope/providers/Microsoft.EventHub/namespaces/europe-mgmtexpint/eventhubs/armlin\
kednotifications" --notification-mode "EventHub" --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub notification-registration delete'] = """
    type: command
    short-summary: "Deletes a notification registration."
    examples:
      - name: NotificationRegistrations_Delete
        text: |-
               az providerhub notification-registration delete --name "testNotificationRegistration" \
--provider-namespace "Microsoft.Contoso"
"""

helps['providerhub operation'] = """
    type: group
    short-summary: Manage operation with providerhub
"""

helps['providerhub operation list'] = """
    type: command
    short-summary: "Gets the operations supported by the given provider."
    examples:
      - name: Operations_ListByProviderRegistration
        text: |-
               az providerhub operation list --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub operation create'] = """
    type: command
    short-summary: "Create the operation supported by the given provider."
    examples:
      - name: Operations_CreateOrUpdate
        text: |-
               az providerhub operation create --contents "[{\\"name\\":\\"Microsoft.Contoso/Employees/Read\\",\\"displ\
ay\\":{\\"description\\":\\"Read employees\\",\\"operation\\":\\"Gets/List employee resources\\",\\"provider\\":\\"Micr\
osoft.Contoso\\",\\"resource\\":\\"Employees\\"}}]" --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub operation delete'] = """
    type: command
    short-summary: "Deletes an operation."
    examples:
      - name: Operations_Delete
        text: |-
               az providerhub operation delete --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub provider-registration'] = """
    type: group
    short-summary: Manage provider registration with providerhub
"""

helps['providerhub provider-registration list'] = """
    type: command
    short-summary: "Gets the list of the provider registrations in the subscription."
    examples:
      - name: ProviderRegistrations_List
        text: |-
               az providerhub provider-registration list
"""

helps['providerhub provider-registration show'] = """
    type: command
    short-summary: "Gets the provider registration details."
    examples:
      - name: ProviderRegistrations_Get
        text: |-
               az providerhub provider-registration show --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub provider-registration create'] = """
    type: command
    short-summary: "Create the provider registration."
    parameters:
      - name: --provider-authentication --provider-authn
        short-summary: 'Used to set alternative audiences or resources that ARM should accept from the token while authenticating requests for the provider.'
        long-summary: |
            Usage: --provider-authentication allowed-audiences=XX

            allowed-audiences: Required. The allowed audiences.

      - name: --provider-authorizations --provider-authz
        short-summary: 'The resource provider authorizations.'
        long-summary: |
            Usage: --provider-authorizations application-id=XX role-definition-id=XX managed-by-role-definition-id=XX

            application-id: Required. The application ID.
            role-definition-id: Required. The role definition ID.
            managed-by-role-definition-id: Required. The managed by role definition ID.

            Multiple actions can be specified by using more than one --provider-authorizations argument.
      - name: --provider-version
        type: string
        short-summary: 'The provider version.'
        long-summary: |
            Usage: --provider-version "2.0"

      - name: --provider-type
        type: string
        short-summary: 'The provider type.'
        long-summary: |
            Usage: --provider-type "Internal"

            Available provider types include: Internal, External, Hidden, RegistrationFree, LegacyRegistrationRequired, TenantOnly, AuthorizationFree

      - name: --namespace
        type: string
        short-summary: 'The name of the resource provider hosted within ProviderHub.'
        long-summary: |
            Usage: --namespace "Microsoft.Contoso"

      - name: --capabilities
        short-summary: 'The resource provider capabilities.'
        long-summary: |
            Usage: --capabilities quota-id=XX effect=XX required-features=XX


            Multiple actions can be specified by using more than one --capabilities argument.
      - name: --template-deployment-options --tmplt-deploy-opt
        short-summary: 'The template deployment options.'
        long-summary: |
            Usage: --template-deployment-options preflight-supported=XX preflight-options=XX

      - name: --schema-owners
        short-summary: 'Specifies an array of needed ACIS claims to modify the resource provider schema via ACIS.'
        long-summary: |
            Usage: --schema-owners "Contoso schema owners"

             Multiple actions can be specified by using more than one --schema-owners argument.
      - name: --manifest-owners
        short-summary: "Specifies an array of required ACIS claims to modify the resource provider's manifest content via ACIS."
        long-summary: |
            Usage: --manifest-owners "SPARTA-PlatformServiceAdministrator"

             Multiple actions can be specified by using more than one --manifest-owners argument.
      - name: --incident-routing-service --incident-service
        type: string
        short-summary: 'The service in IcM when creating or transferring incidents to the RP.'
        long-summary: |
            Usage: --incident-routing-service "Contoso Resource Provider"

      - name: --incident-routing-team --incident-team
        type: string
        short-summary: 'The team in IcM when creating or transferring incidents to the RP.'
        long-summary: |
            Usage: --incident-routing-team "Contoso Triage"

      - name: --incident-contact-email
        type: string
        short-summary: 'The email address of contacts for incidents related to the RP.'
        long-summary: |
            Usage: --incident-contact-email "helpme@contoso.com"

      - name: --service-tree-infos
        short-summary: 'The ServiceTree information for the resource provider.'
        long-summary: |
            Usage: --service-tree-infos service-id=XX component-id=XX

            service-id: Required. The service ID.
            component-id: Required. The component ID.


            Multiple actions can be specified by using more than one --service-tree-infos argument.
      - name: --override-actions --subscription-state-override-actions
        short-summary: 'The subscription state override actions.'
        long-summary: |
            Usage: --subscription-state-override-actions state=XX action=XX


            Multiple actions can be specified by using more than one --subscription-state-override-actions argument.
      - name: --metadata-authz --providerhub-metadata-authorizations
        short-summary: 'The ProviderHub metadata authorizations.'
        long-summary: |
            Usage: --providerhub-metadata-authorizations application-id=XX role-definition-id=XX \
managed-by-role-definition-id=XX

            application-id: Required. The application ID.
            role-definition-id: Required. The role definition ID.
            managed-by-role-definition-id: Required. The managed by role definition ID.

            Multiple actions can be specified by using more than one --providerhub-metadata-authorizations \
argument.
      - name: --metadata-authn --providerhub-metadata-authentication
        short-summary: 'The ProviderHub metadata authentication.'
        long-summary: |
            Usage: --providerhub-metadata-authentication allowed-audiences=XX

            allowed-audiences: Required. The allowed audiences.

      - name: --resource-access-policy
        type: string
        short-summary: 'The resource access policy.'
        long-summary: |
            Usage: --resource-access-policy "AcisReadAllowed, AcisActionAllowed"

      - name: --opt-in-headers
        type: string
        short-summary: 'The opt-in headers.'
        long-summary: |
            Usage: --opt-in-headers "SignedUserToken"

      - name: --lighthouse-auth --lighthouse-authorizations
        short-summary: 'The lighthouse authorizations.'
        long-summary: |
            Usage: --lighthouse-authorizations principal-id=XX role-definition-id=XX

            principal-id: Required. The principal ID.
            role-definition-id: Required. The role definition ID.

      - name: --managed-by-tenant-id
        type: string
        short-summary: 'The managed by tenant ID.'
        long-summary: |
            Usage: --managed-by-tenant-id "00000000-0000-0000-0000-000000000000"
    examples:
      - name: ProviderRegistrations_CreateOrUpdate
        text: |-
               az providerhub provider-registration create \
    --providerhub-metadata-authorizations application-id="00000000-0000-0000-0000-000000000000" \
    role-definition-id="00000000-0000-0000-0000-000000000000" \
    --providerhub-metadata-authentication allowed-audiences="https://management.core.windows.net/" \
    --service-tree-infos service-id="00000000-0000-0000-0000-000000000000" \
    component-id="00000000-0000-0000-0000-000000000000" \
    --capabilities effect="Allow" quota-id="CSP_2015-05-01" \
    --capabilities effect="Allow" quota-id="CSP_MG_2017-12-01" \
    --manifest-owners "SPARTA-PlatformServiceAdministrator" \
    --incident-contact-email "helpme@contoso.com" \
    --incident-routing-service "Contoso Resource Provider" \
    --incident-routing-team "Contoso Triage" \
    --provider-type "Internal" \
    --provider-version "2.0" \
    --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub provider-registration delete'] = """
    type: command
    short-summary: "Deletes a provider registration."
    examples:
      - name: ProviderRegistrations_Delete
        text: |-
               az providerhub provider-registration delete --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub provider-registration generate-operation'] = """
    type: command
    short-summary: "Generates the operations api for the given provider."
    examples:
      - name: ProviderRegistrations_GenerateOperations
        text: |-
               az providerhub provider-registration generate-operation --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub resource-type-registration'] = """
    type: group
    short-summary: Manage resource type registration with providerhub
"""

helps['providerhub resource-type-registration list'] = """
    type: command
    short-summary: "Gets the list of the resource types for the given provider."
    examples:
      - name: ResourceTypeRegistrations_ListByProviderRegistration
        text: |-
               az providerhub resource-type-registration list --provider-namespace "Microsoft.Contoso"
"""

helps['providerhub resource-type-registration show'] = """
    type: command
    short-summary: "Gets a resource type details in the given subscription and provider."
    examples:
      - name: ResourceTypeRegistrations_Get
        text: |-
               az providerhub resource-type-registration show --provider-namespace "Microsoft.Contoso" --resource-type \
"employees"
"""

helps['providerhub resource-type-registration create'] = """
    type: command
    short-summary: "Create a resource type."
    parameters:
      - name: --swagger-specifications
        short-summary: 'The Swagger spec of the resource type.'
        long-summary: |
            Usage: --swagger-specifications api-versions=XX swagger-spec-folder-uri=XX

            api-versions: Required. The resource type API versions, separated by commas.
            swagger-spec-folder-uri: Required. The Swagger spec URI.

            Multiple actions can be specified by using more than one --swagger-specifications argument.
      - name: --routing-type
        type: string
        short-summary: 'The resource routing type.​'
        long-summary: |
            Usage: --routing-type "Default"

            Available routing types include: Default, ProxyOnly, HostBased, Extension, Tenant, Fanout, LocationBased, Failover, CascadeExtension, ChildFanout, CascadeAuthorizedExtension, BypassEndpointSelectionOptimization

      - name: --regionality
        type: string
        short-summary: 'The regionality of the resource type.'
        long-summary: |
            Usage: --regionality "Regional"
      - name: --endpoints
        type: string
        short-summary: 'The resource type endpoints.'
        long-summary: |
            Usage: --endpoints api-versions=XX locations=XX required-features=XX
            api-versions: Required. Comma separated list of API versions.
            locations: Required. Comma separated list of locations.
            required-features: Required. List of required features. Multiple required-features can be specified.
            Multiple actions can be specified by using more than one --endpoints argument.
      - name: --creation-begin --resource-creation-begin
        short-summary: 'Extension options for handling the resource creation begin extension request.'
        long-summary: |
            Usage: --creation-begin request=XX response=XX
            request: The list of extension option types.
            response: The list of extension option types.
      - name: --patch-begin --resource-patch-begin
        short-summary: 'Extension options for handling the resource patch begin extension request.'
        long-summary: |
            Usage: --patch-begin request=XX response=XX
            request: The list of extension option types.
            response: The list of extension option types.
      - name: --marketplace-type
        type: string
        short-summary: 'The type of marketplace behavior for the resource type.'
        long-summary: |
            Usage: --marketplace-type "AddOn"
      - name: --allowed-unauthorized-actions --aua
        type: string
        short-summary: 'The allowed unauthorized actions'
        long-summary: |
            Usage: --allowed-unauthorized-actions "Microsoft.Contoso/rpResourceType/read, Microsoft.Contoso/rpResourceType/delete"
      - name: --auth-mappings --authorization-action-mappings
        short-summary: 'Allows RP to override action verb for RBAC purposes at ARM.'
        long-summary: |
            Usage: --auth-mappings original=XX desired=XX

            original: Required. The original action name.
            desired: Required. The desired action name.

            Multiple actions can be specified by using more than one --auth-mappings argument.
      - name: --linked-access-checks
        short-summary: 'Enables additional Role Based Access Control (RBAC) checks on related resources.'
        long-summary: |
            Usage: --linked-access-checks action-name=XX linked-property=XX linked-action=XX linked-action-verb=XX \
linked-type=XX

            action-name: The action name.
            linked-property: The linked property.
            linked-action: The linked action.
            linked-action-verb: The linked action verb.
            linked-type: The linked type.

            Multiple actions can be specified by using more than one --linked-access-checks argument.
      - name: --default-api-version
        type: string
        short-summary: 'The default API version for the endpoint.'
        long-summary: |
            Usage: --default-api-version "2021-01-01"

      - name: --logging-rules
        type: string
        short-summary: 'The logging rules'
        long-summary: |
            Usage: --logging-rules action=XX direction=XX detail-level=XX

            action: Required. The action name.
            direction: Required. The direction.
            detail-level: Required. The detail level.

            Multiple actions can be specified by using more than one --logging-rules argument.
      - name: --throttling-rules
        type: string
        short-summary: 'Enables setting individual limits for different actions in terms of number of requests or number of resources (for collection read requests only).'
        long-summary: |
            Usage: --throttling-rules action=XX metrics=XX required-features=XX

            action: Required. The action name.
            metrics: Required. The throttling metrics.
            required-features: The throttling rule required features.

            Multiple actions can be specified by using more than one --throttling-rules argument.
      - name: --required-features
        type: string
        short-summary: 'The required features.'
        long-summary: |
            Usage: --required-features "Microsoft.Contoso/feature1, Microsoft.Contoso/feature2"

      - name: --req-features-policy --required-features-policy
        short-summary: 'The accepted values are "Any" or "All". If the value is "All", then only the subscriptions registered to all the corresponding feature flag will be allowed.​'
        long-summary: |
            Usage: --req-features-policy "All"

      - name: --enable-async-operation
        type: string
        short-summary: 'Indicates whether the async operation is enabled for this resource type.'
        long-summary: |
            Usage: --enable-async-operation "false"

      - name: --enable-third-party-s2s
        type: string
        short-summary: 'Indicates whether third party s2s is enabled for this resource type.'
        long-summary: |
            Usage: --enable-third-party-s2s "false"

      - name: --is-pure-proxy
        type: string
        short-summary: 'Indicates whether this is a PureProxy resource type.'
        long-summary: |
            Usage: --is-pure-proxy "false"

      - name: --identity-management
        type: string
        short-summary: 'MSI related settings.'
        long-summary: |
            Usage: --identity-management type=XX application-id=XX

            type: The type of the identity management.
            application-id: The application ID that handles the identity.

      - name: --check-name-availability-specifications --checkname-specs
        short-summary: 'Name availability checks feature at the platform level.'
        long-summary: |
            Usage: --check-name-availability-specifications enable-default-validation=XX \
resource-types-with-custom-validation=XX

            enable-default-validation: Boolean indicating whether RP has chosen to opt-out of RPaaS to perform check name.
            resource-types-with-custom-validation: The types which needs additional validation from the RP.

      - name: --dav --disallowed-action-verbs
        type: string
        short-summary: 'The disallowed action verbs.'
        long-summary: |
            Usage: --dav "read"

      - name: --service-tree-infos
        short-summary: 'The ServiceTree information for the resource provider.'
        long-summary: |
            Usage: --service-tree-infos service-id=XX component-id=XX

            service-id: Required. The service ID.
            component-id: Required. The component ID.

            Multiple actions can be specified by using more than one --service-tree-infos argument.
      - name: --opt-in-headers
        type: string
        short-summary: 'The opt-in headers.'
        long-summary: |
            Usage: --opt-in-headers "SignedUserToken"

      - name: --sub-state-rules --subscription-state-rules
        short-summary: 'The subscription state rules.'
        long-summary: |
            Usage: --sub-state-rules state=XX allowed-actions=XX

            state: The subscription state.
            allowed-actions: The allowed actions.

            Multiple actions can be specified by using more than one --sub-state-rules argument.
      - name: --template-deployment-options --tmplt-deploy-opt
        short-summary: 'The template deployment options.'
        long-summary: |
            Usage: --template-deployment-options preflight-supported=XX preflight-options=XX

            preflight-supported: Boolean indicating whether preflight validation is supported.
            preflight-options: The preflight options.

      - name: --extended-locations
        short-summary: 'The extended location options'
        long-summary: |
            Usage: --extended-locations type=XX supported-policy=XX

            type: The extended location type.
            supported-policy: The supported policy.

            Multiple actions can be specified by using more than one --extended-locations argument.
      - name: --resource-move-policy
        short-summary: 'The resource move policy.'
        long-summary: |
            Usage: --resource-move-policy validation-required=XX cross-resource-group-move-enabled=XX \
cross-subscription-move-enabled=XX

            validation-required: Boolean indicating whether validation is required for moving the resource.
            cross-resource-group-move-enabled: Boolean indicating whether moving resources across resource groups is allowed.
            cross-subscription-move-enabled: Boolean indicating whether moving resources across subscriptions is allowed.

      - name: --deletion-policy --resource-deletion-policy
        type: string
        short-summary: 'The resource deletion policy.'
        long-summary: |
            Usage: --deletion-policy "CascadeDeleteAll"

      - name: --override-actions --subscription-state-override-actions
        short-summary: 'The subscription state override actions.'
        long-summary: |
            Usage: --subscription-state-override-actions state=XX action=XX


            Multiple actions can be specified by using more than one --subscription-state-override-actions argument.

    examples:
      - name: ResourceTypeRegistrations_CreateOrUpdate
        text: |-
               az providerhub resource-type-registration create \
    --endpoints api-versions="2019-01-01" locations="Global" \
    required-features="Microsoft.Contoso/RPaaSSampleApp" \
    extension-endpoint-uri="https://contoso-test-extension-endpoint.com/" \
    extension-categories="ResourceReadValidate" extension-categories="ResourceDeletionValidate" \
    --regionality "Global" \
    --routing-type "ProxyOnly" \
    --swagger-specifications api-versions="2019-01-01" \
    swagger-spec-folder-uri="https://github.com/pathtoresourceproviderswaggerspecfolder" \
    --provider-namespace "Microsoft.Contoso" \
    --enable-async-operation false \
    --template-deployment-options preflight-supported="true" \
    preflight-options="DefaultValidationOnly" preflight-options="continueDeploymentOnFailure" \
    --resource-type "testResourceType"
"""

helps['providerhub resource-type-registration delete'] = """
    type: command
    short-summary: "Deletes a resource type."
    examples:
      - name: ResourceTypeRegistrations_Delete
        text: |-
               az providerhub resource-type-registration delete --provider-namespace "Microsoft.Contoso" \
--resource-type "testResourceType"
"""

helps['providerhub sku'] = """
    type: group
    short-summary: Manage sku with providerhub
"""

helps['providerhub sku list'] = """
    type: command
    short-summary: "Gets the list of skus for the given resource type. And Gets the list of skus for the given \
resource type. And Gets the list of skus for the given resource type. And Gets the list of skus for the given resource \
type."
    examples:
      - name: Skus_ListByResourceTypeRegistrationsNestedResourceTypeThird
        text: |-
               az providerhub sku list --nested-resource-type-first "nestedResourceTypeFirst" \
--nested-resource-type-second "nestedResourceTypeSecond" --nested-resource-type-third "nestedResourceTypeThird" \
--provider-namespace "Microsoft.Contoso" --resource-type "testResourceType"
      - name: Skus_ListByResourceTypeRegistrationsNestedResourceTypeSecond
        text: |-
               az providerhub sku list --nested-resource-type-first "nestedResourceTypeFirst" \
--nested-resource-type-second "nestedResourceTypeSecond" --provider-namespace "Microsoft.Contoso" --resource-type \
"testResourceType"
      - name: Skus_ListByResourceTypeRegistrationsNestedResourceTypeFirst
        text: |-
               az providerhub sku list --nested-resource-type-first "nestedResourceTypeFirst" --provider-namespace \
"Microsoft.Contoso" --resource-type "testResourceType"
      - name: Skus_ListByResourceTypeRegistrations
        text: |-
               az providerhub sku list --provider-namespace "Microsoft.Contoso" --resource-type "testResourceType"
"""

helps['providerhub sku show'] = """
    type: command
    short-summary: "Gets the sku details for the given resource type and sku name."
    examples:
      - name: Skus_Get
        text: |-
               az providerhub sku show --provider-namespace "Microsoft.Contoso" --resource-type "testResourceType" \
--sku "testSku"
"""

helps['providerhub sku create'] = """
    type: command
    short-summary: "Creates or updates the resource type skus in the given resource type. And Creates or updates the \
resource type skus in the given resource type. And Creates or updates the resource type skus in the given resource \
type. And Create the resource type skus in the given resource type."
    examples:
      - name: Skus_CreateOrUpdateNestedResourceTypeThird
        text: |-
               az providerhub sku create --nested-resource-type-first "nestedResourceTypeFirst" \
--nested-resource-type-second "nestedResourceTypeSecond" --nested-resource-type-third "nestedResourceTypeThird" \
--sku-settings "[{\\"name\\":\\"freeSku\\",\\"kind\\":\\"Standard\\",\\"tier\\":\\"Tier1\\"},{\\"name\\":\\"premiumSku\
\\",\\"costs\\":[{\\"meterId\\":\\"xxx\\"}],\\"kind\\":\\"Premium\\",\\"tier\\":\\"Tier2\\"}]" --provider-namespace \
"Microsoft.Contoso" --resource-type "testResourceType" --sku "testSku"
      - name: Skus_CreateOrUpdateNestedResourceTypeSecond
        text: |-
               az providerhub sku create --nested-resource-type-first "nestedResourceTypeFirst" \
--nested-resource-type-second "nestedResourceTypeSecond" --sku-settings "[{\\"name\\":\\"freeSku\\",\\"kind\\":\\"Stand\
ard\\",\\"tier\\":\\"Tier1\\"},{\\"name\\":\\"premiumSku\\",\\"costs\\":[{\\"meterId\\":\\"xxx\\"}],\\"kind\\":\\"Premi\
um\\",\\"tier\\":\\"Tier2\\"}]" --provider-namespace "Microsoft.Contoso" --resource-type "testResourceType" --sku \
"testSku"
      - name: Skus_CreateOrUpdateNestedResourceTypeFirst
        text: |-
               az providerhub sku create --nested-resource-type-first "nestedResourceTypeFirst" --sku-settings \
"[{\\"name\\":\\"freeSku\\",\\"kind\\":\\"Standard\\",\\"tier\\":\\"Tier1\\"},{\\"name\\":\\"premiumSku\\",\\"costs\\":\
[{\\"meterId\\":\\"xxx\\"}],\\"kind\\":\\"Premium\\",\\"tier\\":\\"Tier2\\"}]" --provider-namespace \
"Microsoft.Contoso" --resource-type "testResourceType" --sku "testSku"
      - name: Skus_CreateOrUpdate
        text: |-
               az providerhub sku create --sku-settings "[{\\"name\\":\\"freeSku\\",\\"kind\\":\\"Standard\\",\\"tier\\\
":\\"Tier1\\"},{\\"name\\":\\"premiumSku\\",\\"costs\\":[{\\"meterId\\":\\"xxx\\"}],\\"kind\\":\\"Premium\\",\\"tier\\"\
:\\"Tier2\\"}]" --provider-namespace "Microsoft.Contoso" --resource-type "testResourceType" --sku "testSku"
"""

helps['providerhub sku delete'] = """
    type: command
    short-summary: "Deletes a resource type sku. And Deletes a resource type sku. And Deletes a resource type sku. And \
Deletes a resource type sku."
    examples:
      - name: Skus_DeleteNestedResourceTypeThird
        text: |-
               az providerhub sku delete --nested-resource-type-first "nestedResourceTypeFirst" \
--nested-resource-type-second "nestedResourceTypeSecond" --nested-resource-type-third "nestedResourceTypeThird" \
--provider-namespace "Microsoft.Contoso" --resource-type "testResourceType" --sku "testSku"
      - name: Skus_DeleteNestedResourceTypeSecond
        text: |-
               az providerhub sku delete --nested-resource-type-first "nestedResourceTypeFirst" \
--nested-resource-type-second "nestedResourceTypeSecond" --provider-namespace "Microsoft.Contoso" --resource-type \
"testResourceType" --sku "testSku"
      - name: Skus_DeleteNestedResourceTypeFirst
        text: |-
               az providerhub sku delete --nested-resource-type-first "nestedResourceTypeFirst" --provider-namespace \
"Microsoft.Contoso" --resource-type "testResourceType" --sku "testSku"
      - name: Skus_Delete
        text: |-
               az providerhub sku delete --provider-namespace "Microsoft.Contoso" --resource-type "testResourceType" \
--sku "testSku"
"""

helps['providerhub sku show-nested-resource-type-first'] = """
    type: command
    short-summary: "Gets the sku details for the given resource type and sku name."
    examples:
      - name: Skus_GetNestedResourceTypeFirst
        text: |-
               az providerhub sku show-nested-resource-type-first --nested-resource-type-first \
"nestedResourceTypeFirst" --provider-namespace "Microsoft.Contoso" --resource-type "testResourceType" --sku "testSku"
"""

helps['providerhub sku show-nested-resource-type-second'] = """
    type: command
    short-summary: "Gets the sku details for the given resource type and sku name."
    examples:
      - name: Skus_GetNestedResourceTypeSecond
        text: |-
               az providerhub sku show-nested-resource-type-second --nested-resource-type-first \
"nestedResourceTypeFirst" --nested-resource-type-second "nestedResourceTypeSecond" --provider-namespace \
"Microsoft.Contoso" --resource-type "testResourceType" --sku "testSku"
"""

helps['providerhub sku show-nested-resource-type-third'] = """
    type: command
    short-summary: "Gets the sku details for the given resource type and sku name."
    examples:
      - name: Skus_GetNestedResourceTypeThird
        text: |-
               az providerhub sku show-nested-resource-type-third --nested-resource-type-first \
"nestedResourceTypeFirst" --nested-resource-type-second "nestedResourceTypeSecond" --nested-resource-type-third \
"nestedResourceTypeThird" --provider-namespace "Microsoft.Contoso" --resource-type "testResourceType" --sku "testSku"
"""
