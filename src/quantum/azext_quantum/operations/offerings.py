# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long,redefined-builtin

from knack.util import CLIError
from .._client_factory import cf_offerings
import time


def list_offerings(cmd, location=None):
    """
    Get the list of all provider offerings available on the given location.
    """
    if (not location):
        raise CLIError("A location is required to list offerings available.")
    client = cf_offerings(cmd.cli_ctx)
    return client.list(location_name=location)
