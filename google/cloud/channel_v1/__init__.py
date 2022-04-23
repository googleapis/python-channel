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

from .services.cloud_channel_service import (
    CloudChannelServiceAsyncClient,
    CloudChannelServiceClient,
)
from .types.channel_partner_links import (
    ChannelPartnerLink,
    ChannelPartnerLinkState,
    ChannelPartnerLinkView,
)
from .types.common import AdminUser, CloudIdentityInfo, EduData, Value
from .types.customers import ContactInfo, Customer
from .types.entitlements import (
    AssociationInfo,
    CommitmentSettings,
    Entitlement,
    Parameter,
    ProvisionedService,
    RenewalSettings,
    TransferableSku,
    TransferEligibility,
    TrialSettings,
)
from .types.offers import (
    Constraints,
    CustomerConstraints,
    Offer,
    ParameterDefinition,
    PaymentPlan,
    PaymentType,
    Period,
    PeriodType,
    Plan,
    Price,
    PriceByResource,
    PricePhase,
    PriceTier,
    PromotionalOrderType,
    ResourceType,
)
from .types.operations import OperationMetadata
from .types.products import MarketingInfo, Media, MediaType, Product, Sku
from .types.repricing import (
    ChannelPartnerRepricingConfig,
    CustomerRepricingConfig,
    PercentageAdjustment,
    RebillingBasis,
    RepricingAdjustment,
    RepricingConfig,
)
from .types.service import (
    ActivateEntitlementRequest,
    CancelEntitlementRequest,
    ChangeOfferRequest,
    ChangeParametersRequest,
    ChangeRenewalSettingsRequest,
    CheckCloudIdentityAccountsExistRequest,
    CheckCloudIdentityAccountsExistResponse,
    CloudIdentityCustomerAccount,
    CreateChannelPartnerLinkRequest,
    CreateChannelPartnerRepricingConfigRequest,
    CreateCustomerRepricingConfigRequest,
    CreateCustomerRequest,
    CreateEntitlementRequest,
    DeleteChannelPartnerRepricingConfigRequest,
    DeleteCustomerRepricingConfigRequest,
    DeleteCustomerRequest,
    GetChannelPartnerLinkRequest,
    GetChannelPartnerRepricingConfigRequest,
    GetCustomerRepricingConfigRequest,
    GetCustomerRequest,
    GetEntitlementRequest,
    ImportCustomerRequest,
    ListChannelPartnerLinksRequest,
    ListChannelPartnerLinksResponse,
    ListChannelPartnerRepricingConfigsRequest,
    ListChannelPartnerRepricingConfigsResponse,
    ListCustomerRepricingConfigsRequest,
    ListCustomerRepricingConfigsResponse,
    ListCustomersRequest,
    ListCustomersResponse,
    ListEntitlementsRequest,
    ListEntitlementsResponse,
    ListOffersRequest,
    ListOffersResponse,
    ListProductsRequest,
    ListProductsResponse,
    ListPurchasableOffersRequest,
    ListPurchasableOffersResponse,
    ListPurchasableSkusRequest,
    ListPurchasableSkusResponse,
    ListSkusRequest,
    ListSkusResponse,
    ListSubscribersRequest,
    ListSubscribersResponse,
    ListTransferableOffersRequest,
    ListTransferableOffersResponse,
    ListTransferableSkusRequest,
    ListTransferableSkusResponse,
    LookupOfferRequest,
    ProvisionCloudIdentityRequest,
    PurchasableOffer,
    PurchasableSku,
    RegisterSubscriberRequest,
    RegisterSubscriberResponse,
    StartPaidServiceRequest,
    SuspendEntitlementRequest,
    TransferableOffer,
    TransferEntitlementsRequest,
    TransferEntitlementsResponse,
    TransferEntitlementsToGoogleRequest,
    UnregisterSubscriberRequest,
    UnregisterSubscriberResponse,
    UpdateChannelPartnerLinkRequest,
    UpdateChannelPartnerRepricingConfigRequest,
    UpdateCustomerRepricingConfigRequest,
    UpdateCustomerRequest,
)
from .types.subscriber_event import CustomerEvent, EntitlementEvent, SubscriberEvent

__all__ = (
    "CloudChannelServiceAsyncClient",
    "ActivateEntitlementRequest",
    "AdminUser",
    "AssociationInfo",
    "CancelEntitlementRequest",
    "ChangeOfferRequest",
    "ChangeParametersRequest",
    "ChangeRenewalSettingsRequest",
    "ChannelPartnerLink",
    "ChannelPartnerLinkState",
    "ChannelPartnerLinkView",
    "ChannelPartnerRepricingConfig",
    "CheckCloudIdentityAccountsExistRequest",
    "CheckCloudIdentityAccountsExistResponse",
    "CloudChannelServiceClient",
    "CloudIdentityCustomerAccount",
    "CloudIdentityInfo",
    "CommitmentSettings",
    "Constraints",
    "ContactInfo",
    "CreateChannelPartnerLinkRequest",
    "CreateChannelPartnerRepricingConfigRequest",
    "CreateCustomerRepricingConfigRequest",
    "CreateCustomerRequest",
    "CreateEntitlementRequest",
    "Customer",
    "CustomerConstraints",
    "CustomerEvent",
    "CustomerRepricingConfig",
    "DeleteChannelPartnerRepricingConfigRequest",
    "DeleteCustomerRepricingConfigRequest",
    "DeleteCustomerRequest",
    "EduData",
    "Entitlement",
    "EntitlementEvent",
    "GetChannelPartnerLinkRequest",
    "GetChannelPartnerRepricingConfigRequest",
    "GetCustomerRepricingConfigRequest",
    "GetCustomerRequest",
    "GetEntitlementRequest",
    "ImportCustomerRequest",
    "ListChannelPartnerLinksRequest",
    "ListChannelPartnerLinksResponse",
    "ListChannelPartnerRepricingConfigsRequest",
    "ListChannelPartnerRepricingConfigsResponse",
    "ListCustomerRepricingConfigsRequest",
    "ListCustomerRepricingConfigsResponse",
    "ListCustomersRequest",
    "ListCustomersResponse",
    "ListEntitlementsRequest",
    "ListEntitlementsResponse",
    "ListOffersRequest",
    "ListOffersResponse",
    "ListProductsRequest",
    "ListProductsResponse",
    "ListPurchasableOffersRequest",
    "ListPurchasableOffersResponse",
    "ListPurchasableSkusRequest",
    "ListPurchasableSkusResponse",
    "ListSkusRequest",
    "ListSkusResponse",
    "ListSubscribersRequest",
    "ListSubscribersResponse",
    "ListTransferableOffersRequest",
    "ListTransferableOffersResponse",
    "ListTransferableSkusRequest",
    "ListTransferableSkusResponse",
    "LookupOfferRequest",
    "MarketingInfo",
    "Media",
    "MediaType",
    "Offer",
    "OperationMetadata",
    "Parameter",
    "ParameterDefinition",
    "PaymentPlan",
    "PaymentType",
    "PercentageAdjustment",
    "Period",
    "PeriodType",
    "Plan",
    "Price",
    "PriceByResource",
    "PricePhase",
    "PriceTier",
    "Product",
    "PromotionalOrderType",
    "ProvisionCloudIdentityRequest",
    "ProvisionedService",
    "PurchasableOffer",
    "PurchasableSku",
    "RebillingBasis",
    "RegisterSubscriberRequest",
    "RegisterSubscriberResponse",
    "RenewalSettings",
    "RepricingAdjustment",
    "RepricingConfig",
    "ResourceType",
    "Sku",
    "StartPaidServiceRequest",
    "SubscriberEvent",
    "SuspendEntitlementRequest",
    "TransferEligibility",
    "TransferEntitlementsRequest",
    "TransferEntitlementsResponse",
    "TransferEntitlementsToGoogleRequest",
    "TransferableOffer",
    "TransferableSku",
    "TrialSettings",
    "UnregisterSubscriberRequest",
    "UnregisterSubscriberResponse",
    "UpdateChannelPartnerLinkRequest",
    "UpdateChannelPartnerRepricingConfigRequest",
    "UpdateCustomerRepricingConfigRequest",
    "UpdateCustomerRequest",
    "Value",
)
