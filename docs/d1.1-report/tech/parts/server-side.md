
## Web frameworks

For the back-end, the server-side of the web application, the pre-selection reduced
the review to three web-frameworks implemented in different programming languages:
[express]/[nodejs] in *javascript*,  [wt] in *C++* and flask]/[sanic] in *python*.

All these web-frameworks were pre-selected since they provide a minimum set of
features (included or within packages), namely:

- routing URLs to handlers
- interacting with databases
- support user sessions and authorization
- templating system to render data (e.g HTML, JSON, XML, ...)
- security against web attacks
- communication with client-side (e.g. web-sockets, ...)
- can serve at least one of the pre-selected front-end technologies

The following sections summarizes the reviews and highlights aspects
that were found useful to support the final recommendation to implement SIM-CORE.

## Javascript [express]/[nodejs]

[express] is probably the smallest web framework on [nodejs], and therefore written
in javascript. It is a lightweight and unopinionated framework which, in conjunction
with the large amount of compatible modules available to extend it, makes it an interesting
candidate for this review.

  - **Language**: node.js, javascript
  - **Popularity**: Github score 92, Stack-overflow score 83
  - **License**: MIT license

**Pros:**

  - *Productivity*:
    - Generally very high since the package manager [npm] solves does most of the heavy
    lifting in many stages of development: initialization, testing, deployment ...
    - Same language as in client sides
  - *Functionality*:
    - Large amount of packages for virtually everything!
    - State-of-the-art package managers as [npm], [yarn] or [bower] can be used
    to install and handle effectively module dependencies

**Cons:**

  - Javascript has low level of integration with python/C++ code.
  - Javascript does not have an official built-in or standard-like library like
   other languages but instead a plethora of *de facto* modules.
  - Found that the complexity of module dependencies makes sometimes it very difficult
  to track down and solve issues.

## C++ [wt]

[wt] cannot be *strictly* defined neither as a client nor a server-side tech, but rather a C++ library to develop web applications that partially run on both sides. This solution allows writing web GUIs in C++ using a widget abstraction. This paradigm is traditionally used in GUI programming in desktop applications, as in [Sim4Life], which makes it very convenient. [wt] also permits the integration side-by-side of third-party javascript libraries like [threejs], to handle the 3D rendering at the client-side. The same type of integration
is expected from the client technologies described in previous sections.

The figure shows a prototype website rendering a part of a 3D human model from the [ViP] family using this technology. More details can be found later in the [demonstrations sections](demos.md).
![wt-screenshot](../img/wt.png)


- Language: C++
- Popularity: Github score 56, Stack-overflow score 40
- License: Dual: GNU General Public + commercial

**Pros**:

- C++ and widget abstraction allows high reusability and compatibility with existing code-base
- Abstracts request handling and UI rendering
- Integrates session management and lifetime: every user has its own application object and deployment models for with dedicated/shared processes per session.
- Can integrate side-by-side other third-party javascript libraries, e.g. [threejs]
- C++ integrates very well with other scripting language like python (see [boost.python])
 ...), etc
- Other advantages inherent to the C++ language: type safety, speed, support to concurrency (multi-threading, coroutines, ...

**Cons**:

- Heavy lifting to get containers build and run. Build and deploy C++ applications can be time-consuming and complex compared to scripting languages-based libraries. Containerization of the development environment (ie. compilers, ...) might lighten this inconvenient but it is definitively more demanding than any other solution based on javascript or other scripting language.
- Not clear separation between server-client. The documentation shows that this is intentionally avoided by design, but it can become an issue when the target is to clearly control the responsibility of each side (e.g. to reduce communication between both sides). First trials shows a high level of communication with the server
even for simple operations that could be easily delegated to the client side.
- License scheme makes it incompatible with MIT license, which is the desirable scheme for this platform.


## Python [flask]/[sanic]

[flask] is a relatively new framework written in python. It takes advantage of
modern features of the language to offer an easy-to-code, lightweight and unopinionated
web framework in python. Asynchronous requests are not supported out of the box but
new built-in modules in python 3 like [asyncio] or brand new frameworks as [sanic]
overcome this important drawback.

  - **Language**: python 3
  - **Popularity**: Github score 91, Stack-overflow score 77
  - **License**: BSD/MIT license

**Pros:**

- *Productivity*: light-weight complete web-framework.
- *Functionality*: standard web-framework
  - Coroutines/asynchronous APIs with [sanic] or [asyncio]
  - Python is a very popular and rich language with extensive built-in library
  - Python has a strong integration with C++ (pyd modules)

**Cons:**

- As all lightweight and unopinionated frameworks, the responsibility to add
standard features (via 3rd party or in-house modules) heavily depends
on the dev-team with the consequent risk of accumulating [technical debt](https://en.wikipedia.org/wiki/Technical_debt) as the codebase grows.


## Conclusions
Based on our review, the selected web-framework candidate is
[flask]/[sanic] in **python**. [express] could be used to prototype or as a dummy server
to test services or APIs. [wt] is not recommended, nonetheless provided the large amount
of modules already available in C++, the evolution of the framework should be monitored in future
extensions.


[asyncio]: https://docs.python.org/3/library/asyncio.html
[boost.python]: http://www.boost.org/doc/libs/1_66_0/libs/python/doc/html/index.html
[bower]: https://bower.io
[express]: http://expressjs.com/
[flask]: http://flask.pocoo.org/
[nodejs]: https://nodejs.org/
[npm]: https://www.npmjs.com
[sanic]: https://github.com/channelcat/sanic
[Sim4Life]: https://www.zurichmedtech.com/sim4life/
[threejs]: https://threejs.org/
[ViP]: https://www.itis.ethz.ch/virtual-population/virtual-population/overview/
[wt]: https://wwww.webtoolkit.eu/wt
[yarn]: https://yarnpkg.com/en/
