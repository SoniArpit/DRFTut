from rest_framework.pagination import CursorPagination


class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'  # by default 'created' field, by default finding
    cursor_query_param = 'cur'
