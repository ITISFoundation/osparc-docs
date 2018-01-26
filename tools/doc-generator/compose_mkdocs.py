# coding: utf-8
"""
    Helper to merge all markdown files into a single and viceversa
"""
# pylint: disable=import-error

import os
import sys
import re
import yaml
import logging

logging.basicConfig(level=logging.DEBUG)
_LOGGER = logging.getLogger(__name__)


def join_parts(parts, stream=sys.stdout, basepath='.'):
    """ Reads all files an joins into a single stream """
    for part in parts:
        for key, value in part.items():
            if not isinstance(value, list):
                with open(os.path.join(basepath, value), encoding="utf8") as fstrm:
                    stream.write('=={}:{}==\n'.format(key, value))
                    stream.write(fstrm.read())
            else:
                print('\n\n=={}=='.format(key), file=stream)
                join_parts(value, stream, basepath)

def split_parts(singlefilepath, basepath='.'):
    """ Splits one-file into parts and creates separate files for each-one """
    with open(singlefilepath) as fstm:
        text = fstm.read()

    # TODO pages should produce yaml!
    pages = {}
    result = re.split(r'==([\w\s\-]+):([\w\s\-/]+.md)==', text)
    pattern = re.compile(r'\n==([\w\s]+)==')

    for index, part in enumerate(result):
        if part.endswith('.md'):
            fpath = part
            title = result[index-1]
            content = result[index+1]
            pages.update({title: fpath})

            found = pattern.search(content)
            if found:
                #pages[found.groups()[0]] = []
                # TODO finish this
                content = pattern.sub('', content).strip()


            fpath = os.path.join(basepath, fpath)
            dirname = os.path.dirname(fpath)
            if not os.path.exists(dirname):
                os.makedirs( dirname )

            with open(fpath, 'wt') as ofstream:
                ofstream.write(content)

    _LOGGER.info(pages)

def split_file():
    """ Splits single into multiple documents"""
    split_parts('d1.1-report_v3.txt', basepath='new-docs')

def join_files():
    """
    Default implementation
    """
    mkdocs = yaml.load(open('mkdocs.yml').read())
    # mkdocs.keys()

    output_filename = os.path.basename( mkdocs.get('docs_dir', 'report') ) + '.txt'
    _LOGGER.info('Creating %s ...', output_filename)

    with open(output_filename, 'wt', encoding="utf8") as fstrm:
        join_parts(mkdocs['pages'], fstrm, mkdocs['docs_dir'])


if __name__ == '__main__':
    join_files()
    #split_file()
