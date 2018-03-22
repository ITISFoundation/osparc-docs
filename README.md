# oSPARC documentation
[![Documentation Status](https://readthedocs.org/projects/osparc-docs/badge/?version=latest)](http://osparc-docs.readthedocs.io/en/latest/?badge=latest)

Source and tools for documentation and reporting

The documentation in this repo is written in markup language. Currently
we are using [markdown] and is rendered using [mkdocs].

Under ```tools``` folder, we provide a docker with [mkdocs] pre-installed to render
all [markdown] into an html. Just
```bash
  docker-compose build
  docker-compose up doc-generator
  # open localhost:8000 in browser
```
Any further changes in the doc files will automatically trigger an updated of
the website.

Alternatively, you can build and run the container using directly docker:
```bash
# pull
docker pull itisfoundation/doc-generator:latest
# or build in place
docker build -t itisfoundation/doc-generator -f tools/doc-generator/Dockerfile .

# then run
docker run -it -v $(pwd):/usr/app -p 8000:8000 itisfoundation/doc-generator:latest
```







**NOTE**: the content of this repository was originally within a doc folder in [osparc-lab repo](https://github.com/ITISFoundation/osparc-lab). The git history was
[moved](http://gbayer.com/development/moving-files-from-one-git-repository-to-another-preserving-history/) into this repository.

[MarkDown]: https://daringfireball.net/projects/markdown/syntax#philosophy
[markdown]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
[mkdocs]: http://www.mkdocs.org
