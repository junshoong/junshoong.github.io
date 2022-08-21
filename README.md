## Build Environment

### install RVM

[wiki](https://wiki.archlinux.org/title/RVM)
[rvm](https://rvm.io/)

```bash
gpg2 --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
curl -sSL https://get.rvm.io | bash -s stable
```

### install Ruby
```
rvm pkg install openssl
rvm install 2.7 --with-openssl-dir=/home/$(whoami)/.rvm/usr
rvm use 2.7 --default
```

### install bundler and jekyll packages
```
gem install bundler
bundle install
```

### Running Test Server
```
rake build
```
