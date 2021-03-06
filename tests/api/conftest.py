# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Graz University of Technology.
#
# invenio-records-lom is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""

import uuid

import pytest
from invenio_accounts.testutils import create_test_user
from invenio_app.factory import create_api
from invenio_pidstore.models import PersistentIdentifier, PIDStatus

from invenio_records_lom.indexer import LomRecordIndexer
from invenio_records_lom.proxies import Lom


@pytest.fixture(scope="module")
def create_app(instance_path):
    """Application factory fixture."""
    return create_api
