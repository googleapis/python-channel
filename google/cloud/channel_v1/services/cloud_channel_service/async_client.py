# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Mapping, Optional, Sequence, Tuple, Type, Union

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore
import pkg_resources

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.type import postal_address_pb2  # type: ignore

from google.cloud.channel_v1.services.cloud_channel_service import pagers
from google.cloud.channel_v1.types import (
    channel_partner_links,
    common,
    customers,
    entitlements,
    offers,
    operations,
    products,
    repricing,
    service,
)

from .client import CloudChannelServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, CloudChannelServiceTransport
from .transports.grpc_asyncio import CloudChannelServiceGrpcAsyncIOTransport


class CloudChannelServiceAsyncClient:
    """CloudChannelService lets Google cloud resellers and distributors
    manage their customers, channel partners, entitlements, and reports.

    Using this service:

    1. Resellers and distributors can manage a customer entity.
    2. Distributors can register an authorized reseller in their channel
       and provide them with delegated admin access.
    3. Resellers and distributors can manage customer entitlements.

    CloudChannelService exposes the following resources:

    -  [Customer][google.cloud.channel.v1.Customer]s: An entity—usually
       an enterprise—managed by a reseller or distributor.

    -  [Entitlement][google.cloud.channel.v1.Entitlement]s: An entity
       that provides a customer with the means to use a service.
       Entitlements are created or updated as a result of a successful
       fulfillment.

    -  [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]s:
       An entity that identifies links between distributors and their
       indirect resellers in a channel.
    """

    _client: CloudChannelServiceClient

    DEFAULT_ENDPOINT = CloudChannelServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = CloudChannelServiceClient.DEFAULT_MTLS_ENDPOINT

    channel_partner_link_path = staticmethod(
        CloudChannelServiceClient.channel_partner_link_path
    )
    parse_channel_partner_link_path = staticmethod(
        CloudChannelServiceClient.parse_channel_partner_link_path
    )
    channel_partner_repricing_config_path = staticmethod(
        CloudChannelServiceClient.channel_partner_repricing_config_path
    )
    parse_channel_partner_repricing_config_path = staticmethod(
        CloudChannelServiceClient.parse_channel_partner_repricing_config_path
    )
    customer_path = staticmethod(CloudChannelServiceClient.customer_path)
    parse_customer_path = staticmethod(CloudChannelServiceClient.parse_customer_path)
    customer_repricing_config_path = staticmethod(
        CloudChannelServiceClient.customer_repricing_config_path
    )
    parse_customer_repricing_config_path = staticmethod(
        CloudChannelServiceClient.parse_customer_repricing_config_path
    )
    entitlement_path = staticmethod(CloudChannelServiceClient.entitlement_path)
    parse_entitlement_path = staticmethod(
        CloudChannelServiceClient.parse_entitlement_path
    )
    offer_path = staticmethod(CloudChannelServiceClient.offer_path)
    parse_offer_path = staticmethod(CloudChannelServiceClient.parse_offer_path)
    product_path = staticmethod(CloudChannelServiceClient.product_path)
    parse_product_path = staticmethod(CloudChannelServiceClient.parse_product_path)
    sku_path = staticmethod(CloudChannelServiceClient.sku_path)
    parse_sku_path = staticmethod(CloudChannelServiceClient.parse_sku_path)
    common_billing_account_path = staticmethod(
        CloudChannelServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        CloudChannelServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(CloudChannelServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        CloudChannelServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        CloudChannelServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        CloudChannelServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(CloudChannelServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        CloudChannelServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(CloudChannelServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        CloudChannelServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CloudChannelServiceAsyncClient: The constructed client.
        """
        return CloudChannelServiceClient.from_service_account_info.__func__(CloudChannelServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CloudChannelServiceAsyncClient: The constructed client.
        """
        return CloudChannelServiceClient.from_service_account_file.__func__(CloudChannelServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return CloudChannelServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> CloudChannelServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            CloudChannelServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(CloudChannelServiceClient).get_transport_class,
        type(CloudChannelServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, CloudChannelServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the cloud channel service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.CloudChannelServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = CloudChannelServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_customers(
        self,
        request: Union[service.ListCustomersRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListCustomersAsyncPager:
        r"""List [Customer][google.cloud.channel.v1.Customer]s.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request is
           different from the reseller account in the API request.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.

        Return value: List of
        [Customer][google.cloud.channel.v1.Customer]s, or an empty list
        if there are no customers.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_customers():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ListCustomersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_customers(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListCustomersRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ListCustomers][google.cloud.channel.v1.CloudChannelService.ListCustomers]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListCustomersAsyncPager:
                Response message for
                [CloudChannelService.ListCustomers][google.cloud.channel.v1.CloudChannelService.ListCustomers].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListCustomersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_customers,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListCustomersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_customer(
        self,
        request: Union[service.GetCustomerRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> customers.Customer:
        r"""Returns the requested
        [Customer][google.cloud.channel.v1.Customer] resource.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request is
           different from the reseller account in the API request.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: The customer resource doesn't exist. Usually the
           result of an invalid name parameter.

        Return value: The [Customer][google.cloud.channel.v1.Customer]
        resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_get_customer():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.GetCustomerRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_customer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.GetCustomerRequest, dict]):
                The request object. Request message for
                [CloudChannelService.GetCustomer][google.cloud.channel.v1.CloudChannelService.GetCustomer].
            name (:class:`str`):
                Required. The resource name of the customer to retrieve.
                Name uses the format:
                accounts/{account_id}/customers/{customer_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.Customer:
                Entity representing a customer of a
                reseller or distributor.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetCustomerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_customer,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def check_cloud_identity_accounts_exist(
        self,
        request: Union[service.CheckCloudIdentityAccountsExistRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.CheckCloudIdentityAccountsExistResponse:
        r"""Confirms the existence of Cloud Identity accounts based on the
        domain and if the Cloud Identity accounts are owned by the
        reseller.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request is
           different from the reseller account in the API request.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  INVALID_VALUE: Invalid domain value in the request.

        Return value: A list of
        [CloudIdentityCustomerAccount][google.cloud.channel.v1.CloudIdentityCustomerAccount]
        resources for the domain (may be empty)

        Note: in the v1alpha1 version of the API, a NOT_FOUND error
        returns if no
        [CloudIdentityCustomerAccount][google.cloud.channel.v1.CloudIdentityCustomerAccount]
        resources match the domain.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_check_cloud_identity_accounts_exist():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.CheckCloudIdentityAccountsExistRequest(
                    parent="parent_value",
                    domain="domain_value",
                )

                # Make the request
                response = await client.check_cloud_identity_accounts_exist(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.CheckCloudIdentityAccountsExistRequest, dict]):
                The request object. Request message for
                [CloudChannelService.CheckCloudIdentityAccountsExist][google.cloud.channel.v1.CloudChannelService.CheckCloudIdentityAccountsExist].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.CheckCloudIdentityAccountsExistResponse:
                Response message for
                   [CloudChannelService.CheckCloudIdentityAccountsExist][google.cloud.channel.v1.CloudChannelService.CheckCloudIdentityAccountsExist].

        """
        # Create or coerce a protobuf request object.
        request = service.CheckCloudIdentityAccountsExistRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.check_cloud_identity_accounts_exist,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_customer(
        self,
        request: Union[service.CreateCustomerRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> customers.Customer:
        r"""Creates a new [Customer][google.cloud.channel.v1.Customer]
        resource under the reseller or distributor account.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request is
           different from the reseller account in the API request.
        -  INVALID_ARGUMENT:

           -  Required request parameters are missing or invalid.
           -  Domain field value doesn't match the primary email domain.

        Return value: The newly created
        [Customer][google.cloud.channel.v1.Customer] resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_create_customer():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                customer = channel_v1.Customer()
                customer.org_display_name = "org_display_name_value"
                customer.domain = "domain_value"

                request = channel_v1.CreateCustomerRequest(
                    parent="parent_value",
                    customer=customer,
                )

                # Make the request
                response = await client.create_customer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.CreateCustomerRequest, dict]):
                The request object. Request message for
                [CloudChannelService.CreateCustomer][google.cloud.channel.v1.CloudChannelService.CreateCustomer]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.Customer:
                Entity representing a customer of a
                reseller or distributor.

        """
        # Create or coerce a protobuf request object.
        request = service.CreateCustomerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_customer,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_customer(
        self,
        request: Union[service.UpdateCustomerRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> customers.Customer:
        r"""Updates an existing [Customer][google.cloud.channel.v1.Customer]
        resource for the reseller or distributor.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request is
           different from the reseller account in the API request.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: No [Customer][google.cloud.channel.v1.Customer]
           resource found for the name in the request.

        Return value: The updated
        [Customer][google.cloud.channel.v1.Customer] resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_update_customer():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                customer = channel_v1.Customer()
                customer.org_display_name = "org_display_name_value"
                customer.domain = "domain_value"

                request = channel_v1.UpdateCustomerRequest(
                    customer=customer,
                )

                # Make the request
                response = await client.update_customer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.UpdateCustomerRequest, dict]):
                The request object. Request message for
                [CloudChannelService.UpdateCustomer][google.cloud.channel.v1.CloudChannelService.UpdateCustomer].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.Customer:
                Entity representing a customer of a
                reseller or distributor.

        """
        # Create or coerce a protobuf request object.
        request = service.UpdateCustomerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_customer,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("customer.name", request.customer.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_customer(
        self,
        request: Union[service.DeleteCustomerRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes the given [Customer][google.cloud.channel.v1.Customer]
        permanently.

        Possible error codes:

        -  PERMISSION_DENIED: The account making the request does not
           own this customer.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  FAILED_PRECONDITION: The customer has existing entitlements.
        -  NOT_FOUND: No [Customer][google.cloud.channel.v1.Customer]
           resource found for the name in the request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_delete_customer():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.DeleteCustomerRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_customer(request=request)

        Args:
            request (Union[google.cloud.channel_v1.types.DeleteCustomerRequest, dict]):
                The request object. Request message for
                [CloudChannelService.DeleteCustomer][google.cloud.channel.v1.CloudChannelService.DeleteCustomer].
            name (:class:`str`):
                Required. The resource name of the
                customer to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.DeleteCustomerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_customer,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def import_customer(
        self,
        request: Union[service.ImportCustomerRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> customers.Customer:
        r"""Imports a [Customer][google.cloud.channel.v1.Customer] from the
        Cloud Identity associated with the provided Cloud Identity ID or
        domain before a TransferEntitlements call. If a linked Customer
        already exists and overwrite_if_exists is true, it will update
        that Customer's data.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request is
           different from the reseller account in the API request.
        -  NOT_FOUND: Cloud Identity doesn't exist or was deleted.
        -  INVALID_ARGUMENT: Required parameters are missing, or the
           auth_token is expired or invalid.
        -  ALREADY_EXISTS: A customer already exists and has conflicting
           critical fields. Requires an overwrite.

        Return value: The [Customer][google.cloud.channel.v1.Customer].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_import_customer():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ImportCustomerRequest(
                    domain="domain_value",
                    parent="parent_value",
                    overwrite_if_exists=True,
                )

                # Make the request
                response = await client.import_customer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ImportCustomerRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ImportCustomer][google.cloud.channel.v1.CloudChannelService.ImportCustomer]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.Customer:
                Entity representing a customer of a
                reseller or distributor.

        """
        # Create or coerce a protobuf request object.
        request = service.ImportCustomerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.import_customer,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def provision_cloud_identity(
        self,
        request: Union[service.ProvisionCloudIdentityRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a Cloud Identity for the given customer using the
        customer's information, or the information provided here.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: The customer was not found.
        -  ALREADY_EXISTS: The customer's primary email already exists.
           Retry after changing the customer's primary contact email.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        contains an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_provision_cloud_identity():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ProvisionCloudIdentityRequest(
                    customer="customer_value",
                )

                # Make the request
                operation = client.provision_cloud_identity(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ProvisionCloudIdentityRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ProvisionCloudIdentity][google.cloud.channel.v1.CloudChannelService.ProvisionCloudIdentity]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Customer` Entity
                representing a customer of a reseller or distributor.

        """
        # Create or coerce a protobuf request object.
        request = service.ProvisionCloudIdentityRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.provision_cloud_identity,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("customer", request.customer),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            customers.Customer,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def list_entitlements(
        self,
        request: Union[service.ListEntitlementsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListEntitlementsAsyncPager:
        r"""Lists [Entitlement][google.cloud.channel.v1.Entitlement]s
        belonging to a customer.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.

        Return value: A list of the customer's
        [Entitlement][google.cloud.channel.v1.Entitlement]s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_entitlements():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ListEntitlementsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_entitlements(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListEntitlementsRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ListEntitlements][google.cloud.channel.v1.CloudChannelService.ListEntitlements]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListEntitlementsAsyncPager:
                Response message for
                [CloudChannelService.ListEntitlements][google.cloud.channel.v1.CloudChannelService.ListEntitlements].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListEntitlementsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_entitlements,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEntitlementsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_transferable_skus(
        self,
        request: Union[service.ListTransferableSkusRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTransferableSkusAsyncPager:
        r"""List [TransferableSku][google.cloud.channel.v1.TransferableSku]s
        of a customer based on the Cloud Identity ID or Customer Name in
        the request.

        Use this method to list the entitlements information of an
        unowned customer. You should provide the customer's Cloud
        Identity ID or Customer Name.

        Possible error codes:

        -  PERMISSION_DENIED:

           -  The customer doesn't belong to the reseller and has no
              auth token.
           -  The supplied auth token is invalid.
           -  The reseller account making the request is different from
              the reseller account in the query.

        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.

        Return value: A list of the customer's
        [TransferableSku][google.cloud.channel.v1.TransferableSku].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_transferable_skus():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ListTransferableSkusRequest(
                    cloud_identity_id="cloud_identity_id_value",
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_transferable_skus(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListTransferableSkusRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ListTransferableSkus][google.cloud.channel.v1.CloudChannelService.ListTransferableSkus]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListTransferableSkusAsyncPager:
                Response message for
                [CloudChannelService.ListTransferableSkus][google.cloud.channel.v1.CloudChannelService.ListTransferableSkus].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListTransferableSkusRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_transferable_skus,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListTransferableSkusAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_transferable_offers(
        self,
        request: Union[service.ListTransferableOffersRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTransferableOffersAsyncPager:
        r"""List
        [TransferableOffer][google.cloud.channel.v1.TransferableOffer]s
        of a customer based on Cloud Identity ID or Customer Name in the
        request.

        Use this method when a reseller gets the entitlement information
        of an unowned customer. The reseller should provide the
        customer's Cloud Identity ID or Customer Name.

        Possible error codes:

        -  PERMISSION_DENIED:

           -  The customer doesn't belong to the reseller and has no
              auth token.
           -  The customer provided incorrect reseller information when
              generating auth token.
           -  The reseller account making the request is different from
              the reseller account in the query.

        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.

        Return value: List of
        [TransferableOffer][google.cloud.channel.v1.TransferableOffer]
        for the given customer and SKU.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_transferable_offers():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ListTransferableOffersRequest(
                    cloud_identity_id="cloud_identity_id_value",
                    parent="parent_value",
                    sku="sku_value",
                )

                # Make the request
                page_result = client.list_transferable_offers(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListTransferableOffersRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ListTransferableOffers][google.cloud.channel.v1.CloudChannelService.ListTransferableOffers]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListTransferableOffersAsyncPager:
                Response message for
                [CloudChannelService.ListTransferableOffers][google.cloud.channel.v1.CloudChannelService.ListTransferableOffers].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListTransferableOffersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_transferable_offers,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListTransferableOffersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_entitlement(
        self,
        request: Union[service.GetEntitlementRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> entitlements.Entitlement:
        r"""Returns the requested
        [Entitlement][google.cloud.channel.v1.Entitlement] resource.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: The customer entitlement was not found.

        Return value: The requested
        [Entitlement][google.cloud.channel.v1.Entitlement] resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_get_entitlement():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.GetEntitlementRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_entitlement(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.GetEntitlementRequest, dict]):
                The request object. Request message for
                [CloudChannelService.GetEntitlement][google.cloud.channel.v1.CloudChannelService.GetEntitlement].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.Entitlement:
                An entitlement is a representation of
                a customer's ability to use a service.

        """
        # Create or coerce a protobuf request object.
        request = service.GetEntitlementRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_entitlement,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_entitlement(
        self,
        request: Union[service.CreateEntitlementRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates an entitlement for a customer.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT:

           -  Required request parameters are missing or invalid.
           -  There is already a customer entitlement for a SKU from the
              same product family.

        -  INVALID_VALUE: Make sure the OfferId is valid. If it is,
           contact Google Channel support for further troubleshooting.
        -  NOT_FOUND: The customer or offer resource was not found.
        -  ALREADY_EXISTS:

           -  The SKU was already purchased for the customer.
           -  The customer's primary email already exists. Retry after
              changing the customer's primary contact email.

        -  CONDITION_NOT_MET or FAILED_PRECONDITION:

           -  The domain required for purchasing a SKU has not been
              verified.
           -  A pre-requisite SKU required to purchase an Add-On SKU is
              missing. For example, Google Workspace Business Starter is
              required to purchase Vault or Drive.
           -  (Developer accounts only) Reseller and resold domain must
              meet the following naming requirements:

              -  Domain names must start with goog-test.
              -  Domain names must include the reseller domain.

        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_create_entitlement():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                entitlement = channel_v1.Entitlement()
                entitlement.offer = "offer_value"

                request = channel_v1.CreateEntitlementRequest(
                    parent="parent_value",
                    entitlement=entitlement,
                )

                # Make the request
                operation = client.create_entitlement(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.CreateEntitlementRequest, dict]):
                The request object. Request message for
                [CloudChannelService.CreateEntitlement][google.cloud.channel.v1.CloudChannelService.CreateEntitlement]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        request = service.CreateEntitlementRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_entitlement,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def change_parameters(
        self,
        request: Union[service.ChangeParametersRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Change parameters of the entitlement.

        An entitlement update is a long-running operation and it updates
        the entitlement as a result of fulfillment.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid. For example, the number of seats being changed is
           greater than the allowed number of max seats, or decreasing
           seats for a commitment based plan.
        -  NOT_FOUND: Entitlement resource not found.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_change_parameters():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ChangeParametersRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.change_parameters(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ChangeParametersRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ChangeParametersRequest][].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        request = service.ChangeParametersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.change_parameters,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def change_renewal_settings(
        self,
        request: Union[service.ChangeRenewalSettingsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the renewal settings for an existing customer
        entitlement.

        An entitlement update is a long-running operation and it updates
        the entitlement as a result of fulfillment.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: Entitlement resource not found.
        -  NOT_COMMITMENT_PLAN: Renewal Settings are only applicable for
           a commitment plan. Can't enable or disable renewals for
           non-commitment plans.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_change_renewal_settings():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ChangeRenewalSettingsRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.change_renewal_settings(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ChangeRenewalSettingsRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ChangeRenewalSettings][google.cloud.channel.v1.CloudChannelService.ChangeRenewalSettings].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        request = service.ChangeRenewalSettingsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.change_renewal_settings,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def change_offer(
        self,
        request: Union[service.ChangeOfferRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the Offer for an existing customer entitlement.

        An entitlement update is a long-running operation and it updates
        the entitlement as a result of fulfillment.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: Offer or Entitlement resource not found.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_change_offer():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ChangeOfferRequest(
                    name="name_value",
                    offer="offer_value",
                )

                # Make the request
                operation = client.change_offer(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ChangeOfferRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ChangeOffer][google.cloud.channel.v1.CloudChannelService.ChangeOffer].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        request = service.ChangeOfferRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.change_offer,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def start_paid_service(
        self,
        request: Union[service.StartPaidServiceRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Starts paid service for a trial entitlement.

        Starts paid service for a trial entitlement immediately. This
        method is only applicable if a plan is set up for a trial
        entitlement but has some trial days remaining.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: Entitlement resource not found.
        -  FAILED_PRECONDITION/NOT_IN_TRIAL: This method only works for
           entitlement on trial plans.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_start_paid_service():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.StartPaidServiceRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.start_paid_service(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.StartPaidServiceRequest, dict]):
                The request object. Request message for
                [CloudChannelService.StartPaidService][google.cloud.channel.v1.CloudChannelService.StartPaidService].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        request = service.StartPaidServiceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.start_paid_service,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def suspend_entitlement(
        self,
        request: Union[service.SuspendEntitlementRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Suspends a previously fulfilled entitlement.

        An entitlement suspension is a long-running operation.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: Entitlement resource not found.
        -  NOT_ACTIVE: Entitlement is not active.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_suspend_entitlement():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.SuspendEntitlementRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.suspend_entitlement(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.SuspendEntitlementRequest, dict]):
                The request object. Request message for
                [CloudChannelService.SuspendEntitlement][google.cloud.channel.v1.CloudChannelService.SuspendEntitlement].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        request = service.SuspendEntitlementRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.suspend_entitlement,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def cancel_entitlement(
        self,
        request: Union[service.CancelEntitlementRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Cancels a previously fulfilled entitlement.

        An entitlement cancellation is a long-running operation.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request is
           different from the reseller account in the API request.
        -  FAILED_PRECONDITION: There are Google Cloud projects linked
           to the Google Cloud entitlement's Cloud Billing subaccount.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: Entitlement resource not found.
        -  DELETION_TYPE_NOT_ALLOWED: Cancel is only allowed for Google
           Workspace add-ons, or entitlements for Google Cloud's
           development platform.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The response will
        contain google.protobuf.Empty on success. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_cancel_entitlement():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.CancelEntitlementRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.cancel_entitlement(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.CancelEntitlementRequest, dict]):
                The request object. Request message for
                [CloudChannelService.CancelEntitlement][google.cloud.channel.v1.CloudChannelService.CancelEntitlement].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        request = service.CancelEntitlementRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.cancel_entitlement,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def activate_entitlement(
        self,
        request: Union[service.ActivateEntitlementRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Activates a previously suspended entitlement. Entitlements
        suspended for pending ToS acceptance can't be activated using
        this method.

        An entitlement activation is a long-running operation and it
        updates the state of the customer entitlement.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request is
           different from the reseller account in the API request.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: Entitlement resource not found.
        -  SUSPENSION_NOT_RESELLER_INITIATED: Can only activate
           reseller-initiated suspensions and entitlements that have
           accepted the TOS.
        -  NOT_SUSPENDED: Can only activate suspended entitlements not
           in an ACTIVE state.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_activate_entitlement():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ActivateEntitlementRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.activate_entitlement(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ActivateEntitlementRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ActivateEntitlement][google.cloud.channel.v1.CloudChannelService.ActivateEntitlement].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        request = service.ActivateEntitlementRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.activate_entitlement,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def transfer_entitlements(
        self,
        request: Union[service.TransferEntitlementsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Transfers customer entitlements to new reseller.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: The customer or offer resource was not found.
        -  ALREADY_EXISTS: The SKU was already transferred for the
           customer.
        -  CONDITION_NOT_MET or FAILED_PRECONDITION:

           -  The SKU requires domain verification to transfer, but the
              domain is not verified.
           -  An Add-On SKU (example, Vault or Drive) is missing the
              pre-requisite SKU (example, G Suite Basic).
           -  (Developer accounts only) Reseller and resold domain must
              meet the following naming requirements:

              -  Domain names must start with goog-test.
              -  Domain names must include the reseller domain.

           -  Specify all transferring entitlements.

        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_transfer_entitlements():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                entitlements = channel_v1.Entitlement()
                entitlements.offer = "offer_value"

                request = channel_v1.TransferEntitlementsRequest(
                    parent="parent_value",
                    entitlements=entitlements,
                )

                # Make the request
                operation = client.transfer_entitlements(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.TransferEntitlementsRequest, dict]):
                The request object. Request message for
                [CloudChannelService.TransferEntitlements][google.cloud.channel.v1.CloudChannelService.TransferEntitlements].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.channel_v1.types.TransferEntitlementsResponse` Response message for [CloudChannelService.TransferEntitlements][google.cloud.channel.v1.CloudChannelService.TransferEntitlements].
                   This is put in the response field of
                   google.longrunning.Operation.

        """
        # Create or coerce a protobuf request object.
        request = service.TransferEntitlementsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.transfer_entitlements,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            service.TransferEntitlementsResponse,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def transfer_entitlements_to_google(
        self,
        request: Union[service.TransferEntitlementsToGoogleRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Transfers customer entitlements from their current reseller to
        Google.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: The customer or offer resource was not found.
        -  ALREADY_EXISTS: The SKU was already transferred for the
           customer.
        -  CONDITION_NOT_MET or FAILED_PRECONDITION:

           -  The SKU requires domain verification to transfer, but the
              domain is not verified.
           -  An Add-On SKU (example, Vault or Drive) is missing the
              pre-requisite SKU (example, G Suite Basic).
           -  (Developer accounts only) Reseller and resold domain must
              meet the following naming requirements:

              -  Domain names must start with goog-test.
              -  Domain names must include the reseller domain.

        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The ID of a long-running operation.

        To get the results of the operation, call the GetOperation
        method of CloudChannelOperationsService. The response will
        contain google.protobuf.Empty on success. The Operation metadata
        will contain an instance of
        [OperationMetadata][google.cloud.channel.v1.OperationMetadata].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_transfer_entitlements_to_google():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                entitlements = channel_v1.Entitlement()
                entitlements.offer = "offer_value"

                request = channel_v1.TransferEntitlementsToGoogleRequest(
                    parent="parent_value",
                    entitlements=entitlements,
                )

                # Make the request
                operation = client.transfer_entitlements_to_google(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.TransferEntitlementsToGoogleRequest, dict]):
                The request object. Request message for
                [CloudChannelService.TransferEntitlementsToGoogle][google.cloud.channel.v1.CloudChannelService.TransferEntitlementsToGoogle].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        request = service.TransferEntitlementsToGoogleRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.transfer_entitlements_to_google,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def list_channel_partner_links(
        self,
        request: Union[service.ListChannelPartnerLinksRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListChannelPartnerLinksAsyncPager:
        r"""List
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]s
        belonging to a distributor. You must be a distributor to call
        this method.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request is
           different from the reseller account in the API request.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.

        Return value: The list of the distributor account's
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]
        resources.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_channel_partner_links():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ListChannelPartnerLinksRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_channel_partner_links(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListChannelPartnerLinksRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ListChannelPartnerLinks][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerLinks]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListChannelPartnerLinksAsyncPager:
                Response message for
                [CloudChannelService.ListChannelPartnerLinks][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerLinks].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListChannelPartnerLinksRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_channel_partner_links,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListChannelPartnerLinksAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_channel_partner_link(
        self,
        request: Union[service.GetChannelPartnerLinkRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> channel_partner_links.ChannelPartnerLink:
        r"""Returns the requested
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]
        resource. You must be a distributor to call this method.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request is
           different from the reseller account in the API request.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: ChannelPartnerLink resource not found because of
           an invalid channel partner link name.

        Return value: The
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]
        resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_get_channel_partner_link():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.GetChannelPartnerLinkRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_channel_partner_link(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.GetChannelPartnerLinkRequest, dict]):
                The request object. Request message for
                [CloudChannelService.GetChannelPartnerLink][google.cloud.channel.v1.CloudChannelService.GetChannelPartnerLink].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.ChannelPartnerLink:
                Entity representing a link between
                distributors and their indirect
                resellers in an n-tier resale channel.

        """
        # Create or coerce a protobuf request object.
        request = service.GetChannelPartnerLinkRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_channel_partner_link,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_channel_partner_link(
        self,
        request: Union[service.CreateChannelPartnerLinkRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> channel_partner_links.ChannelPartnerLink:
        r"""Initiates a channel partner link between a distributor and a
        reseller, or between resellers in an n-tier reseller channel.
        Invited partners need to follow the invite_link_uri provided in
        the response to accept. After accepting the invitation, a link
        is set up between the two parties. You must be a distributor to
        call this method.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request is
           different from the reseller account in the API request.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  ALREADY_EXISTS: The ChannelPartnerLink sent in the request
           already exists.
        -  NOT_FOUND: No Cloud Identity customer exists for provided
           domain.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The new
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]
        resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_create_channel_partner_link():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                channel_partner_link = channel_v1.ChannelPartnerLink()
                channel_partner_link.reseller_cloud_identity_id = "reseller_cloud_identity_id_value"
                channel_partner_link.link_state = "SUSPENDED"

                request = channel_v1.CreateChannelPartnerLinkRequest(
                    parent="parent_value",
                    channel_partner_link=channel_partner_link,
                )

                # Make the request
                response = await client.create_channel_partner_link(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.CreateChannelPartnerLinkRequest, dict]):
                The request object. Request message for
                [CloudChannelService.CreateChannelPartnerLink][google.cloud.channel.v1.CloudChannelService.CreateChannelPartnerLink]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.ChannelPartnerLink:
                Entity representing a link between
                distributors and their indirect
                resellers in an n-tier resale channel.

        """
        # Create or coerce a protobuf request object.
        request = service.CreateChannelPartnerLinkRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_channel_partner_link,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_channel_partner_link(
        self,
        request: Union[service.UpdateChannelPartnerLinkRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> channel_partner_links.ChannelPartnerLink:
        r"""Updates a channel partner link. Distributors call this method to
        change a link's status. For example, to suspend a partner link.
        You must be a distributor to call this method.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request is
           different from the reseller account in the API request.
        -  INVALID_ARGUMENT:

           -  Required request parameters are missing or invalid.
           -  Link state cannot change from invited to active or
              suspended.
           -  Cannot send reseller_cloud_identity_id, invite_url, or
              name in update mask.

        -  NOT_FOUND: ChannelPartnerLink resource not found.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The updated
        [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink]
        resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_update_channel_partner_link():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                channel_partner_link = channel_v1.ChannelPartnerLink()
                channel_partner_link.reseller_cloud_identity_id = "reseller_cloud_identity_id_value"
                channel_partner_link.link_state = "SUSPENDED"

                request = channel_v1.UpdateChannelPartnerLinkRequest(
                    name="name_value",
                    channel_partner_link=channel_partner_link,
                )

                # Make the request
                response = await client.update_channel_partner_link(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.UpdateChannelPartnerLinkRequest, dict]):
                The request object. Request message for
                [CloudChannelService.UpdateChannelPartnerLink][google.cloud.channel.v1.CloudChannelService.UpdateChannelPartnerLink]
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.ChannelPartnerLink:
                Entity representing a link between
                distributors and their indirect
                resellers in an n-tier resale channel.

        """
        # Create or coerce a protobuf request object.
        request = service.UpdateChannelPartnerLinkRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_channel_partner_link,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_customer_repricing_config(
        self,
        request: Union[service.GetCustomerRepricingConfigRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> repricing.CustomerRepricingConfig:
        r"""Gets information about how a Reseller modifies their bill before
        sending it to a Customer.

        Possible Error Codes:

        -  PERMISSION_DENIED: If the account making the request and the
           account being queried are different.
        -  NOT_FOUND: The
           [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
           was not found.
        -  INTERNAL: Any non-user error related to technical issues in
           the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        resource, otherwise returns an error.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_get_customer_repricing_config():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.GetCustomerRepricingConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_customer_repricing_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.GetCustomerRepricingConfigRequest, dict]):
                The request object. Request message for
                [CloudChannelService.GetCustomerRepricingConfig][google.cloud.channel.v1.CloudChannelService.GetCustomerRepricingConfig].
            name (:class:`str`):
                Required. The resource name of the
                CustomerRepricingConfig. Format:
                accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.CustomerRepricingConfig:
                Configuration for how a reseller will
                reprice a Customer.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetCustomerRepricingConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_customer_repricing_config,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_customer_repricing_configs(
        self,
        request: Union[service.ListCustomerRepricingConfigsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListCustomerRepricingConfigsAsyncPager:
        r"""Lists information about how a Reseller modifies their bill
        before sending it to a Customer.

        Possible Error Codes:

        -  PERMISSION_DENIED: If the account making the request and the
           account being queried are different.
        -  NOT_FOUND: The
           [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
           specified does not exist or is not associated with the given
           account.
        -  INTERNAL: Any non-user error related to technical issues in
           the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        resources. The data for each resource is displayed in the
        ascending order of:

        -  customer ID
        -  [RepricingConfig.EntitlementGranularity.entitlement][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity.entitlement]
        -  [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        -  [CustomerRepricingConfig.update_time][google.cloud.channel.v1.CustomerRepricingConfig.update_time]

        If unsuccessful, returns an error.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_customer_repricing_configs():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ListCustomerRepricingConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_customer_repricing_configs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListCustomerRepricingConfigsRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ListCustomerRepricingConfigs][google.cloud.channel.v1.CloudChannelService.ListCustomerRepricingConfigs].
            parent (:class:`str`):
                Required. The resource name of the customer. Parent uses
                the format:
                accounts/{account_id}/customers/{customer_id}. Supports
                accounts/{account_id}/customers/- to retrieve configs
                for all customers.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListCustomerRepricingConfigsAsyncPager:
                Response message for
                [CloudChannelService.ListCustomerRepricingConfigs][google.cloud.channel.v1.CloudChannelService.ListCustomerRepricingConfigs].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListCustomerRepricingConfigsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_customer_repricing_configs,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListCustomerRepricingConfigsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_customer_repricing_config(
        self,
        request: Union[service.CreateCustomerRepricingConfigRequest, dict] = None,
        *,
        parent: str = None,
        customer_repricing_config: repricing.CustomerRepricingConfig = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> repricing.CustomerRepricingConfig:
        r"""Creates a CustomerRepricingConfig. Call this method to set
        modifications for a specific customer's bill. You can only
        create configs if the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is a future month. If needed, you can create a config for the
        current month, with some restrictions.

        When creating a config for a future month, make sure there are
        no existing configs for that
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].

        The following restrictions are for creating configs in the
        current month.

        -  This functionality is reserved for recovering from an
           erroneous config, and should not be used for regular business
           cases.
        -  The new config will not modify exports used with other
           configs. Changes to the config may be immediate, but may take
           up to 24 hours.
        -  There is a limit of ten configs for any
           [RepricingConfig.EntitlementGranularity.entitlement][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity.entitlement]
           or
           [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].
        -  The contained
           [CustomerRepricingConfig.repricing_config][google.cloud.channel.v1.CustomerRepricingConfig.repricing_config]
           vaule must be different from the value used in the current
           config for a
           [RepricingConfig.EntitlementGranularity.entitlement][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity.entitlement].

        Possible Error Codes:

        -  PERMISSION_DENIED: If the account making the request and the
           account being queried are different.
        -  INVALID_ARGUMENT: Missing or invalid required parameters in
           the request. Also displays if the updated config is for the
           current month or past months.
        -  NOT_FOUND: The
           [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
           specified does not exist or is not associated with the given
           account.
        -  INTERNAL: Any non-user error related to technical issues in
           the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the updated
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        resource, otherwise returns an error.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_create_customer_repricing_config():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                customer_repricing_config = channel_v1.CustomerRepricingConfig()
                customer_repricing_config.repricing_config.rebilling_basis = "DIRECT_CUSTOMER_COST"

                request = channel_v1.CreateCustomerRepricingConfigRequest(
                    parent="parent_value",
                    customer_repricing_config=customer_repricing_config,
                )

                # Make the request
                response = await client.create_customer_repricing_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.CreateCustomerRepricingConfigRequest, dict]):
                The request object. Request message for
                [CloudChannelService.CreateCustomerRepricingConfig][google.cloud.channel.v1.CloudChannelService.CreateCustomerRepricingConfig].
            parent (:class:`str`):
                Required. The resource name of the customer that will
                receive this repricing config. Parent uses the format:
                accounts/{account_id}/customers/{customer_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            customer_repricing_config (:class:`google.cloud.channel_v1.types.CustomerRepricingConfig`):
                Required. The CustomerRepricingConfig
                object to update.

                This corresponds to the ``customer_repricing_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.CustomerRepricingConfig:
                Configuration for how a reseller will
                reprice a Customer.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, customer_repricing_config])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.CreateCustomerRepricingConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if customer_repricing_config is not None:
            request.customer_repricing_config = customer_repricing_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_customer_repricing_config,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_customer_repricing_config(
        self,
        request: Union[service.UpdateCustomerRepricingConfigRequest, dict] = None,
        *,
        customer_repricing_config: repricing.CustomerRepricingConfig = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> repricing.CustomerRepricingConfig:
        r"""Updates a CustomerRepricingConfig. Call this method to set
        modifications for a specific customer's bill. This method
        overwrites the existing CustomerRepricingConfig.

        You can only update configs if the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is a future month. To make changes to configs for the current
        month, use
        [CreateCustomerRepricingConfig][google.cloud.channel.v1.CloudChannelService.CreateCustomerRepricingConfig],
        taking note of its restrictions. You cannot update the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].

        When updating a config in the future:

        -  This config must already exist.

        Possible Error Codes:

        -  PERMISSION_DENIED: If the account making the request and the
           account being queried are different.
        -  INVALID_ARGUMENT: Missing or invalid required parameters in
           the request. Also displays if the updated config is for the
           current month or past months.
        -  NOT_FOUND: The
           [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
           specified does not exist or is not associated with the given
           account.
        -  INTERNAL: Any non-user error related to technical issues in
           the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the updated
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        resource, otherwise returns an error.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_update_customer_repricing_config():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                customer_repricing_config = channel_v1.CustomerRepricingConfig()
                customer_repricing_config.repricing_config.rebilling_basis = "DIRECT_CUSTOMER_COST"

                request = channel_v1.UpdateCustomerRepricingConfigRequest(
                    customer_repricing_config=customer_repricing_config,
                )

                # Make the request
                response = await client.update_customer_repricing_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.UpdateCustomerRepricingConfigRequest, dict]):
                The request object. Request message for
                [CloudChannelService.UpdateCustomerRepricingConfig][google.cloud.channel.v1.CloudChannelService.UpdateCustomerRepricingConfig].
            customer_repricing_config (:class:`google.cloud.channel_v1.types.CustomerRepricingConfig`):
                Required. The CustomerRepricingConfig
                object to update.

                This corresponds to the ``customer_repricing_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.CustomerRepricingConfig:
                Configuration for how a reseller will
                reprice a Customer.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([customer_repricing_config])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.UpdateCustomerRepricingConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if customer_repricing_config is not None:
            request.customer_repricing_config = customer_repricing_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_customer_repricing_config,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "customer_repricing_config.name",
                        request.customer_repricing_config.name,
                    ),
                )
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_customer_repricing_config(
        self,
        request: Union[service.DeleteCustomerRepricingConfigRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes the given
        [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
        permanently. You can only delete configs if their
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is set to a date after the current month.

        Possible error codes:

        -  PERMISSION_DENIED: The account making the request does not
           own this customer.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  FAILED_PRECONDITION: The
           [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
           is active or in the past.
        -  NOT_FOUND: No
           [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
           found for the name in the request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_delete_customer_repricing_config():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.DeleteCustomerRepricingConfigRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_customer_repricing_config(request=request)

        Args:
            request (Union[google.cloud.channel_v1.types.DeleteCustomerRepricingConfigRequest, dict]):
                The request object. Request message for
                [CloudChannelService.DeleteCustomerRepricingConfig][google.cloud.channel.v1.CloudChannelService.DeleteCustomerRepricingConfig].
            name (:class:`str`):
                Required. The resource name of the customer repricing
                config rule to delete. Format:
                accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.DeleteCustomerRepricingConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_customer_repricing_config,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def get_channel_partner_repricing_config(
        self,
        request: Union[service.GetChannelPartnerRepricingConfigRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> repricing.ChannelPartnerRepricingConfig:
        r"""Gets information about how a Distributor modifies their bill
        before sending it to a ChannelPartner.

        Possible Error Codes:

        -  PERMISSION_DENIED: If the account making the request and the
           account being queried are different.
        -  NOT_FOUND: The
           [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
           was not found.
        -  INTERNAL: Any non-user error related to technical issues in
           the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        resource, otherwise returns an error.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_get_channel_partner_repricing_config():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.GetChannelPartnerRepricingConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_channel_partner_repricing_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.GetChannelPartnerRepricingConfigRequest, dict]):
                The request object. Request message for
                [CloudChannelService.GetChannelPartnerRepricingConfig][google.cloud.channel.v1.CloudChannelService.GetChannelPartnerRepricingConfig]
            name (:class:`str`):
                Required. The resource name of the
                ChannelPartnerRepricingConfig Format:
                accounts/{account_id}/channelPartnerLinks/{channel_partner_id}/channelPartnerRepricingConfigs/{id}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.ChannelPartnerRepricingConfig:
                Configuration for how a distributor
                will rebill a channel partner (also
                known as a distributor-authorized
                reseller).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetChannelPartnerRepricingConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_channel_partner_repricing_config,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_channel_partner_repricing_configs(
        self,
        request: Union[service.ListChannelPartnerRepricingConfigsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListChannelPartnerRepricingConfigsAsyncPager:
        r"""Lists information about how a Reseller modifies their bill
        before sending it to a ChannelPartner.

        Possible Error Codes:

        -  PERMISSION_DENIED: If the account making the request and the
           account being queried are different.
        -  NOT_FOUND: The
           [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
           specified does not exist or is not associated with the given
           account.
        -  INTERNAL: Any non-user error related to technical issues in
           the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        resources. The data for each resource is displayed in the
        ascending order of:

        -  channel partner ID
        -  [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        -  [ChannelPartnerRepricingConfig.update_time][google.cloud.channel.v1.ChannelPartnerRepricingConfig.update_time]

        If unsuccessful, returns an error.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_channel_partner_repricing_configs():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ListChannelPartnerRepricingConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_channel_partner_repricing_configs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListChannelPartnerRepricingConfigsRequest, dict]):
                The request object. Request message for
                [CloudChannelService.ListChannelPartnerRepricingConfigs][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerRepricingConfigs].
            parent (:class:`str`):
                Required. The resource name of the account's
                [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink].
                Parent uses the format:
                accounts/{account_id}/channelPartnerLinks/{channel_partner_id}.
                Supports accounts/{account_id}/channelPartnerLinks/- to
                retrieve configs for all channel partners.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListChannelPartnerRepricingConfigsAsyncPager:
                Response message for
                   [CloudChannelService.ListChannelPartnerRepricingConfigs][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerRepricingConfigs].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListChannelPartnerRepricingConfigsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_channel_partner_repricing_configs,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListChannelPartnerRepricingConfigsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_channel_partner_repricing_config(
        self,
        request: Union[service.CreateChannelPartnerRepricingConfigRequest, dict] = None,
        *,
        parent: str = None,
        channel_partner_repricing_config: repricing.ChannelPartnerRepricingConfig = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> repricing.ChannelPartnerRepricingConfig:
        r"""Creates a ChannelPartnerRepricingConfig. Call this method to set
        modifications for a specific ChannelPartner's bill. You can only
        create configs if the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is a future month. If needed, you can create a config for the
        current month, with some restrictions.

        When creating a config for a future month, make sure there are
        no existing configs for that
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].

        The following restrictions are for creating configs in the
        current month.

        -  This functionality is reserved for recovering from an
           erroneous config, and should not be used for regular business
           cases.
        -  The new config will not modify exports used with other
           configs. Changes to the config may be immediate, but may take
           up to 24 hours.
        -  There is a limit of ten configs for any ChannelPartner or
           [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].
        -  The contained
           [ChannelPartnerRepricingConfig.repricing_config][google.cloud.channel.v1.ChannelPartnerRepricingConfig.repricing_config]
           vaule must be different from the value used in the current
           config for a ChannelPartner.

        Possible Error Codes:

        -  PERMISSION_DENIED: If the account making the request and the
           account being queried are different.
        -  INVALID_ARGUMENT: Missing or invalid required parameters in
           the request. Also displays if the updated config is for the
           current month or past months.
        -  NOT_FOUND: The
           [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
           specified does not exist or is not associated with the given
           account.
        -  INTERNAL: Any non-user error related to technical issues in
           the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the updated
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        resource, otherwise returns an error.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_create_channel_partner_repricing_config():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                channel_partner_repricing_config = channel_v1.ChannelPartnerRepricingConfig()
                channel_partner_repricing_config.repricing_config.rebilling_basis = "DIRECT_CUSTOMER_COST"

                request = channel_v1.CreateChannelPartnerRepricingConfigRequest(
                    parent="parent_value",
                    channel_partner_repricing_config=channel_partner_repricing_config,
                )

                # Make the request
                response = await client.create_channel_partner_repricing_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.CreateChannelPartnerRepricingConfigRequest, dict]):
                The request object. Request message for
                [CloudChannelService.CreateChannelPartnerRepricingConfig][google.cloud.channel.v1.CloudChannelService.CreateChannelPartnerRepricingConfig].
            parent (:class:`str`):
                Required. The resource name of the ChannelPartner that
                will receive the repricing config. Parent uses the
                format:
                accounts/{account_id}/channelPartnerLinks/{channel_partner_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            channel_partner_repricing_config (:class:`google.cloud.channel_v1.types.ChannelPartnerRepricingConfig`):
                Required. The
                ChannelPartnerRepricingConfig object to
                update.

                This corresponds to the ``channel_partner_repricing_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.ChannelPartnerRepricingConfig:
                Configuration for how a distributor
                will rebill a channel partner (also
                known as a distributor-authorized
                reseller).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, channel_partner_repricing_config])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.CreateChannelPartnerRepricingConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if channel_partner_repricing_config is not None:
            request.channel_partner_repricing_config = channel_partner_repricing_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_channel_partner_repricing_config,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_channel_partner_repricing_config(
        self,
        request: Union[service.UpdateChannelPartnerRepricingConfigRequest, dict] = None,
        *,
        channel_partner_repricing_config: repricing.ChannelPartnerRepricingConfig = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> repricing.ChannelPartnerRepricingConfig:
        r"""Updates a ChannelPartnerRepricingConfig. Call this method to set
        modifications for a specific ChannelPartner's bill. This method
        overwrites the existing CustomerRepricingConfig.

        You can only update configs if the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is a future month. To make changes to configs for the current
        month, use
        [CreateChannelPartnerRepricingConfig][google.cloud.channel.v1.CloudChannelService.CreateChannelPartnerRepricingConfig],
        taking note of its restrictions. You cannot update the
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month].

        When updating a config in the future:

        -  This config must already exist.

        Possible Error Codes:

        -  PERMISSION_DENIED: If the account making the request and the
           account being queried are different.
        -  INVALID_ARGUMENT: Missing or invalid required parameters in
           the request. Also displays if the updated config is for the
           current month or past months.
        -  NOT_FOUND: The
           [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
           specified does not exist or is not associated with the given
           account.
        -  INTERNAL: Any non-user error related to technical issues in
           the backend. In this case, contact Cloud Channel support.

        Return Value: If successful, the updated
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        resource, otherwise returns an error.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_update_channel_partner_repricing_config():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                channel_partner_repricing_config = channel_v1.ChannelPartnerRepricingConfig()
                channel_partner_repricing_config.repricing_config.rebilling_basis = "DIRECT_CUSTOMER_COST"

                request = channel_v1.UpdateChannelPartnerRepricingConfigRequest(
                    channel_partner_repricing_config=channel_partner_repricing_config,
                )

                # Make the request
                response = await client.update_channel_partner_repricing_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.UpdateChannelPartnerRepricingConfigRequest, dict]):
                The request object. Request message for
                [CloudChannelService.UpdateChannelPartnerRepricingConfig][google.cloud.channel.v1.CloudChannelService.UpdateChannelPartnerRepricingConfig].
            channel_partner_repricing_config (:class:`google.cloud.channel_v1.types.ChannelPartnerRepricingConfig`):
                Required. The
                ChannelPartnerRepricingConfig object to
                update.

                This corresponds to the ``channel_partner_repricing_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.ChannelPartnerRepricingConfig:
                Configuration for how a distributor
                will rebill a channel partner (also
                known as a distributor-authorized
                reseller).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([channel_partner_repricing_config])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.UpdateChannelPartnerRepricingConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if channel_partner_repricing_config is not None:
            request.channel_partner_repricing_config = channel_partner_repricing_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_channel_partner_repricing_config,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "channel_partner_repricing_config.name",
                        request.channel_partner_repricing_config.name,
                    ),
                )
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_channel_partner_repricing_config(
        self,
        request: Union[service.DeleteChannelPartnerRepricingConfigRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes the given
        [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
        permanently. You can only delete configs if their
        [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
        is set to a date after the current month.

        Possible error codes:

        -  PERMISSION_DENIED: The account making the request does not
           own this customer.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  FAILED_PRECONDITION: The
           [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
           is active or in the past.
        -  NOT_FOUND: No
           [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
           found for the name in the request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_delete_channel_partner_repricing_config():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.DeleteChannelPartnerRepricingConfigRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_channel_partner_repricing_config(request=request)

        Args:
            request (Union[google.cloud.channel_v1.types.DeleteChannelPartnerRepricingConfigRequest, dict]):
                The request object. Request message for
                DeleteChannelPartnerRepricingConfig.
            name (:class:`str`):
                Required. The resource name of the
                channel partner repricing config rule to
                delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.DeleteChannelPartnerRepricingConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_channel_partner_repricing_config,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def lookup_offer(
        self,
        request: Union[service.LookupOfferRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> offers.Offer:
        r"""Returns the requested [Offer][google.cloud.channel.v1.Offer]
        resource.

        Possible error codes:

        -  PERMISSION_DENIED: The entitlement doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: Entitlement or offer was not found.

        Return value: The [Offer][google.cloud.channel.v1.Offer]
        resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_lookup_offer():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.LookupOfferRequest(
                    entitlement="entitlement_value",
                )

                # Make the request
                response = await client.lookup_offer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.LookupOfferRequest, dict]):
                The request object. Request message for LookupOffer.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.Offer:
                Represents an offer made to resellers for purchase.
                   An offer is associated with a
                   [Sku][google.cloud.channel.v1.Sku], has a plan for
                   payment, a price, and defines the constraints for
                   buying.

        """
        # Create or coerce a protobuf request object.
        request = service.LookupOfferRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.lookup_offer,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("entitlement", request.entitlement),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_products(
        self,
        request: Union[service.ListProductsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListProductsAsyncPager:
        r"""Lists the Products the reseller is authorized to sell.

        Possible error codes:

        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_products():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ListProductsRequest(
                    account="account_value",
                )

                # Make the request
                page_result = client.list_products(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListProductsRequest, dict]):
                The request object. Request message for ListProducts.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListProductsAsyncPager:
                Response message for ListProducts.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListProductsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_products,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListProductsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_skus(
        self,
        request: Union[service.ListSkusRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListSkusAsyncPager:
        r"""Lists the SKUs for a product the reseller is authorized to sell.

        Possible error codes:

        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_skus():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ListSkusRequest(
                    parent="parent_value",
                    account="account_value",
                )

                # Make the request
                page_result = client.list_skus(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListSkusRequest, dict]):
                The request object. Request message for ListSkus.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListSkusAsyncPager:
                Response message for ListSkus.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListSkusRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_skus,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListSkusAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_offers(
        self,
        request: Union[service.ListOffersRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListOffersAsyncPager:
        r"""Lists the Offers the reseller can sell.

        Possible error codes:

        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_offers():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ListOffersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_offers(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListOffersRequest, dict]):
                The request object. Request message for ListOffers.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListOffersAsyncPager:
                Response message for ListOffers.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListOffersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_offers,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListOffersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_purchasable_skus(
        self,
        request: Union[service.ListPurchasableSkusRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPurchasableSkusAsyncPager:
        r"""Lists the following:

        -  SKUs that you can purchase for a customer
        -  SKUs that you can upgrade or downgrade for an entitlement.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_purchasable_skus():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                create_entitlement_purchase = channel_v1.CreateEntitlementPurchase()
                create_entitlement_purchase.product = "product_value"

                request = channel_v1.ListPurchasableSkusRequest(
                    create_entitlement_purchase=create_entitlement_purchase,
                    customer="customer_value",
                )

                # Make the request
                page_result = client.list_purchasable_skus(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListPurchasableSkusRequest, dict]):
                The request object. Request message for
                ListPurchasableSkus.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListPurchasableSkusAsyncPager:
                Response message for
                ListPurchasableSkus.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListPurchasableSkusRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_purchasable_skus,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("customer", request.customer),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListPurchasableSkusAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_purchasable_offers(
        self,
        request: Union[service.ListPurchasableOffersRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPurchasableOffersAsyncPager:
        r"""Lists the following:

        -  Offers that you can purchase for a customer.
        -  Offers that you can change for an entitlement.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_purchasable_offers():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                create_entitlement_purchase = channel_v1.CreateEntitlementPurchase()
                create_entitlement_purchase.sku = "sku_value"

                request = channel_v1.ListPurchasableOffersRequest(
                    create_entitlement_purchase=create_entitlement_purchase,
                    customer="customer_value",
                )

                # Make the request
                page_result = client.list_purchasable_offers(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListPurchasableOffersRequest, dict]):
                The request object. Request message for
                ListPurchasableOffers.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListPurchasableOffersAsyncPager:
                Response message for
                ListPurchasableOffers.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListPurchasableOffersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_purchasable_offers,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("customer", request.customer),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListPurchasableOffersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def register_subscriber(
        self,
        request: Union[service.RegisterSubscriberRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.RegisterSubscriberResponse:
        r"""Registers a service account with subscriber privileges on the
        Cloud Pub/Sub topic for this Channel Services account. After you
        create a subscriber, you get the events through
        [SubscriberEvent][google.cloud.channel.v1.SubscriberEvent]

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request
           and the provided reseller account are different, or the
           impersonated user is not a super admin.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The topic name with the registered service email
        address.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_register_subscriber():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.RegisterSubscriberRequest(
                    account="account_value",
                    service_account="service_account_value",
                )

                # Make the request
                response = await client.register_subscriber(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.RegisterSubscriberRequest, dict]):
                The request object. Request Message for
                RegisterSubscriber.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.RegisterSubscriberResponse:
                Response Message for
                RegisterSubscriber.

        """
        # Create or coerce a protobuf request object.
        request = service.RegisterSubscriberRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.register_subscriber,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("account", request.account),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def unregister_subscriber(
        self,
        request: Union[service.UnregisterSubscriberRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.UnregisterSubscriberResponse:
        r"""Unregisters a service account with subscriber privileges on the
        Cloud Pub/Sub topic created for this Channel Services account.
        If there are no service accounts left with subscriber
        privileges, this deletes the topic. You can call ListSubscribers
        to check for these accounts.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request
           and the provided reseller account are different, or the
           impersonated user is not a super admin.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: The topic resource doesn't exist.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: The topic name that unregistered the service email
        address. Returns a success response if the service email address
        wasn't registered with the topic.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_unregister_subscriber():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.UnregisterSubscriberRequest(
                    account="account_value",
                    service_account="service_account_value",
                )

                # Make the request
                response = await client.unregister_subscriber(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.UnregisterSubscriberRequest, dict]):
                The request object. Request Message for
                UnregisterSubscriber.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.types.UnregisterSubscriberResponse:
                Response Message for
                UnregisterSubscriber.

        """
        # Create or coerce a protobuf request object.
        request = service.UnregisterSubscriberRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.unregister_subscriber,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("account", request.account),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_subscribers(
        self,
        request: Union[service.ListSubscribersRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListSubscribersAsyncPager:
        r"""Lists service accounts with subscriber privileges on the Cloud
        Pub/Sub topic created for this Channel Services account.

        Possible error codes:

        -  PERMISSION_DENIED: The reseller account making the request
           and the provided reseller account are different, or the
           impersonated user is not a super admin.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.
        -  NOT_FOUND: The topic resource doesn't exist.
        -  INTERNAL: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.
        -  UNKNOWN: Any non-user error related to a technical issue in
           the backend. Contact Cloud Channel support.

        Return value: A list of service email addresses.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import channel_v1

            async def sample_list_subscribers():
                # Create a client
                client = channel_v1.CloudChannelServiceAsyncClient()

                # Initialize request argument(s)
                request = channel_v1.ListSubscribersRequest(
                    account="account_value",
                )

                # Make the request
                page_result = client.list_subscribers(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.ListSubscribersRequest, dict]):
                The request object. Request Message for ListSubscribers.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListSubscribersAsyncPager:
                Response Message for ListSubscribers.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListSubscribersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_subscribers,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("account", request.account),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListSubscribersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_operations(
        self,
        request: operations_pb2.ListOperationsRequest = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.ListOperationsRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.list_operations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_operation(
        self,
        request: operations_pb2.GetOperationRequest = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.GetOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.get_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a long-running operation.

        This method indicates that the client is no longer interested
        in the operation result. It does not cancel the operation.
        If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.DeleteOperationRequest`):
                The request object. Request message for
                `DeleteOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.DeleteOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.delete_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Starts asynchronous cancellation on a long-running operation.

        The server makes a best effort to cancel the operation, but success
        is not guaranteed.  If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.CancelOperationRequest`):
                The request object. Request message for
                `CancelOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.CancelOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.cancel_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-channel",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("CloudChannelServiceAsyncClient",)
