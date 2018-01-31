

The framework shall serve a website designed to provide any SIM-CORE user with 
functionality for building, pipelining, scheduling, and running computational models. These 
models and the associated information (sometimes denoted as metadata) can be provided 
by the user himself and/or pulled/pushed/searched from/to, e.g., the DAT- or MAP-CORE.  
The SIM-CORE shall define its own user entry-point and shall interface to the other CORE's 
services and/or APIs.

Regarding technology, the [front-end](client-side.md) shall be implemented in the [qooxdoo] 
framework. For the [web server](server-side.md) [flask],  a python web framework, shall be 
the preferred technology. The [computational services](comp-services.md)
shall be encapsulated in [docker] containers and orchestrated using [swarm]. Docker 
containerization of computational services provides an ideal solution for sustainability since 
the original user applications will run in the framework within environments closely 
resembling the environments in which they were conceived, without requiring major 
modifications to interact with the orchestrator or communicate with other services.
The [communication](communications.md) between services shall be accomplished with
[apache-thrift] or a REST-API. The former shall be the preferred method for internal services,
while the latter shall be used to interact with APIs of external services.

The platform, as well as the computational services, shall be designed to be deployed and 
run in the cloud. 

The performance of the different modules/parts will continue to be monitored as user 
stories are successively implemented in the development process, and if necessary, the 
above described technological approaches will be adapted. Special attention will have to be 
paid to the orchestration of computational services and the responsiveness of the web-UI 
when large CAD models are manipulated or transmitted.

 

