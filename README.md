# osparc-docs
Source and tools for documentation and reporting

The documentation in this repo can be rendered using [mkdocs]. A pre-installation
of all necessary tools is already available in a docker. The easies way to render
the doc locally in a website and see the changes in the md files is
```bash
  docker-compose build
  docker-compose up doc-generator
  # open localhost:8000 in browser
```

Alternatively, you can build and run the container using directly docker
```bash
# pull
docker pull itisfoundation/doc-generator:latest
# or build in place
docker build -t itisfoundation/doc-generator -f tools/doc-generator/Dockerfile .

# then run
docker run -it -v $(pwd):/usr/app -p 8000:8000 itisfoundation/doc-generator:latest
```

**NOTE**: the content of this repository started as a doc folder in [osparc-lab repo](https://github.com/ITISFoundation/osparc-lab).

[mkdocs]: http://www.mkdocs.org
