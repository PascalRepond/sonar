# -*- coding: utf-8 -*-
#
# Swiss Open Access Repository
# Copyright (C) 2021 RERO
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Loaders.

This file contains sample loaders that can be used to deserialize input data in
an application level data structure. The marshmallow_loader() method can be
parameterized with different schemas for the record metadata. In the provided
json_v1 instance, it uses the OrganisationMetadataSchemaV1, defining the
PersistentIdentifier field.
"""

from __future__ import absolute_import, print_function

from invenio_records_rest.loaders.marshmallow import json_patch_loader, \
    marshmallow_loader

from ..marshmallow import OrganisationMetadataSchemaV1

#: JSON loader using Marshmallow for data validation.
json_v1 = marshmallow_loader(OrganisationMetadataSchemaV1)

__all__ = (
    'json_v1',
)
