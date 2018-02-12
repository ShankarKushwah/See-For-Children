from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class ChildrenPagination(LimitOffsetPagination):
    default_limit = 6
    max_limit = 100
    limit_query_param = "limit"
    offset_query_param = "offset"
