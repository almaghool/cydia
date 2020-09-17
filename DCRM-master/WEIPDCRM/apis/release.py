# coding=utf-8

"""
DCRM - Darwin Cydia Repository Manager
Copyright (C) 2017  WU Zheng <i.82@me.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from rest_framework import serializers, viewsets
from rest_framework.pagination import LimitOffsetPagination
from WEIPDCRM.models.release import Release


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = '__all__'

    _icon_link = serializers.URLField(source='icon_link', read_only=True)


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    pagination_class = LimitOffsetPagination
