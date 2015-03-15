# Consul Demo
This is a simple demo and introduction to consul.

## Setup
Setup assumes a Mac running a modern version of OS X

1. Install [boot2docker](http://boot2docker.io)
1. Install docker-compose:
```
pip install docker-compose
```
1. Clone this repo, run consul
```
git clone git@github.com:micahhausler/consul-demo.git
cd consul-demo/
docker-compose build
docker-compose up
```

## See the UI
[http://192.168.59.103:8500/ui/](http://192.168.59.103:8500/ui/)
