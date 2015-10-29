# anitya and devpi

Let's try a proof of concept where we try to release a package to our locally running devpi and let anitya to pick up the release.

## Guide

Build and run both services

```
$ docker-compose up
```

(yes, it's one dead-simple command)


### devpi

We need to set up an account on devpi:

```
$ docker exec -ti anityadevpidemo_devpi_1 bash
devpi $ devpi use http://localhost:5001
devpi $ devpi login root --password ''
devpi $ devpi user -m root password=123
```

And create index:

```
devpi index -c demo
devpi use dev
```

We are all set to upload our package:

```
cd demo_package/
devpi upload --no-vcs
```
