Title: [Docker] Data Volume을 사용해서 데이터 지속하기
Date: 2017-04-21
Category: Docker
Tags: docker, data
Slug: persist-data-with-data-volume
Authors: junshoong

docker와 git-hook을 사용해서 어느정도 프로세스를 자동화하고 있다.
하지만 docker container를 부수고 다시 build 해서 돌리면 내부 데이터가 날아간다. DB의 경우는 `--link` 옵션을 이용해서 유지하지만 실제로 upload한 image와 같은 file들의 경우는 컨테이너와 함께 지워진다.

Data Volume을 사용해서 해결해보자.

```bash
docker create -v /srv/media --name data-store ubuntu /bin/true
```

이렇게하면 ubuntu 이미지를 기반으로한 Data Volume이 하나 생긴다.
이때 공유된 디렉터리인 `/srv/media` 는 다른 컨테이너에 붙여서 사용할 수 있다.

```bash
sudo docker run --name possster --volumes-from media-store -d project
```

지웠다가 다시 만들어서 run해도 동일한 상태를 확인할 수 있다.
또한 여러 컨테이너들과 같은 Data Volume을 공유할 수도 있다.

아래에서 좀 더 다양한 정보를 확인할 수 있다.
- [docker 공식문서 - Manage data in containers](https://docs.docker.com/engine/tutorials/dockervolumes/)
- [Tricks of the Trades - Data volumes and Data Containers](http://www.tricksofthetrades.net/2016/03/14/docker-data-volumes/)
- [DigitalOcean - How To Work with Docker Data Volumes on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-work-with-docker-data-volumes-on-ubuntu-14-04)
