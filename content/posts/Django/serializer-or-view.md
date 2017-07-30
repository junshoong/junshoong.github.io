Title: [Django] serializer의 구현
Date: 2017-04-20
Category: Django
Tags: django, drf
Slug: serializer-or-view
Authors: junshoong
Summary: DRF에서 create를 구현하는 경우 `ViewSet`의 `perform_create`를 사용하면 Serializer의 create를 돌지 않는다.


DRF에서 create를 구현하는 경우 `ViewSet`의 `perform_create`를 사용하면 `Serializer`의 `create`를 돌지 않는다.

어떤 식으로 처리하는게 더 나은지는 모르겠지만.. `request`를 처리할 필요가 있으면 view에서 구현해주고, 입력된 데이터인 `validated_data`를 처리할 필요가 있으면 serializer에서 구현해주는게 좋은 것 같다. 
