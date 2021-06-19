Title: [CSS] rem과 em
Date: 2017-04-13
Category: CSS
Tags: css, front
Slug: rem-vs-em
Authors: junshoong
Summary: rem은 root에, em은 해당 요소의 font-size에 비례한다. 그리고 rem이 권장되는 편이다.

css로 디자인을 할때 `margin`이나 `padding`등의 값을 주곤한다. 이럴때 사용하는 단위가 `px`, `em`, `rem`등이 있다.

- `px`은 픽셀을 의미한다. 고정된 크기를 제공한다.
- `em`은 해당 요소의 font-size에 비례하는 값이다.
- `rem`은 html요소(root)의 root font-size에 비례한다. 

그러니까.. `rem`이 html의 전반에 걸쳐서 사용하는 font-size에 영향을 받기 때문에 이를 사용해서 디자인을 하는게 좋다.  `em`을 사용해도 되긴하지만 해당 요소에 특별하게 영향을 줄때만 사용하고 왠만하면 `rem`이 권장된다.

더 자세한 내용은 [tutsplus의 'Rem 그리고 Em, 언제 써야 할까'](https://webdesign.tutsplus.com/ko/tutorials/comprehensive-guide-when-to-use-em-vs-rem--cms-23984)를 참고한다.

