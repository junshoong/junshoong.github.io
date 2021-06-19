Title: [Django] restframework에서 image 제공하기
Date: 2017-04-16
Modified: 2017-04-17
Category: Django
Tags: django, rest
Slug: django-restframework-image-field
Authors: junshoong
Summary: DRF에서 image field를 serving 해보자.

drf에서 이미지를 제공하기 위해서는 이미지 Renderer가 별도로 필요하다. 이는 JSONRenderer 등과는 다르게 직접 만들어줘야 한다. 

__/myapp/views.py__
```python
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response

class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpg'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data

class TestViewSet(viewsets.ModelViewSet):
    
    ...

    @detail_route(renderer_classes=[JPEGRenderer])
    def image(self, request, *args, **kwargs):
        obj_name = self.get_object()
        return Response(obj_name.image)
```

이렇게 제공하면 url끝에 ~/image/ 경로로 이미지에 접근할 수 있다.
그런데 url의 정보는 그대로인것 같은데 이건 serialize에서 수정해주면 될 것같다.

_/myapp/serializers.py_
```python
class TestSerializer(serializer.HyperlinkedModelSerializer):
    image = serializers.HyperlinkedIdentityField(view_name='test-image', format='html')
    ...
```

이런 식으로 제공할 수 있다.
