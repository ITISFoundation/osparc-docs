


## Introduction

The computational backend involves all services needed to handle the
actual computational workload. A computational workflow is described as a
pipeline that processes a stream of data in a sequential way. Every
pipeline consists of multiple algorithms, each one expecting specific
input data and providing specific output data. The pipeline can be built
up in the frontend as a directed acyclic graph (dag) where the edges
describing input/output and the nodes consisting of the algorithms (i.e., the
computational kernels). Such kernels include complete, standalone solvers,
algorithms to calculate specific quantities, or viewers that renders
data into graphs, plots or tables, etc.


## Responsibilities

The computational backend:

- schedules the execution of pipelines in an efficient way, while
respecting the inherent data dependencies
- provides the user with a list of all available algorithms
- provides a mechanism to easily inject new algorithms
- allows control/managing of concurrently running pipelines
- can be dynamically up/down-scaled depending on the current load
- has access to a database with all relevant input and output data

## Selection of technology for computational kernel integration

Since a central purpose of the SIM-CORE platform is to allow users to add
user-defined algorithms, the technology preselection was based on the
criterion that it should provide an isolated, protected context that preserves the user's 
application and minimized the adaptation effort required to integrate the model in the SIM-
CORE. 

Modern scientific libraries and solvers span a broad range of programming
languages, are typically very specialized, have many dependencies on
numerical libraries, and are usually designed to work best on 
very specific platforms. In order to ease the deployment of services
consisting of such codes into the heterogeneous SIM-CORE platform, it is
desirable to provide contributors with the toolsets and platforms they
know best. This can be achieved using containers or virtual machines. Due
to the large overhead in terms of hardware consumption, usage of virtual
machines has been discarded in favor of the containerized approach.
Containers, in contrast to virtual machines, do not emulate the hardware
but the operating system itself. This makes them much more lightweight
and allows for up to thousands of instances running simultaneously on one
host.

There are several approaches to containerization. However [docker] has
become the de-facto standard in industry and academia, and many
scientific applications already provide users with [docker] images of their
code. Furthermore, it is possible to use the [docker] [swarm] tool that
natively allows the orchestration of multiple [docker] containers among a
heterogeneous network of computers. Furthermore, all major cloud
providers support the technology. If more sophisticated means of orchestration are required 
during the future evolution of the
platform, there
exists the possibility of using kubernetes, which is the major player
when it comes to managing containers and for which [docker] has recently
added full support.

The [docker] framework also allows easy functionality extension on
existing images, which will be used to enhance algorithms with an
additional layer that makes integration into the SIM-CORE ecosystem
possible. A specific use case will be discussed below.


## Core components of computational backend

**Docker image registry**

Considering the technology decision outlined above, another core
component of the [docker] ecosystem is being used for the computational
backend, namely the concept of a [docker] registry. Every computational
service is provided as a [docker] image in a repository that is part of the
SIM-CORE platform. These images are pulled from the registry when
required, and a container is created to run (execute) the corresponding
service.

In addition to the images themselves, the registry also contains meta-
information for the services. This allows storing information such as:

- required input data (format)
- output data (format)
- specific hardware needs (GPU/multicore)
- version number and hashes for identification

This data can be used to check whether two algorithms in the pipeline
can be connected or not.

**Director**

The director acts as bridge between the frontend/backend and the
computational backend. It is aware of all available algorithms in the
registry and can translate incoming pipelines into workflows and
schedule jobs to be executed in a proper order.

All jobs are kept in a queue and their status can be queried by the
client. Job control such as stop/kill/resume is also provided.

**Distributed task queue and message broker**

All jobs in the platform are being scheduled in a centralized queue based
on message passing. Workers can grab tasks from the list and execute them
concurrently. For that purpose, a broker service that handles all the
message passing from the director to the worker is also part of the
computational backend. Due to its popularity and wide usage, the *celery*
library has been chosen for the distributed task queue. It is easy to
integrate and offers bindings to several languages. It also supports
several message brokers and database backends. For the initial
prototyping, *RabbitMQ* is chosen as message broker and *MongoDB* as
database.

**Workers**

Workers are the services that perform the actual computation. They always
appear as pairs of containers: a sidecar and an actual computational
service. The sidecar is always alive and is connected to the tasks queue.
When required it creates a so-called one-shot container that runs the
requested computational service. All the sidecar-computational service
interactions happen through the command line interface. Furthermore,
since being physically on the same host, the side care and computational
service share the filesystem, which allows the sidecar to make input
files or other data available to the computational service.

The advantage of this design is that all complex interaction with the
system is being abstracted away from the computational service and
enables contributors to add algorithms without the need for detailed
knowledge of the platform.

**Service Orchestration**

As mentioned above, SIM-CORE takes advantage of the native [docker]
orchestration tool [swarm]. If more flexibility is required in the future,
it will be possible to use kubernetes to support orchestration.


### Example use case


In this section, we briefly outline how we envision enabling platform users to share their 
models/services on the SIM-CORE. The minimal requirements for successful integration are:
- the service resources (source code, executable, third party libraries...) required for 
execution (and potentially compilation or other pre-/post-processing steps)  (preferably as 
already contained in a dockerfile)
- information about input data requirements
- information about produced output


For the sake of simplicity, consider a computational service that
evaluates a user defined single variable function in a given interval and
a second service that renders that result as a scatter plot. For the
function parsing service, C and C++ code is available from a contributor.
In addition, the contributor specified the command line arguments for its
algorithm. For the visualization part, a default service from the SIM-
CORE platform will be used that expects a tab separated list of values as
an input and creates a rendered html page with a scatter plot.

**Dockerfile**

A [docker]-file contains all commands needed to create a [docker] image that
can be run in a container. For the function evaluator, this file looks as
follows:


```bash
  FROM alpine

  MAINTAINER  Manuel guidon <guidon@itis.ethz.ch>

  RUN apk add --no-cache g++ bash jq

  WORKDIR /work

  ADD ./code /work
  ADD ./simcore.io /simcore.io
  RUN chmod +x /simcore.io/*

  ENV PATH="/simcore.io:${PATH}"

  RUN gcc -c -fPIC -lm tinyexpr.c -o libtiny.o
  RUN g++ -std=c++11 -o test main.cpp libtiny.o
  RUN rm *.cpp *.c *.h
```

The image is based on a very small Linux distribution called `alpine`
with compilers `gcc`, shell `bash` and jason parser `jq`. The important point here is that 
contributors of such services can freely choose base images, compilers and libraries. All that 
is required for integration into the SIM-CORE platform is a description of the kernels 
command line and of the input data.
Here, in addition, to compiing the source code into an executable called `test` the `PATH` is
being augmented by some scripts from what is called `simcore.io`. This
allows to enhance the [docker] command line interface (cli) by whatever is
needed to run the computational service via the sidecar. In this case,
there is a `run` command added to the cli. The content of this command is shown below. It 
parses the input data and creates properly formatted command line arguments for the 
computational kernel. Alternatively, or in addition, input files could be used. As mentioned 
above, this information needs to be provided by the contributors of the code.

```bash
  #!/bin/bash

  arg1=$(cat $INPUT_FOLDER/input.json | jq '.[] | select(.name =="xmin")
.value')
  arg2=$(cat $INPUT_FOLDER/input.json | jq '.[] | select(.name =="xmax")
.value')
  arg3=$(cat $INPUT_FOLDER/input.json | jq '.[] | select(.name =="N")
.value')
  arg4=$(cat $INPUT_FOLDER/input.json | jq '.[] | select(.name =="func")
.value')
  temp="${arg4%\"}"
  temp="${temp#\"}"
  arg5=$OUTPUT_FOLDER/output

  ./test $arg1 $arg2 $arg3 $temp $arg5 > $LOG_FOLDER/log.dat
```
In this case, the sidecar would copy the all input data needed into a
file called `input.json` which the above script would parse and pass to
the test executable.

After building, the [docker] image is deployed into the [docker] registry
with the following meta data:

```json
{
  "input":[
    {
      "name": "N",
      "value": 10
    },
    {
      "name": "xmin",
      "value": 0.0
    },
    {
      "name": "xmax",
      "value": 1.0
    }
    {
       "name": "func",
       "value" : "sin(x)"
    }
  ],
  "output": tsv
}
```

Finally, the descriptor for this part of the pipeline would look like

```json
   {
     "input":
     [
       {
         "name": "N",
         "value": 10
       },
       {
         "name": "xmin",
        "value": -1.0
      },
      {
        "name": "xmax",
        "value": 1.0
      },
      {
        "name": "func",
        "value": "exp(x)*sin(x)"
      }
    ],
    "container":
    {
      "name": "simcore.io.registry/comp.services/function-parser",
      "tag": "1.1"
    }
  }
```

The above scripts and file descriptors represents the current state and
steps during the technology evaluation process. It needs to be clarified
to what degree this can be simplified for integration of SPARC/3rd party
computational services, or assigned to a supporting entity (e.g., IT'IS
support within SPARC), or facilitated through increased automation within
the SIM-CORE platform (resulting in additional development effort).

**Miscellaneous**

- By the end of 2016 Microsoft added support for [docker] containers on the
Windows family of operating systems. Since [docker] [swarm] is operating
system agnostic, the SIM-CORE platform automatically supports Linux- and
Windows-based computational services
 - Shifter, a new open source project provides a runtime for container
images and is specifically suited for HPC on supercomputer architecture.
Among other formats it supports [docker]
- The MPICH application binary interface (ABI) can be used to link code
against the ubuntu MPICH library package and change the binding at
runtime to the host ABI compatible MPI implementation. This is important, because scientific 
code often needs to be completely recompiled in order to accommodate to different MPI 
libraries. The mentioned approach, where available, significantly reduces the amount of work 
involved in becoming compatible with the underlying specific communication hardware.


[docker]: https://www.docker.com
[swarm]: https://docs.docker.com/engine/swarm/
