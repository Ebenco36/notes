from rest_framework.renderers import JSONRenderer
from utils.response import ApiResponse

class ResponseJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Check if the view's response is a custom response
        if renderer_context is not None and 'response' in renderer_context:
            response = renderer_context['response']
            
            if isinstance(response, ApiResponse):
                return super().render(response.data, accepted_media_type, renderer_context)

        # Default handling for non-custom responses
        default_data = {
            'status': 'success',
            'data': data,
        }
        return super().render(default_data, accepted_media_type, renderer_context)
