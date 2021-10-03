## Build Environment

### install RVM

[wiki](https://wiki.archlinux.org/title/RVM)

```bash
curl -L get.rvm.io > rvm-install
bash < ./rvm-install
source ~/.bash_profile
```

### install Ruby
```
rvm install 2.7
rvm use 2.7 --default
```

### install jekyll
```
gem install bundler
bundle install
```

### Running Test Server
```
rake build
```
