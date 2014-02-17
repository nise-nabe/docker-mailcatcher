docker-mailcatcher
==================

SMPT メールサーバモック

## ビルド

    $ docker build -t nisenabe/mailcatcher -rm .

## 動作確認

    $ CONTAINER_ID=$(docker run -d -t nisenabe/mailcatcher)
    $ IPADDRESS=$(docker inspect -format '{{.NetworkSettings.IPAddress}}' $CONTAINER_ID)
    $ python3 test_send_mail.py $IPADDRESS:1025

see http://$IPADDRESS:1080/
