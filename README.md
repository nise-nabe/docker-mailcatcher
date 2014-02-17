docker-mailcatcher
==================

SMPT メールサーバモック

## ビルド

```
$ docker build -t nise_nabe/mailcatcher -rm .
```

## 動作確認

```
$ CONTAINER_ID=$(docker run -d -t nise_nabe/mailcatcher)
$ IPADDRESS=$(docker inspect -format '{{.NetworkSettings.IPAddress}}' $CONTAINER_ID)
$ python3 test_send_mail.py $IPADDRESS:1025
```

see http://$IPADDRESS:1080/
