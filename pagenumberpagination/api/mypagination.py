from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'records'  # client can also decide how much data will display per page ex. /?records=6
    max_page_size = 7  # maximum record to be display, limitation for client
    last_page_strings = 'end'  # ex. ?p=end default is "?=last"
