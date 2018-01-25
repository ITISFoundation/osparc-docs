
## Frameworks

For the back-end, the server-side of the web application, the following
web-frameworks were pre-selected for review: [express] in node.js,
[flask]/[sanic] in python and [wt] in C++.

All these web-frameworks provide standard features (included or within
packages) for:

- routing URLs to handlers
- interacting with databases
- support user sessions and authorization
- templating system to render data (e.g HTML, JSON, XML, ...)
- security against web attacks

Most of the points below highlight aspects which are useful for the
discussion in the context of this project.


## [express]

  - **Language**: node.js, js
  - **Popularity**: Github score 92, Stack-overflow score 83
  - **License**: MIT license

**Pros:**

  - *Productivity*:
    - Very high (if no issues with npm or configurations)
    - Same language as in client side
  - *Functionality*:
    - Large amount of packages for virtually everything!
    - npm proves to be state-of-the-art managing dependencies
    - TODO review ongoing

**Cons:**

  - Difficult to integrate python/C++ code (only via other processes)
  - npm complexity makes it very difficult (for non-experts) to track and
solve errors
  - TODO review ongoing


## [flask]/[sanic]
  - **Language**: python 3
  - **Popularity**: Github score 91, Stack-overflow score 77
  - **License**: BSD/MIT license

**Pros:**

- *Productivity*: light-weight complete web-framework.
- *Functionality*: standard web-framework
  - Using asynchronous APIs (sanic)
  - Allows mixed python/C++
  - TODO review ongoing

**Cons:**

-  TODO review ongoing

## [wt]
  - **Language** C++
  - **Popularity**: Github score 56, Stack-overflow score 40
  - **License**: Dual: GNU General Public + commercial

**Pros:**

- *Productivity*: UI programed in a similar way as in desktop app
(analogous to Qt).
- *Functionality*: All power of C++: concurrency, courroutines, multi-
threading ... you name it
    - Has the potential of replacing one-to-one MFC but difficult to
proof
    - TODO review ongoing

**Cons:**

- First trials shows a high level of communication with the server
- Needs some heavy-lifting to get it up and running in container (c++
libs, build, ...)
- TODO review ongoing

## Conclusions
Based on our review, the selected web-framework candidate is
[flask]/[sanic]. [express] could be used as prototype with/for mockup
servers. Although the use of [wt] is currently not recommended, the
evolution of this technology should be followed and reconsidered at a
later stage of the project.

[express]: http://expressjs.com/
[flask]: http://flask.pocoo.org/
[sanic]: https://github.com/channelcat/sanic
[wt]: http://www.webtoolkit.eu/wt

