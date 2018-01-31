# Doc Tools
[![Documentation Status](https://readthedocs.org/projects/osparc-docs/badge/?version=latest)](http://osparc-docs.readthedocs.io/en/latest/?badge=latest)


 A collection of tools to build, format, compose, convert, ... documentation
 written in a markup language, e.g. [markdown] or [reStructuredText] text.


 ## Content:

 - doc-generator : dockerized [mkdocs]
 - [md2pdf]: a dockerized python tool to create a PDF document from a markdown sources



#### Dev Notes:
Tried several tools to convert from mkdocs to pandoc and then to pdf but found some troubles:
 - ~~[mkdocs-pandoc]~~ fails upon execution with ```TypeError: _split_row() takes exactly 2 arguments (3 given)```!?
 - ~~[mkdocs-combine]~~ is a fork of [mkdocs-pandoc] but does not process correctly mkdocs.yml pages hierarchy. It produces a pandoc file with only the uppermost sections.




 [markdown]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
 [md2pdf]: https://github.com/Fiware/tools.Md2pdf
 [mkdocs]: http://www.mkdocs.org
 [mkdocs-combine]: https://twardoch.github.io/mkdocs-combine/
 [mkdocs-pandoc]: https://github.com/jgrassler/mkdocs-pandoc
 [reStructuredText]: http://docutils.sourceforge.net/rst.html
