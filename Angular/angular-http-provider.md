Title: [Angular] no provider for Http 에러
Date: 2017-04-17
Category: Angular
Tags: angular, http
Slug: angular-http-provider
Authors: junshoong
Summary: Uncaught (in promise): No provider for Http! 에러

https://gonehybrid.com/build-your-first-mobile-app-with-ionic-2-angular-2-part-5/
간단한 ionic 예제를 따라하던중 `Uncaught (in promise): No provider for Http!` 로그가 계속 찍힌다.

이건 `app.moduls.ts`파일에 아래와 같은 부분을 추가해주면 된다.

```typescript
import { HttpModule } from '@angular/http';

@NgModule({
    imports: [ ... , HttpModule ],
    ...
})

```
