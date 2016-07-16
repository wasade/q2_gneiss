# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Gneiss development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime
import skbio

from qiime.plugin import Plugin, Metadata

import q2_gneiss
from q2_types import FeatureTable
from gneiss.balances import balanceplot, balance_basis
from os.path import join


def balanceplot(output_dir: str, sample_metadata: qiime.Metadata,
                otu_table: FeatureTable) -> None:

    mf = sample_metadata.to_dataframe()

    return None


plugin = Plugin(
    name='gneiss',
    version=q2_gneiss.__version__,
    website='https://github.com/biocore/gneiss',
    package='q2_gneiss'
)

plugin.visualizers.register_function(
    function=balanceplot,
    inputs={'otu_table': FeatureTable},
    parameters={'sample_metadata': Metadata},
    name='Visualize balance trees',
    description='Generate balance tree visualization.'
)
