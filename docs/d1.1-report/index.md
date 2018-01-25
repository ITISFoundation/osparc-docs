## Executive Summary
This document is related to Deliverable D1.1 of the IT'IS SIM-CORE
proposal: "D1.1 -Detailed technical specifications for o2S2PARC, based on
user requirements (e.g., from questionnaires) and technology evaluation".
The requirements for the SIM-CORE platform (o2S2PARC) were established
through two activities: 1) contacting SPARC teams to establish their
modeling needs and 2) evaluating the relevant software technologies
necessary for the effective implementation of the SIM-CORE, mostly by
creating feasibility prototypes. The related Milestones are M1.1, M1.2,
and M1.3. These activities (methodology, results, conclusions) have now
been completed and are summarized in this document. From this, high level
platform functionality specifications and concrete framework architecture
specifications are derived.

The requirements are very much aligned with prior expectations and only
minor adaptation of the proposal and possibly a change in prioritization
is suggested, as elaborated in this document. The technology evaluation
has resulted in a clear idea of the technologies and approach that should
be applied to implement the SPARC SIM-CORE platform. The design of the
platform will enable maximal flexibility with regard to the wide variety
of existing and envisioned user-generated modeling services. It will also
offer user-friendly interfaces, allowing users to engage on different
levels with the platform, ranging from simple execution of existing
models to the advanced generation of services with fine-grained control
over dedicated user-interface elements, depending on expertise. Due to
the modularity of the chosen approach, it will be simple to extend and
adapt the platform at later time-points, and it will be feasible to
revisit some of the choices as technology evolves and to replace layers
or components of the implementation without the need for a complete
redesign of the platform.


## Introduction
This document is related to Deliverable D1.1 of the IT'IS SIM-CORE
proposal: "D1.1 -Detailed technical specifications for o2S2PARC, based on
user requirements (e.g., from questionnaires) and technology evaluation".
The requirements for the SIM-CORE platform were established through two
activities: 1) contacting SPARC teams to establish their modeling needs
and 2) evaluating the relevant software technologies necessary for the
effective implementation of the SIM-CORE, mostly by creating feasibility
prototypes. The related Milestones are M1.1, M1.2, and M1.3. These
activities have now been completed and the results are summarized in this
document. After presenting the [requirement gathering approach and
effort](./reqs/methodology.md), the [obtained information is
summarized](./reqs/results.md), and [conclusions](./reqs/conclusions.md)
are drawn. The [technology evaluation approach and
activities](./tech/intro.md) are introduced, [results](./tech/intro.md)
are presented, and  [conclusions](./tech/conclusion.md) are reached. From
this, [high level platform functionality specifications](./specs/high-level.md) 
and [framework architecture specifications](./specs/low-level.md) are derived.