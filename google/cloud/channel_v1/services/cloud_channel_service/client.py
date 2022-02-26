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
import os
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.channel_v1.services.cloud_channel_service import pagers
from google.cloud.channel_v1.types import channel_partner_links
from google.cloud.channel_v1.types import common
from google.cloud.channel_v1.types import customers
from google.cloud.channel_v1.types import entitlements
from google.cloud.channel_v1.types import offers
from google.cloud.channel_v1.types import operations
from google.cloud.channel_v1.types import products
from google.cloud.channel_v1.types import service
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.type import postal_address_pb2  # type: ignore
from .transports.base import CloudChannelServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import CloudChannelServiceGrpcTransport
from .transports.grpc_asyncio import CloudChannelServiceGrpcAsyncIOTransport


class CloudChannelServiceClientMeta(type):
    """Metaclass for the CloudChannelService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = (
        OrderedDict()
    )  # type: Dict[str, Type[CloudChannelServiceTransport]]
    _transport_registry["grpc"] = CloudChannelServiceGrpcTransport
    _transport_registry["grpc_asyncio"] = CloudChannelServiceGrpcAsyncIOTransport

    def get_transport_class(
        cls, label: str = None,
    ) -> Type[CloudChannelServiceTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class CloudChannelServiceClient(metaclass=CloudChannelServiceClientMeta):
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

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "cloudchannel.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
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
            CloudChannelServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

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
            CloudChannelServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> CloudChannelServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            CloudChannelServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def channel_partner_link_path(account: str, channel_partner_link: str,) -> str:
        """Returns a fully-qualified channel_partner_link string."""
        return "accounts/{account}/channelPartnerLinks/{channel_partner_link}".format(
            account=account, channel_partner_link=channel_partner_link,
        )

    @staticmethod
    def parse_channel_partner_link_path(path: str) -> Dict[str, str]:
        """Parses a channel_partner_link path into its component segments."""
        m = re.match(
            r"^accounts/(?P<account>.+?)/channelPartnerLinks/(?P<channel_partner_link>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def customer_path(account: str, customer: str,) -> str:
        """Returns a fully-qualified customer string."""
        return "accounts/{account}/customers/{customer}".format(
            account=account, customer=customer,
        )

    @staticmethod
    def parse_customer_path(path: str) -> Dict[str, str]:
        """Parses a customer path into its component segments."""
        m = re.match(r"^accounts/(?P<account>.+?)/customers/(?P<customer>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def entitlement_path(account: str, customer: str, entitlement: str,) -> str:
        """Returns a fully-qualified entitlement string."""
        return "accounts/{account}/customers/{customer}/entitlements/{entitlement}".format(
            account=account, customer=customer, entitlement=entitlement,
        )

    @staticmethod
    def parse_entitlement_path(path: str) -> Dict[str, str]:
        """Parses a entitlement path into its component segments."""
        m = re.match(
            r"^accounts/(?P<account>.+?)/customers/(?P<customer>.+?)/entitlements/(?P<entitlement>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def offer_path(account: str, offer: str,) -> str:
        """Returns a fully-qualified offer string."""
        return "accounts/{account}/offers/{offer}".format(account=account, offer=offer,)

    @staticmethod
    def parse_offer_path(path: str) -> Dict[str, str]:
        """Parses a offer path into its component segments."""
        m = re.match(r"^accounts/(?P<account>.+?)/offers/(?P<offer>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def product_path(product: str,) -> str:
        """Returns a fully-qualified product string."""
        return "products/{product}".format(product=product,)

    @staticmethod
    def parse_product_path(path: str) -> Dict[str, str]:
        """Parses a product path into its component segments."""
        m = re.match(r"^products/(?P<product>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def sku_path(product: str, sku: str,) -> str:
        """Returns a fully-qualified sku string."""
        return "products/{product}/skus/{sku}".format(product=product, sku=sku,)

    @staticmethod
    def parse_sku_path(path: str) -> Dict[str, str]:
        """Parses a sku path into its component segments."""
        m = re.match(r"^products/(?P<product>.+?)/skus/(?P<sku>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(billing_account: str,) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(folder: str,) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(folder=folder,)

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(organization: str,) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(organization=organization,)

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(project: str,) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(project=project,)

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(project: str, location: str,) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project, location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[client_options_lib.ClientOptions] = None
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
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_client_cert not in ("true", "false"):
            raise ValueError(
                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"
            )
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert == "true":
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, CloudChannelServiceTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the cloud channel service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, CloudChannelServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
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
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()

        api_endpoint, client_cert_source_func = self.get_mtls_endpoint_and_cert_source(
            client_options
        )

        api_key_value = getattr(client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError(
                "client_options.api_key and credentials are mutually exclusive"
            )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, CloudChannelServiceTransport):
            # transport is a CloudChannelServiceTransport instance.
            if credentials or client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(
                google.auth._default, "get_api_key_credentials"
            ):
                credentials = google.auth._default.get_api_key_credentials(
                    api_key_value
                )

            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
            )

    def list_customers(
        self,
        request: Union[service.ListCustomersRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListCustomersPager:
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

            from google.cloud import channel_v1

            def sample_list_customers():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ListCustomersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_customers(request=request)

                # Handle the response
                for response in page_result:
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
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListCustomersPager:
                Response message for
                [CloudChannelService.ListCustomers][google.cloud.channel.v1.CloudChannelService.ListCustomers].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListCustomersRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListCustomersRequest):
            request = service.ListCustomersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_customers]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListCustomersPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_customer(
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

            from google.cloud import channel_v1

            def sample_get_customer():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.GetCustomerRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_customer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.channel_v1.types.GetCustomerRequest, dict]):
                The request object. Request message for
                [CloudChannelService.GetCustomer][google.cloud.channel.v1.CloudChannelService.GetCustomer].
            name (str):
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

        # Minor optimization to avoid making a copy if the user passes
        # in a service.GetCustomerRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.GetCustomerRequest):
            request = service.GetCustomerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_customer]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def check_cloud_identity_accounts_exist(
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

            from google.cloud import channel_v1

            def sample_check_cloud_identity_accounts_exist():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.CheckCloudIdentityAccountsExistRequest(
                    parent="parent_value",
                    domain="domain_value",
                )

                # Make the request
                response = client.check_cloud_identity_accounts_exist(request=request)

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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.CheckCloudIdentityAccountsExistRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.CheckCloudIdentityAccountsExistRequest):
            request = service.CheckCloudIdentityAccountsExistRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.check_cloud_identity_accounts_exist
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def create_customer(
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

            from google.cloud import channel_v1

            def sample_create_customer():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                customer = channel_v1.Customer()
                customer.org_display_name = "org_display_name_value"
                customer.domain = "domain_value"

                request = channel_v1.CreateCustomerRequest(
                    parent="parent_value",
                    customer=customer,
                )

                # Make the request
                response = client.create_customer(request=request)

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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.CreateCustomerRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.CreateCustomerRequest):
            request = service.CreateCustomerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_customer]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def update_customer(
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

            from google.cloud import channel_v1

            def sample_update_customer():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                customer = channel_v1.Customer()
                customer.org_display_name = "org_display_name_value"
                customer.domain = "domain_value"

                request = channel_v1.UpdateCustomerRequest(
                    customer=customer,
                )

                # Make the request
                response = client.update_customer(request=request)

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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.UpdateCustomerRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.UpdateCustomerRequest):
            request = service.UpdateCustomerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_customer]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("customer.name", request.customer.name),)
            ),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def delete_customer(
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

            from google.cloud import channel_v1

            def sample_delete_customer():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.DeleteCustomerRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_customer(request=request)

        Args:
            request (Union[google.cloud.channel_v1.types.DeleteCustomerRequest, dict]):
                The request object. Request message for
                [CloudChannelService.DeleteCustomer][google.cloud.channel.v1.CloudChannelService.DeleteCustomer].
            name (str):
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

        # Minor optimization to avoid making a copy if the user passes
        # in a service.DeleteCustomerRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.DeleteCustomerRequest):
            request = service.DeleteCustomerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_customer]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def import_customer(
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

            from google.cloud import channel_v1

            def sample_import_customer():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ImportCustomerRequest(
                    domain="domain_value",
                    parent="parent_value",
                    overwrite_if_exists=True,
                )

                # Make the request
                response = client.import_customer(request=request)

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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ImportCustomerRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ImportCustomerRequest):
            request = service.ImportCustomerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.import_customer]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def provision_cloud_identity(
        self,
        request: Union[service.ProvisionCloudIdentityRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
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

            from google.cloud import channel_v1

            def sample_provision_cloud_identity():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ProvisionCloudIdentityRequest(
                    customer="customer_value",
                )

                # Make the request
                operation = client.provision_cloud_identity(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

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
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Customer` Entity
                representing a customer of a reseller or distributor.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ProvisionCloudIdentityRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ProvisionCloudIdentityRequest):
            request = service.ProvisionCloudIdentityRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.provision_cloud_identity]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("customer", request.customer),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            customers.Customer,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_entitlements(
        self,
        request: Union[service.ListEntitlementsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListEntitlementsPager:
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

            from google.cloud import channel_v1

            def sample_list_entitlements():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ListEntitlementsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_entitlements(request=request)

                # Handle the response
                for response in page_result:
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
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListEntitlementsPager:
                Response message for
                [CloudChannelService.ListEntitlements][google.cloud.channel.v1.CloudChannelService.ListEntitlements].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListEntitlementsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListEntitlementsRequest):
            request = service.ListEntitlementsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_entitlements]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListEntitlementsPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_transferable_skus(
        self,
        request: Union[service.ListTransferableSkusRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTransferableSkusPager:
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

            from google.cloud import channel_v1

            def sample_list_transferable_skus():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ListTransferableSkusRequest(
                    cloud_identity_id="cloud_identity_id_value",
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_transferable_skus(request=request)

                # Handle the response
                for response in page_result:
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
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListTransferableSkusPager:
                Response message for
                [CloudChannelService.ListTransferableSkus][google.cloud.channel.v1.CloudChannelService.ListTransferableSkus].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListTransferableSkusRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListTransferableSkusRequest):
            request = service.ListTransferableSkusRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_transferable_skus]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListTransferableSkusPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_transferable_offers(
        self,
        request: Union[service.ListTransferableOffersRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTransferableOffersPager:
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
           -  The supplied auth token is invalid.
           -  The reseller account making the request is different from
              the reseller account in the query.

        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.

        Return value: List of
        [TransferableOffer][google.cloud.channel.v1.TransferableOffer]
        for the given customer and SKU.


        .. code-block:: python

            from google.cloud import channel_v1

            def sample_list_transferable_offers():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ListTransferableOffersRequest(
                    cloud_identity_id="cloud_identity_id_value",
                    parent="parent_value",
                    sku="sku_value",
                )

                # Make the request
                page_result = client.list_transferable_offers(request=request)

                # Handle the response
                for response in page_result:
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
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListTransferableOffersPager:
                Response message for
                [CloudChannelService.ListTransferableOffers][google.cloud.channel.v1.CloudChannelService.ListTransferableOffers].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListTransferableOffersRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListTransferableOffersRequest):
            request = service.ListTransferableOffersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_transferable_offers]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListTransferableOffersPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_entitlement(
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

            from google.cloud import channel_v1

            def sample_get_entitlement():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.GetEntitlementRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_entitlement(request=request)

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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.GetEntitlementRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.GetEntitlementRequest):
            request = service.GetEntitlementRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_entitlement]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def create_entitlement(
        self,
        request: Union[service.CreateEntitlementRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
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

            from google.cloud import channel_v1

            def sample_create_entitlement():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

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

                response = operation.result()

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
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.CreateEntitlementRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.CreateEntitlementRequest):
            request = service.CreateEntitlementRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_entitlement]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    def change_parameters(
        self,
        request: Union[service.ChangeParametersRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
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

            from google.cloud import channel_v1

            def sample_change_parameters():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ChangeParametersRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.change_parameters(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

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
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ChangeParametersRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ChangeParametersRequest):
            request = service.ChangeParametersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.change_parameters]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    def change_renewal_settings(
        self,
        request: Union[service.ChangeRenewalSettingsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
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

            from google.cloud import channel_v1

            def sample_change_renewal_settings():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ChangeRenewalSettingsRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.change_renewal_settings(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

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
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ChangeRenewalSettingsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ChangeRenewalSettingsRequest):
            request = service.ChangeRenewalSettingsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.change_renewal_settings]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    def change_offer(
        self,
        request: Union[service.ChangeOfferRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
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

            from google.cloud import channel_v1

            def sample_change_offer():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ChangeOfferRequest(
                    name="name_value",
                    offer="offer_value",
                )

                # Make the request
                operation = client.change_offer(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

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
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ChangeOfferRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ChangeOfferRequest):
            request = service.ChangeOfferRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.change_offer]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    def start_paid_service(
        self,
        request: Union[service.StartPaidServiceRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
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

            from google.cloud import channel_v1

            def sample_start_paid_service():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.StartPaidServiceRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.start_paid_service(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

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
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.StartPaidServiceRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.StartPaidServiceRequest):
            request = service.StartPaidServiceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.start_paid_service]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    def suspend_entitlement(
        self,
        request: Union[service.SuspendEntitlementRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
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

            from google.cloud import channel_v1

            def sample_suspend_entitlement():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.SuspendEntitlementRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.suspend_entitlement(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

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
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.SuspendEntitlementRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.SuspendEntitlementRequest):
            request = service.SuspendEntitlementRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.suspend_entitlement]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    def cancel_entitlement(
        self,
        request: Union[service.CancelEntitlementRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
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

            from google.cloud import channel_v1

            def sample_cancel_entitlement():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.CancelEntitlementRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.cancel_entitlement(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

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
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.CancelEntitlementRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.CancelEntitlementRequest):
            request = service.CancelEntitlementRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.cancel_entitlement]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    def activate_entitlement(
        self,
        request: Union[service.ActivateEntitlementRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
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

            from google.cloud import channel_v1

            def sample_activate_entitlement():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ActivateEntitlementRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.activate_entitlement(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

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
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.channel_v1.types.Entitlement` An
                entitlement is a representation of a customer's ability
                to use a service.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ActivateEntitlementRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ActivateEntitlementRequest):
            request = service.ActivateEntitlementRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.activate_entitlement]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            entitlements.Entitlement,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    def transfer_entitlements(
        self,
        request: Union[service.TransferEntitlementsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
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

            from google.cloud import channel_v1

            def sample_transfer_entitlements():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

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

                response = operation.result()

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
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.channel_v1.types.TransferEntitlementsResponse` Response message for [CloudChannelService.TransferEntitlements][google.cloud.channel.v1.CloudChannelService.TransferEntitlements].
                   This is put in the response field of
                   google.longrunning.Operation.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.TransferEntitlementsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.TransferEntitlementsRequest):
            request = service.TransferEntitlementsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.transfer_entitlements]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            service.TransferEntitlementsResponse,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    def transfer_entitlements_to_google(
        self,
        request: Union[service.TransferEntitlementsToGoogleRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
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

            from google.cloud import channel_v1

            def sample_transfer_entitlements_to_google():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

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

                response = operation.result()

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
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.TransferEntitlementsToGoogleRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.TransferEntitlementsToGoogleRequest):
            request = service.TransferEntitlementsToGoogleRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.transfer_entitlements_to_google
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=operations.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_channel_partner_links(
        self,
        request: Union[service.ListChannelPartnerLinksRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListChannelPartnerLinksPager:
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

            from google.cloud import channel_v1

            def sample_list_channel_partner_links():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ListChannelPartnerLinksRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_channel_partner_links(request=request)

                # Handle the response
                for response in page_result:
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
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListChannelPartnerLinksPager:
                Response message for
                [CloudChannelService.ListChannelPartnerLinks][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerLinks].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListChannelPartnerLinksRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListChannelPartnerLinksRequest):
            request = service.ListChannelPartnerLinksRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_channel_partner_links
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListChannelPartnerLinksPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_channel_partner_link(
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

            from google.cloud import channel_v1

            def sample_get_channel_partner_link():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.GetChannelPartnerLinkRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_channel_partner_link(request=request)

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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.GetChannelPartnerLinkRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.GetChannelPartnerLinkRequest):
            request = service.GetChannelPartnerLinkRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_channel_partner_link]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def create_channel_partner_link(
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

            from google.cloud import channel_v1

            def sample_create_channel_partner_link():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                channel_partner_link = channel_v1.ChannelPartnerLink()
                channel_partner_link.reseller_cloud_identity_id = "reseller_cloud_identity_id_value"
                channel_partner_link.link_state = "SUSPENDED"

                request = channel_v1.CreateChannelPartnerLinkRequest(
                    parent="parent_value",
                    channel_partner_link=channel_partner_link,
                )

                # Make the request
                response = client.create_channel_partner_link(request=request)

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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.CreateChannelPartnerLinkRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.CreateChannelPartnerLinkRequest):
            request = service.CreateChannelPartnerLinkRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_channel_partner_link
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def update_channel_partner_link(
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

            from google.cloud import channel_v1

            def sample_update_channel_partner_link():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                channel_partner_link = channel_v1.ChannelPartnerLink()
                channel_partner_link.reseller_cloud_identity_id = "reseller_cloud_identity_id_value"
                channel_partner_link.link_state = "SUSPENDED"

                request = channel_v1.UpdateChannelPartnerLinkRequest(
                    name="name_value",
                    channel_partner_link=channel_partner_link,
                )

                # Make the request
                response = client.update_channel_partner_link(request=request)

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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.UpdateChannelPartnerLinkRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.UpdateChannelPartnerLinkRequest):
            request = service.UpdateChannelPartnerLinkRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_channel_partner_link
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def lookup_offer(
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

            from google.cloud import channel_v1

            def sample_lookup_offer():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.LookupOfferRequest(
                    entitlement="entitlement_value",
                )

                # Make the request
                response = client.lookup_offer(request=request)

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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.LookupOfferRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.LookupOfferRequest):
            request = service.LookupOfferRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.lookup_offer]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("entitlement", request.entitlement),)
            ),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_products(
        self,
        request: Union[service.ListProductsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListProductsPager:
        r"""Lists the Products the reseller is authorized to sell.

        Possible error codes:

        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.


        .. code-block:: python

            from google.cloud import channel_v1

            def sample_list_products():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ListProductsRequest(
                    account="account_value",
                )

                # Make the request
                page_result = client.list_products(request=request)

                # Handle the response
                for response in page_result:
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
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListProductsPager:
                Response message for ListProducts.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListProductsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListProductsRequest):
            request = service.ListProductsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_products]

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListProductsPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_skus(
        self,
        request: Union[service.ListSkusRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListSkusPager:
        r"""Lists the SKUs for a product the reseller is authorized to sell.

        Possible error codes:

        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.


        .. code-block:: python

            from google.cloud import channel_v1

            def sample_list_skus():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ListSkusRequest(
                    parent="parent_value",
                    account="account_value",
                )

                # Make the request
                page_result = client.list_skus(request=request)

                # Handle the response
                for response in page_result:
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
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListSkusPager:
                Response message for ListSkus.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListSkusRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListSkusRequest):
            request = service.ListSkusRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_skus]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListSkusPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_offers(
        self,
        request: Union[service.ListOffersRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListOffersPager:
        r"""Lists the Offers the reseller can sell.

        Possible error codes:

        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.


        .. code-block:: python

            from google.cloud import channel_v1

            def sample_list_offers():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ListOffersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_offers(request=request)

                # Handle the response
                for response in page_result:
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
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListOffersPager:
                Response message for ListOffers.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListOffersRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListOffersRequest):
            request = service.ListOffersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_offers]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListOffersPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_purchasable_skus(
        self,
        request: Union[service.ListPurchasableSkusRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPurchasableSkusPager:
        r"""Lists the following:

        -  SKUs that you can purchase for a customer
        -  SKUs that you can upgrade or downgrade for an entitlement.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller.
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.


        .. code-block:: python

            from google.cloud import channel_v1

            def sample_list_purchasable_skus():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

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
                for response in page_result:
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
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListPurchasableSkusPager:
                Response message for
                ListPurchasableSkus.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListPurchasableSkusRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListPurchasableSkusRequest):
            request = service.ListPurchasableSkusRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_purchasable_skus]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("customer", request.customer),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListPurchasableSkusPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_purchasable_offers(
        self,
        request: Union[service.ListPurchasableOffersRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPurchasableOffersPager:
        r"""Lists the following:

        -  Offers that you can purchase for a customer.
        -  Offers that you can change for an entitlement.

        Possible error codes:

        -  PERMISSION_DENIED: The customer doesn't belong to the
           reseller
        -  INVALID_ARGUMENT: Required request parameters are missing or
           invalid.


        .. code-block:: python

            from google.cloud import channel_v1

            def sample_list_purchasable_offers():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

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
                for response in page_result:
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
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListPurchasableOffersPager:
                Response message for
                ListPurchasableOffers.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListPurchasableOffersRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListPurchasableOffersRequest):
            request = service.ListPurchasableOffersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_purchasable_offers]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("customer", request.customer),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListPurchasableOffersPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def register_subscriber(
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

            from google.cloud import channel_v1

            def sample_register_subscriber():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.RegisterSubscriberRequest(
                    account="account_value",
                    service_account="service_account_value",
                )

                # Make the request
                response = client.register_subscriber(request=request)

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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.RegisterSubscriberRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.RegisterSubscriberRequest):
            request = service.RegisterSubscriberRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.register_subscriber]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("account", request.account),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def unregister_subscriber(
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

            from google.cloud import channel_v1

            def sample_unregister_subscriber():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.UnregisterSubscriberRequest(
                    account="account_value",
                    service_account="service_account_value",
                )

                # Make the request
                response = client.unregister_subscriber(request=request)

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
        # Minor optimization to avoid making a copy if the user passes
        # in a service.UnregisterSubscriberRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.UnregisterSubscriberRequest):
            request = service.UnregisterSubscriberRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.unregister_subscriber]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("account", request.account),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_subscribers(
        self,
        request: Union[service.ListSubscribersRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListSubscribersPager:
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

            from google.cloud import channel_v1

            def sample_list_subscribers():
                # Create a client
                client = channel_v1.CloudChannelServiceClient()

                # Initialize request argument(s)
                request = channel_v1.ListSubscribersRequest(
                    account="account_value",
                )

                # Make the request
                page_result = client.list_subscribers(request=request)

                # Handle the response
                for response in page_result:
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
            google.cloud.channel_v1.services.cloud_channel_service.pagers.ListSubscribersPager:
                Response Message for ListSubscribers.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a service.ListSubscribersRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, service.ListSubscribersRequest):
            request = service.ListSubscribersRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_subscribers]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("account", request.account),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListSubscribersPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-channel",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("CloudChannelServiceClient",)
