# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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

import abc
import typing
import pkg_resources

from google import auth  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1    # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials  # type: ignore

from google.cloud.channel_v1.types import channel_partner_links
from google.cloud.channel_v1.types import customers
from google.cloud.channel_v1.types import entitlements
from google.cloud.channel_v1.types import service
from google.longrunning import operations_pb2 as operations  # type: ignore
from google.protobuf import empty_pb2 as empty  # type: ignore


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'google-cloud-channel',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()

class CloudChannelServiceTransport(abc.ABC):
    """Abstract transport class for CloudChannelService."""

    AUTH_SCOPES = (
        'https://www.googleapis.com/auth/apps.order',
    )

    def __init__(
            self, *,
            host: str = 'cloudchannel.googleapis.com',
            credentials: credentials.Credentials = None,
            credentials_file: typing.Optional[str] = None,
            scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
            quota_project_id: typing.Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scope (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
        self._host = host

        # Save the scopes.
        self._scopes = scopes or self.AUTH_SCOPES

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")

        if credentials_file is not None:
            credentials, _ = auth.load_credentials_from_file(
                                credentials_file,
                                scopes=self._scopes,
                                quota_project_id=quota_project_id
                            )

        elif credentials is None:
            credentials, _ = auth.default(scopes=self._scopes, quota_project_id=quota_project_id)

        # Save the credentials.
        self._credentials = credentials

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_customers: gapic_v1.method.wrap_method(
                self.list_customers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_customer: gapic_v1.method.wrap_method(
                self.get_customer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.check_cloud_identity_accounts_exist: gapic_v1.method.wrap_method(
                self.check_cloud_identity_accounts_exist,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_customer: gapic_v1.method.wrap_method(
                self.create_customer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_customer: gapic_v1.method.wrap_method(
                self.update_customer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_customer: gapic_v1.method.wrap_method(
                self.delete_customer,
                default_timeout=None,
                client_info=client_info,
            ),
            self.provision_cloud_identity: gapic_v1.method.wrap_method(
                self.provision_cloud_identity,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_entitlements: gapic_v1.method.wrap_method(
                self.list_entitlements,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_transferable_skus: gapic_v1.method.wrap_method(
                self.list_transferable_skus,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_transferable_offers: gapic_v1.method.wrap_method(
                self.list_transferable_offers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_entitlement: gapic_v1.method.wrap_method(
                self.get_entitlement,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_entitlement: gapic_v1.method.wrap_method(
                self.create_entitlement,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.change_parameters: gapic_v1.method.wrap_method(
                self.change_parameters,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.change_renewal_settings: gapic_v1.method.wrap_method(
                self.change_renewal_settings,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.change_offer: gapic_v1.method.wrap_method(
                self.change_offer,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.start_paid_service: gapic_v1.method.wrap_method(
                self.start_paid_service,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.suspend_entitlement: gapic_v1.method.wrap_method(
                self.suspend_entitlement,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.cancel_entitlement: gapic_v1.method.wrap_method(
                self.cancel_entitlement,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.activate_entitlement: gapic_v1.method.wrap_method(
                self.activate_entitlement,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.transfer_entitlements: gapic_v1.method.wrap_method(
                self.transfer_entitlements,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.transfer_entitlements_to_google: gapic_v1.method.wrap_method(
                self.transfer_entitlements_to_google,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_channel_partner_links: gapic_v1.method.wrap_method(
                self.list_channel_partner_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_channel_partner_link: gapic_v1.method.wrap_method(
                self.get_channel_partner_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_channel_partner_link: gapic_v1.method.wrap_method(
                self.create_channel_partner_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_channel_partner_link: gapic_v1.method.wrap_method(
                self.update_channel_partner_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_products: gapic_v1.method.wrap_method(
                self.list_products,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_skus: gapic_v1.method.wrap_method(
                self.list_skus,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_offers: gapic_v1.method.wrap_method(
                self.list_offers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_purchasable_skus: gapic_v1.method.wrap_method(
                self.list_purchasable_skus,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_purchasable_offers: gapic_v1.method.wrap_method(
                self.list_purchasable_offers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.register_subscriber: gapic_v1.method.wrap_method(
                self.register_subscriber,
                default_timeout=None,
                client_info=client_info,
            ),
            self.unregister_subscriber: gapic_v1.method.wrap_method(
                self.unregister_subscriber,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_subscribers: gapic_v1.method.wrap_method(
                self.list_subscribers,
                default_timeout=None,
                client_info=client_info,
            ),

        }

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_customers(self) -> typing.Callable[
            [service.ListCustomersRequest],
            typing.Union[
                service.ListCustomersResponse,
                typing.Awaitable[service.ListCustomersResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_customer(self) -> typing.Callable[
            [service.GetCustomerRequest],
            typing.Union[
                customers.Customer,
                typing.Awaitable[customers.Customer]
            ]]:
        raise NotImplementedError()

    @property
    def check_cloud_identity_accounts_exist(self) -> typing.Callable[
            [service.CheckCloudIdentityAccountsExistRequest],
            typing.Union[
                service.CheckCloudIdentityAccountsExistResponse,
                typing.Awaitable[service.CheckCloudIdentityAccountsExistResponse]
            ]]:
        raise NotImplementedError()

    @property
    def create_customer(self) -> typing.Callable[
            [service.CreateCustomerRequest],
            typing.Union[
                customers.Customer,
                typing.Awaitable[customers.Customer]
            ]]:
        raise NotImplementedError()

    @property
    def update_customer(self) -> typing.Callable[
            [service.UpdateCustomerRequest],
            typing.Union[
                customers.Customer,
                typing.Awaitable[customers.Customer]
            ]]:
        raise NotImplementedError()

    @property
    def delete_customer(self) -> typing.Callable[
            [service.DeleteCustomerRequest],
            typing.Union[
                empty.Empty,
                typing.Awaitable[empty.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def provision_cloud_identity(self) -> typing.Callable[
            [service.ProvisionCloudIdentityRequest],
            typing.Union[
                operations.Operation,
                typing.Awaitable[operations.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def list_entitlements(self) -> typing.Callable[
            [service.ListEntitlementsRequest],
            typing.Union[
                service.ListEntitlementsResponse,
                typing.Awaitable[service.ListEntitlementsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def list_transferable_skus(self) -> typing.Callable[
            [service.ListTransferableSkusRequest],
            typing.Union[
                service.ListTransferableSkusResponse,
                typing.Awaitable[service.ListTransferableSkusResponse]
            ]]:
        raise NotImplementedError()

    @property
    def list_transferable_offers(self) -> typing.Callable[
            [service.ListTransferableOffersRequest],
            typing.Union[
                service.ListTransferableOffersResponse,
                typing.Awaitable[service.ListTransferableOffersResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_entitlement(self) -> typing.Callable[
            [service.GetEntitlementRequest],
            typing.Union[
                entitlements.Entitlement,
                typing.Awaitable[entitlements.Entitlement]
            ]]:
        raise NotImplementedError()

    @property
    def create_entitlement(self) -> typing.Callable[
            [service.CreateEntitlementRequest],
            typing.Union[
                operations.Operation,
                typing.Awaitable[operations.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def change_parameters(self) -> typing.Callable[
            [service.ChangeParametersRequest],
            typing.Union[
                operations.Operation,
                typing.Awaitable[operations.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def change_renewal_settings(self) -> typing.Callable[
            [service.ChangeRenewalSettingsRequest],
            typing.Union[
                operations.Operation,
                typing.Awaitable[operations.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def change_offer(self) -> typing.Callable[
            [service.ChangeOfferRequest],
            typing.Union[
                operations.Operation,
                typing.Awaitable[operations.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def start_paid_service(self) -> typing.Callable[
            [service.StartPaidServiceRequest],
            typing.Union[
                operations.Operation,
                typing.Awaitable[operations.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def suspend_entitlement(self) -> typing.Callable[
            [service.SuspendEntitlementRequest],
            typing.Union[
                operations.Operation,
                typing.Awaitable[operations.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def cancel_entitlement(self) -> typing.Callable[
            [service.CancelEntitlementRequest],
            typing.Union[
                operations.Operation,
                typing.Awaitable[operations.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def activate_entitlement(self) -> typing.Callable[
            [service.ActivateEntitlementRequest],
            typing.Union[
                operations.Operation,
                typing.Awaitable[operations.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def transfer_entitlements(self) -> typing.Callable[
            [service.TransferEntitlementsRequest],
            typing.Union[
                operations.Operation,
                typing.Awaitable[operations.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def transfer_entitlements_to_google(self) -> typing.Callable[
            [service.TransferEntitlementsToGoogleRequest],
            typing.Union[
                operations.Operation,
                typing.Awaitable[operations.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def list_channel_partner_links(self) -> typing.Callable[
            [service.ListChannelPartnerLinksRequest],
            typing.Union[
                service.ListChannelPartnerLinksResponse,
                typing.Awaitable[service.ListChannelPartnerLinksResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_channel_partner_link(self) -> typing.Callable[
            [service.GetChannelPartnerLinkRequest],
            typing.Union[
                channel_partner_links.ChannelPartnerLink,
                typing.Awaitable[channel_partner_links.ChannelPartnerLink]
            ]]:
        raise NotImplementedError()

    @property
    def create_channel_partner_link(self) -> typing.Callable[
            [service.CreateChannelPartnerLinkRequest],
            typing.Union[
                channel_partner_links.ChannelPartnerLink,
                typing.Awaitable[channel_partner_links.ChannelPartnerLink]
            ]]:
        raise NotImplementedError()

    @property
    def update_channel_partner_link(self) -> typing.Callable[
            [service.UpdateChannelPartnerLinkRequest],
            typing.Union[
                channel_partner_links.ChannelPartnerLink,
                typing.Awaitable[channel_partner_links.ChannelPartnerLink]
            ]]:
        raise NotImplementedError()

    @property
    def list_products(self) -> typing.Callable[
            [service.ListProductsRequest],
            typing.Union[
                service.ListProductsResponse,
                typing.Awaitable[service.ListProductsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def list_skus(self) -> typing.Callable[
            [service.ListSkusRequest],
            typing.Union[
                service.ListSkusResponse,
                typing.Awaitable[service.ListSkusResponse]
            ]]:
        raise NotImplementedError()

    @property
    def list_offers(self) -> typing.Callable[
            [service.ListOffersRequest],
            typing.Union[
                service.ListOffersResponse,
                typing.Awaitable[service.ListOffersResponse]
            ]]:
        raise NotImplementedError()

    @property
    def list_purchasable_skus(self) -> typing.Callable[
            [service.ListPurchasableSkusRequest],
            typing.Union[
                service.ListPurchasableSkusResponse,
                typing.Awaitable[service.ListPurchasableSkusResponse]
            ]]:
        raise NotImplementedError()

    @property
    def list_purchasable_offers(self) -> typing.Callable[
            [service.ListPurchasableOffersRequest],
            typing.Union[
                service.ListPurchasableOffersResponse,
                typing.Awaitable[service.ListPurchasableOffersResponse]
            ]]:
        raise NotImplementedError()

    @property
    def register_subscriber(self) -> typing.Callable[
            [service.RegisterSubscriberRequest],
            typing.Union[
                service.RegisterSubscriberResponse,
                typing.Awaitable[service.RegisterSubscriberResponse]
            ]]:
        raise NotImplementedError()

    @property
    def unregister_subscriber(self) -> typing.Callable[
            [service.UnregisterSubscriberRequest],
            typing.Union[
                service.UnregisterSubscriberResponse,
                typing.Awaitable[service.UnregisterSubscriberResponse]
            ]]:
        raise NotImplementedError()

    @property
    def list_subscribers(self) -> typing.Callable[
            [service.ListSubscribersRequest],
            typing.Union[
                service.ListSubscribersResponse,
                typing.Awaitable[service.ListSubscribersResponse]
            ]]:
        raise NotImplementedError()


__all__ = (
    'CloudChannelServiceTransport',
)