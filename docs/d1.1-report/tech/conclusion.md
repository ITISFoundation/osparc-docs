The technology evaluation started by defining the logical architecture of the
SIM-CORE framework and establishing a pre-selection of technologies for each of the
logical modules and concepts of interest. Proof-of-concepts and/or full functional
prototypes were built with each technology and analyzed during the review process
(see ```demos``` folder in [osparc-lab](https://github.com/ITISFoundation/osparc-lab)
repository at [github]). The main purpose was to establish a more experience-based opinion
on the pros/cons of each option.

Finally, a set of three comprehensive [demonstrators](parts/demos.md) were built and
presented live during the teleconference with the SPARC Subject Matter Experts
on December 13, 2017.

This review concludes with recommendations on technologies to use for different parts
of the SIM-CORE. [qooxdoo] was selected as the most suitable framework for the
[front-end](parts/client-side.md). For the [web server](parts/server-side.md) [flask].
a python web framework, is the preferred technology. The [computational services](parts/comp-services.md)
shall be encapsulated in [docker] containers and orchestrated using [swarm]. The [communication](parts/communication.md) between services shall be accomplished
with [apache-thrift] or a REST-API. The former is the preferred method for internal services,
while the latter shall be used to interact with APIs of external services.


[apache-thrift]: https://thrift.apache.org/
[docker]: https://www.docker.com
[flask]: http://flask.pocoo.org/
[github]: https://github.com/ITISFoundation
[qooxdoo]: http://www.qooxdoo.org
[react]: https://reactjs.org
[swarm]: https://docs.docker.com/engine/swarm/
[three.js]: https://threejs.org/
[qooxdoo]: http://www.qooxdoo.org
[vue]: https://vuejs.org
