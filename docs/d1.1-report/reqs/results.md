

- **Computational resources** : All teams stated that initial
computational resource needs will be moderate, with existing SPARC
related models currently running on simple desktop machines. Typically,
only few people will initially perform modeling and not many simulations
will have to run in parallel. However, in the longer term, parameter
sweeps, optimizations (primarily of stimulation parameters and
configurations), simulations with large number of neurons/cells, and
simulations covering large (simulated) time periods are planned. For that
purpose, support for high performance computing resources has been
requested, with the [NSGportal](https://www.nsgportal.org/) mentioned
in particular as a potential resource worth supporting. One team will
require supercomputing functionality that is beyond what SPARC can
provide. Teams foresee the number of people working
in modeling related areas increase over time and hence, expect a related increase in
computational
burden. However, no concrete estimates of required computational
resources in the longer term could be obtained. Being able to run
simulations in the cloud is seen as valuable and by some groups even considered
necessity.
- **Simulation implementation** : Current simulators are implemented as
C, C++, Java, Matlab, Python, or Excel codes. In some cases, 'workflow'
frameworks (such as Kepler) are used to compile code, manage data, and
post-process results and similar 'workflow' support has been requested.
Linux is the most common environment used by groups that implement their
own compiled codes.
- **Stimulation physics** : Electromagnetic (EM) and acoustic exposure,
thermal, and light propagation modeling have been requested, with
EM modeling most prominently demanded, followed by acoustic
exposure. The other two physics were requested by single teams. Support
for thin layers and anisotropy in the EM modeling is seen as
important. For thermal modeling, consideration of perfusion and
thermoregulation effects is fundamental. Stimulation can be local or
remote, and thus exposure and propagation needs to be modeled on macro-
and micro-anatomical levels. A few teams consider adding own
biomechanical models in the future.
- **Physiological modeling** : Physiological modeling will include body
physiology, organ physiology, and peripheral nervous system (PNS)
electrophysiology models. In addition, modeling of tissue evolution
(damage, interface effects) is planned. Organ models are most frequently
realized as coupled ordinary differential equations (ODEs) of actors
(cells, neurons...), but can also be finite element-type partial
differential equation (PDE) models or even black-box models without known
equations (e.g., extracted through machine learning). PNS models include
compartmental/cable-equation-type models, connection strength models
(stimulation/inhibition), and population activity models, with activity
levels, firing rates, or transient action potentials as primary coupling
quantities. Other coupling quantities include measures of physiological
activity and field distributions. Support for different types of
myelinated and unmyelinated fibers is requested. Both simplified and
morphologically detailed neurons must be supported. NEURON developed by
Yale University is the only software commonly used by the contacted teams
for nerve-electrophysiological modelling. Other software packages, such
as NetPy, are used by single groups. Support for coupling NEURON models
with spatio-temporally varying EM, acoustic, and thermal
exposure has been requested. Computing compound action potentials would
help with validation against experimental data. The MAP-CORE is also
heavily advocating support for CellML/SBML-based solvers.
- **Species** : Contacted teams are interested in modeling the
anatomy/physiology from humans, rats, mice, monkeys, guinea pigs, cats,
rabbits, sheep, and donkeys. An additional poll was launched on the SPARC
SLACK communication platform which revealed that the highest interest is clearly in human,
rat, and mice models.
- **Anatomical models** : Geometric anatomical models on the organ as
well as the nerve microstructure scale have been requested.
Parameterization of anatomical shape would be useful to selected teams.
Furthermore, the possibility of morphing the anatomical geometries to produce
variability and to account, e.g., for organ motility, has been demanded.
Integrating computational models and measured/simulated data in reference
anatomical models is considered as sensible and helpful. Multiple teams
expressed interest in a detailed spinal cord anatomical model.
- **Simulation coupling** : All of the described workflows required/used
by the contacted teams can be implemented as pipelined workflows. Most
computational models, but not all, benefit from convenient separation of
time scales between PNS and the different organ physiological processes,
which permits iterative solving rather than tightly coupled solvers. When
bidirectional or closed loop coupling is employed in the models, it is
always implemented in the form of coupled ODE solvers running in a single
service (for efficiency reasons) and hence can be handled as part of a
pipeline architecture.
- **Visualization** : The typical type of viewers (2D plots, slice field
viewers, surface viewers, 3D rendering, etc.) have been requested. None of the teams
requires the possibility for users to create their own advanced visualization modules.
- **GUI** : There is an important demand for functionality that allows
users to enhance their services/models with a user-friendly interface,
without advanced coding knowledge. The requested interactivity is limited
to standard functionalities, such as parameter specification, message
display, searching, visualization, process submission and monitoring. None of the
groups currently sees a need to be able to implement own specialized forms
of graphical user interface (GUI) interactivity (e.g., an interactive 3D picker). A scripting
interface complementing the GUI would be appreciated by some of the
groups. There is unforeseen demand for a flowchart-like editor for
graphically setting-up, displaying, and editing coupled models with a large number of
components and with properties assigned to nodes and connections
(e.g., neural networks, physiological influences; this can be seen as generalization and
extension of the pipelining/workbench).
- **Sharing** : All groups expressed willingness to share their models.
In some cases, it has been requested that models can be kept private
prior to publication of results or while going through (e.g., internal)
approval processes. In other cases, it has been requested that models can
be shared without need to divulge the underlying implementation, or that
sharing can be limited to research purposes. No request for the ability
to charge for model use has been made. However, the possibility of
licensing solvers developed by SPARC teams prior to the SPARC program for
use on the platform has been brought up. Collaborative model development
between groups involved in the same organ system has been mentioned as
desirable.
- **Image processing** : Segmentation support has been requested and
multiple teams would be interested in using microscopy images to generate
nerve microstructure models. Image processing is used by the SPARC
awardees for various tasks (video analysis, calcium expression, neuron
morphology reconstruction, etc.), but for those tasks the teams will continue
using their established tools (e.g., ImageJ, Imaris, Neurolucida). One team
expressed willingness to share self-developed video analysis
functionality in the form of a SIM-CORE service, but it is unclear if
other parties would be interested in such functionality. Only one team
expressed interest in using a potential SIM-CORE nerve-tracing tool in
the future.
- **Meta-modeling** : There is a high demand for meta-modeling
functionality. This includes parameter studies, parameter tuning,
optimization, uncertainty assessment, and uncertainty propagation.
Multiple teams expressed interest in control functionality (e.g., closed-
loop control) and model order reduction functionality.
- **Quality assurance** : Functionality that allows to reproduce
previously performed studies, as well as ways of
assessing the degree of model validation, is judged as important.
- **Support** : Most teams have requested extensive support with model
development ("What should we measure to create a model?"), in moving
existing models to the platform, and with platform use (training events,
contactable support team).
- **File formats** : File format standards exist for electrophysiological
measurements and image data. Results are frequently stored in ascii
files, Matlab, or Excel form. Overall, teams did not express
the need of supporting specific file formats and seem to be flexible on
adapting their models as required. Some of the teams pointed out that
communities, such as the human brain project, have established standards
for specific purposes.
- **Maintainability** : Long-term sustainability of the platform is seen
as major argument for moving models onto the SPARC platform. Even though, at this point,
teams were not willing to concretize if in the long term they would be
willing to pay for such a service, they do see the platform as highly
valuable beyond SPARC.
- **Platform development** : While most teams are interested in creating
and offering their own services, contributing to the open source
development of the actual platform is generally only seen as something
that could be of interest for student projects. Making use of a scripting
interface is deemed as of potentially high interest by contacted parties,
but not concretely planned.
- **Analysis** : Availability of analysis functionality (e.g., Python-
based analysis scripts) has been requested. Services that run Matlab or
similar tools for analysis purposes are needed by most teams. Other
softwares that are currently used for analysis purposes include R,
Statistica, SPSS, and graphpad. Data transfer between tools is often time consuming and
frequently associated with
a considerable effort and accordingly, supporting analysis pipelines
within the online platform would be valued.
- **Privacy** : The contacted teams do not foresee privacy issues related
to the data or images that they require in the context of computational
modeling.
