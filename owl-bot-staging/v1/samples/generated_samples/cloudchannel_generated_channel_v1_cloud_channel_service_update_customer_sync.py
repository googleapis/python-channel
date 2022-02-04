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
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateCustomer
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-channel


# [START cloudchannel_generated_channel_v1_CloudChannelService_UpdateCustomer_sync]
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

    # Handle response
    print(response)

# [END cloudchannel_generated_channel_v1_CloudChannelService_UpdateCustomer_sync]
