from rest_framework.pagination import PageNumberPagination


class Jobspagination(PageNumberPagination):
    page_size = 5