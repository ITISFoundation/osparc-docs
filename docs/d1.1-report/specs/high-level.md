

- **User Interface**: The user interface shall primarily be a browser-
based GUI. It shall be user-friendly and interactive. It shall support
interface elements that permit setting parameters and properties,
visualizing 3D scenes, displaying data (tables, plots, trees, image-data,
etc.) and messages, setting up and displaying work-flows and complex 
dependencies/influences/coupling ("workbench", interaction graph with possibility of 
assigning properties to nodes and connections),
monitoring and administering computational resources, as well as
accessing and managing data (local data and data in the DAT-CORE). With
lower priority and/or at a later stage, the user interface should also
offer a scripting interface (Python-based). Through the GUI, users shall
be able to access data and models (including search functionality),
manage access rights, set up studies and workflows, execute and monitor
services locally and in the cloud, as well as perform analysis and post-
processing.
- **Services Infrastructure**: Service environments that make it easy to
run Python scripts, to run executables (Unix-based operating systems,
such as Linux, are currently the only platforms used by contacted SPARC
teams developing their own solvers/executables) that take parameters from
the command line or standardized input file formats, to compile and
execute C, C++, and Java code, and to execute R scripts shall be
provided. It shall be easy for users to register new services by using
one of the predefined service environments and inserting their
executables/code/... and it must be simple to specify the required input
parameters such that they are exposed through the online GUI. By
providing information about the generated output, it shall be possible to
present the output using standardized viewers (plots, 3D views, slice
field views, isosurface views, etc.). It shall be possible to link services
with compatible outputs and inputs into pipelines. Advanced users shall
have the possibility of creating services that manage dedicated sections
of the online GUI, allowing them superior control also over visualization
and interaction. When executing a service, all the information required
to reproduce the execution (input data, parameters, version of service, etc.)
shall be stored, to facilitate reproduction.
- **Specialized Services**: A range of commonly required services shall
be provided. On the physics solver side, this includes primarily
EM exposure. Typically, the most required variant of
EM solver is an electroquasistatic solver (for exposure
through electrodes). Another relevant EM solver is the
magnetoquasistatic solver (for exposure by coils and loops). Selected
teams will also require acoustic propagation, biomechanics, optics, and
tissue damage solvers (not all of these can be provided by IT'IS). The
platform must support either the import of discretized models (meshes,
voxels), or provide discretization services (voxeler, mesher), or both.
On the electrophysiological modeling side, the most commonly required
solver that shall be supported is NEURON from Yale. Predefined, diameter-
parameterized fiber models shall be provided, which must include the MRG
model, and shall be assignable along user-defined trajectories. There is
large request for an unmyelinated fiber model, but it is currently
unclear, which model is suitable. It shall also be possible to load and
simulate complex neuron models, defined as .hoc files. It must be
possible to couple EM exposure conditions with
electrophysiological neuron models. Metamodeling services that can vary
parameters of services or pipelines to perform optimization tasks, assess
sensitivity, propagate uncertainty, and perform model order reduction
shall be provided. In addition, a specialized optimization functionality
to find optimal stimulation parameters (currents, pulse-shapes) for
multi-contact electrodes that produce selective stimulation of fibers is
required. A Python service with libraries such as numpy, scipy,
pyplot/plotly that provide users with analysis and post processing
functionalities akin to Matlab shall be offered (Supporting Matlab within
a dedicated service could be problematic at the current time, due to
licensing issues in combination with Docker technology. Octave could be a
highly compatible alternative and Python with suitable extensions also
provides similar functionality to Matlab.). The creation of a SBML/CellML
service to support the MAP-CORE vision is desirable. A coupling service
shall allow setups involving more advanced execution schemes and data
exchange than simple pipelining, within the limitations imposed by
latency and bandwidth. This shall include iterative coupling and
bidirectional coupling. A service allowing (ontological) annotation of
anatomical and physiological models will be provided by the MAP-CORE.
- **Models**: The platform shall offer anatomical models of humans (man
and woman) and a rat. We choose a rat because rats were most popular in the
vote conducted via Slack, and because it is anticipated that imaging
and identifying selected peripheral nerves will be easier in rats than in
mice, because of their size, resulting in superior model quality. Further
animal models that shall be considered at a later point include mice,
cats and a monkey. The anatomical models shall be pre-functionalized with
the trajectories of major peripheral nerves. Through a service, it shall
be possible to obtain for simulation purposes discretized representation
of the models or sub-regions thereof. It shall be possible to register
additional layers of information relative to the anatomical models. These
include measurement and simulation data, image data, nerve trajectories,
anatomical detail, device models, as well as electrophysiological models.
- **Computational Infrastructure**: The platform shall initially run on
HPC hardware localized at IT'IS. Subsequently, the platform shall run on
the Amazon cloud and be flexibly scalable, depending on user demand. It
should be considered to add support for execution of selected services
(e.g., NEURON simulations) on dedicated high-performance computing
resources (e.g., NSG portal).
- **Image-based Modeling**: Functionality shall be available that permits
to segment image-data and convert it into anatomical models. It shall be
facilitated to generate nerve models from histological
images/information, trajectories, and knowledge about fibre type and
property distributions. Morphing functionality for applying
transformation fields to anatomical model and thus parameterize their
geometry shall be provided.
- **Data storage and annotation**: It shall be possible to store models,
services, studies, results, and additional data in the DAT-CORE, the
cloud, or locally. It shall be possible to enhance data with meta-
information, such as links to related information (e.g., links to
documentation and validation data), ontological descriptors, or quality
certification. It shall be possible to relate data to points or regions
within specific anatomical models. Data shall be referenceable (unique
identifier, linkable) and traceable (origin of data, versions).

