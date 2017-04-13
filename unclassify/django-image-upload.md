Title: Django ImageField 업로드문제
Date: 2016-09-09
Modified:
Category:
Tags:
Slug: django-image-upload
Authors: junshoong
Summary:


context
---
title: "Django ImageField 업로드문제"
category: post
tags: django, python
---
Django의 ImageFile를 만들어서 서버에 업로드를 하는데 계속해서 아래와 같은 메세지가 나타났다.  

> This field is required.

admin 페이지에서 업로드할때는 문제가 없는데 직접 구현해둔 곳에서만 문제가 발생한다. 여러가지를 추측해봤는데 결국 Templates 문제였다. 여기서 참고를 위해 코드 일부를 첨부한다.
일단 `models.py`를 보자.  

{% highlight python %}
class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='%Y/%m/%d')
{% endhighlight %}

`forms.py` 는 아주 간단하다.

{% highlight python %}
from django.forms import ModelForm
from .models import Image

class AddForm(ModelForm):
    class Meta:
        model = Image
{% endhighlight %}

`urls.py`를 통해 연결해준다.  

{% highlight python %}
...

urlpatterns = [
    url(r'^add/$', add_image, name='add'),
]
{% endhighlight %}

`views.py`에서 자세한 내용을 올려준다.
{% highlight python %}
from django.shortcuts import render, redirect
from .models import Image
from .forms import AddForm

def add_image(request):
    if request.method == "POST":
        form = AddForm(request.POST, request.FILES)
    
        if form.is_valid():
            new_image = form.save()
            return redirect('/add/')
    else:
        form = AddForm()
    
    return render(request, 'add.html', {'form': form})
{% endhighlight %}

마지막으로 template을 보자 `add.html` 이다.  

{% highlight html %}
{% raw %}
...
<form method="POST" action="{% url 'add' %}" id="add_form" enctype="multipart/form-data">
    {{ form.as_p }}
    {% csrf_token %}
    <button type="submit" form="add_form">Add</button>
</form>
...
{% endraw %}
{% endhighlight %}

> This field is required.
>
> - 필수 항목입니다.

계속 이 메세지가 나왔던건 `enctype="multipart/form-data"`를 누락해서 그런 것이었다.


## 참고자료
- [djangoproject forms](https://docs.djangoproject.com/en/1.10/ref/forms/api/#binding-uploaded-files-to-a-form)
- [Image field didn't get saved, raises error 'This field is required'](http://stackoverflow.com/questions/31745990/image-field-didnt-get-saved-raises-error-this-field-is-required)
- [Django Image Upload Always Fails, form is never valid](http://stackoverflow.com/questions/30138370/django-image-upload-always-fails-form-is-never-valid)
- [날로 먹는 Django 웹프레임워크 강좌 - 7](http://blog.hannal.com/2015/05/start_with_django_webframework_07/)
