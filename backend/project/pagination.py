from rest_framework import pagination
from rest_framework.response import Response


class FlutterPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_paginated_response(self, data):

        return Response(
            {
                "page": self.page.number,
                "totalResults": self.page.paginator.count,
                "totalPages": self.page.paginator.num_pages,
                "results": data,
            }
        )
