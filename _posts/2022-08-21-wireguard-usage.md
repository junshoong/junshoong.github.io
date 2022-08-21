---
layout: single
title: "wireguard 설치 및 설정"
date: "2022-08-21"
categories: "linux"
tags: linux vpn wireguard 
authors: junshoong
---

### 설치환경
- VPN Server
    - OS : CentOS Linux release 8.2.2004 (Core)
    - kernel : 4.18.0-305.25.1.el8_4.centos.plus.x86_64
    - wireguard-tool : 1.0.20210914-1.el8

### 설치
설치는 [공식 페이지](https://www.wireguard.com/install/)를 참고했다.
내 경우에는 제공된 가이드의 방법1을 활용
```bash
yum install yum-utils epel-release
yum-config-manager --setopt=centosplus.includepkgs="kernel-plus, kernel-plus-*" --setopt=centosplus.enabled=1 --save
sed -e 's/^DEFAULTKERNEL=kernel-core$/DEFAULTKERNEL=kernel-plus-core/' -i /etc/sysconfig/kernel
yum install kernel-plus wireguard-tools
```
이후 Reboot 해서 커널이 정상적으로 올라오는지 확인

### 설정
셋팅하기 전에 VPN을 통해 구현하는 바를 명확히 해야 한다.  peer to peer,  peer to site, site to site 등 다양한 구성이 있어 환경에 맞는 구성을 고려해서 셋팅한다.
내 경우는 peer 가 site에 접근하도록 구성했다.
개념을 잡는데 [이 페이지](https://www.procustodibus.com/blog/2020/10/wireguard-topologies/#point-to-site)에서 도움을 받았다. 

#### Site 설정
interface를 직접 만들고 셋팅하는 경우도 있는데 config를 기반으로 한 서비스형태로 활용하기 위해 아래와 같이 설정파일을 구성했다.

/etc/wireguard/wg0.conf
```
[Interface]
PrivateKey = <prikey>
Address = 172.31.1.1/32
ListenPort = 51820
SaveConfig = true
PreUp = firewall-cmd --zone=public --add-port 51820/udp && firewall-cmd --zone=public --add-masquerade
PreUp = iptables -t mangle -A PREROUTING -i wg0 -j MARK --set-mark 0x30
PreUp = iptables -t nat -A POSTROUTING ! -o wg0 -m mark --mark 0x30 -j MASQUERADE
PostDown = firewall-cmd --zone=public --remove-port 51820/udp && firewall-cmd --zone=public --remove-masquerade
PostDown = iptables -t mangle -D PREROUTING -i wg0 -j MARK --set-mark 0x30
PostDown = iptables -t nat -D POSTROUTING ! -o wg0 -m mark --mark 0x30 -j MASQUERADE

[Peer]
PublicKey = <pubkey_peer>
AllowedIPs = 172.31.1.2/32
```

IP는 상황에 맞게.
내 경우는 경험상 172.31.x.x 대역을 사용했던 적이 없는것 같아 이 IP로 설정했다.
peer가 VPN 으로 사용할 IP와 peer가 default Network로 사용한 IP 대역이 겹치는 경우 잘 동작하지 않기 때문에 보통 많이 사용하는 192.168 대역은 피하고자 했다. 물론 접근하는 환경이 개인이 설정할 수 있거나 고정적인 경우에는 크게 문제 없을 것 같다.

conf를 보면 `Interface` section이 있고 `Peer` section이 있다.

`Interface`는 현재 wireguard를 실행하는 Host의 인터페이스에 대한 설정이다. PreUp, PostDown 으로 `firewalld`와  `iptables` 설정을 해주었다.
PrivateKey에 들어가는 key는 아래 커맨드로 생성한다.
```bash
(umask 0077; wg genkey > vpn-server.key)
```
Host에서는 Private key만 있으면 되고, 접근하려는 Peer에 나중에 Public key를 배포한다.
나중에 배포한 Publick key는 이렇게 생성해준다.
```bash
wg pubkey < vpn-server.key > vpn-server.pub
```
파일 이름은 어차피 상관없고 내부에 생성된 값이 중요하다. 생성된 private key 값을 위 config에 넣어주면된다.

`Peer` 부분은 여러번 선언해줄 수 있다. 내 경우에는 배포할 기기별로 선언해두었다.
`AllowedIPs`에 접근할 peer의 IP를 입력해준다. 이 부분도 Peer 설정부분에서 볼 수 있다.

셋팅후 서비스를 올려준다.
```bash
systemctl start wg-quick@wg0.service
```
인터페이스를 보면 wg0라는 이름의 interface가 생겨있다. 
```
12: wg0: <POINTOPOINT,NOARP,UP,LOWER_UP> mtu 1420 qdisc noqueue state UNKNOWN group default qlen 1000
    link/none 
    inet 172.31.1.1/32 scope global wg0
       valid_lft forever preferred_lft forever
```
라우팅이나 iptables, firewalld 설정도 잘 들어가있다.
`wg` 를 입력하면 아래와 같이 현재 상태를 확인할 수 있다.
```
interface: wg0
  public key: <pubkey>
  private key: (hidden)
  listening port: 51820

peer: <pubkey_peer>
  allowed ips: 172.31.1.2/32

```

#### Peer
Peer 설정은 별거없다.
먼저 key를 생성해준다
```bash
wg genkey > peer-a.key
wg pubkey < ./peer-a.key > peer-a.pub
```
그리고 config를 만들어준다.
```
[Interface]
PrivateKey = <prikey_peer>
Address = 172.31.1.2/24
DNS = <dns_a>, <dns_b>

[Peer]
PublicKey = <pubkey_site>
AllowedIPs = 192.168.0.0/24
Endpoint = <host:port>
PersistentKeepalive = 25
```
`Interface` section의 Address는 Peer가 연결시 사용할 IP가 되고, DNS는 연결시 사용할 DNS가 된다. DNS부분은 필요 없으면 넣지 않아도 된다.
`Peer` section에 AllowedIPs에 넣은 값에 따라 Peer의 라우팅 테이블에 데이터가 추가된다. Endpoint는 Site쪽으로 접근할 수 있는 IP(혹은 Domain)와 port를 넣어준다. `PersistentKeepalive`는 연결상태를 유지하기 위해 넣는 옵션으로 상황에 따라 사용하면 된다. [archlinux wiki에 관련 설명](https://wiki.archlinux.org/title/WireGuard#Unable_to_establish_a_persistent_connection_behind_NAT_/_firewall)이 있다.

위와 같은 config 작성후에 접근할 기기에 wireguard를 받고 config를 넣고 activation해주면 정상적으로 접근되는것을 확인 할 수 있다.

### 문제해결
보통 문제가 생기는건 Network쪽이다. Site쪽에서 외부로 노출시킨 IP / Port 정보를 정확히 확인하고 중간에서 막히는 구간이 없는지 체크해봐야 한다. NAT를 사용한다면 Port fowarding rule이나 방화벽의 allow 정책을 확인해보는게 좋다.

혹은 위에 잠깐 언급한, Peer의 현재 IP대역과 VPN접근시 사용하는 IP대역이 물려있진 않은지 확인해보는게 좋다. 라우팅이 꼬여서 접근이 잘 안될 수도 있다.

Site설정시 주의할 점으로는 /etc/wireguard/wg0.conf 파일을 수정후 systemctl로 재시작하면 변경사항이 날아가는 현상을 목격했다. 별도 위치에서 편집후 start하기전에 파일을 옮겨주는게 안전해보인다.

### 결론
기존에 openvpn을 사용했는데, 설정도 꽤 간단하고 테스트는 따로 해보진 않았으나 속도가 빠른게 확연히 체감한다.
접근시 사용할 수 있는 여타 다른 모듈들은 확인해봐야 겠지만 개인적으로 사용하는 입장에서는 만족스럽다.