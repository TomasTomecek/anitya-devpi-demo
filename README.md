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
devpi use demo
```

We are all set to upload our package:

```
cd demo_package/
devpi upload --no-vcs
```

### notes

 * anitya doesn't harvest package metadata (we would have to write this ourself)
 * anitya uses probably cron for scheduling (that's what upstream [has](https://github.com/fedora-infra/anitya/blob/master/files/anitya_cron.py))
 * once a new release is found, anitya posts a message to fedmsg and [new-hotness](https://github.com/fedora-infra/the-new-hotness/) picks it up and processes it
  * will pipeline have message bus?
