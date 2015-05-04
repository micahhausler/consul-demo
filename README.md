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

## Interact
Check out the IPython notebook Consul by running:
```
pip install -r python_app/requirements.txt
ipython notebook --no-browser
```
and navigate to [/notebooks/Consul.ipnb](http://localhost:8888/notebooks/Consul.ipynb)


## Query the DNS API
You can query the consul DNS API once your containers are up by running:

```
dig @$(boot2docker ip) PythonApp.service.consul +tcp
```