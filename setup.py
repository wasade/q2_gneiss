# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Gneiss development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="q2-gneiss",
    version='0.0.1',
    packages=find_packages(),
    install_requires=['scikit-bio', 'qiime >= 2.0.0', 'q2-types'
                      'IPython >= 3.2.0', 'matplotlib >= 1.4.3',
                      'numpy >= 1.9.2', 'pandas >= 0.18.0', 'scipy >= 0.15.1',
                      'nose >= 1.3.7', 'scikit-bio>=0.4.2', 'ete3'],
    author="Jamie Morton",
    author_email="jamietmorton@gmail.com",
    description="Produce balance trees",
    license="bsd",
    url="https://github.com/biocore/gneiss",
    entry_points={
        'qiime.plugins':
        ['q2-gneiss=q2_gneiss.plugin_setup:plugin']
    }
)
