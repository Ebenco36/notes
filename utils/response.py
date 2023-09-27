from rest_framework.response import Response

class ApiResponse(Response):
    def __init__(self, data=None, status=None, message=None, success=True, **kwargs):
        content = {
            "success": success,
            "message": message,
            "data": data,
        }
        super().__init__(data=content, status=status, **kwargs)

    @classmethod
    def success(cls, data=None, message="Success", status=200):
        return cls(data=data, message=message, status=status)

    @classmethod
    def error(cls, message="Error", status=400, data=None):
        return cls(data=data, message=message, status=status, success=False)
