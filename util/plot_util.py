import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re

PRECISION = 1.e-10


def nanmap(val, fillval=0, force_type=False):
    if not force_type:
        if np.isnan(val):
            result = fillval
        else:
            result = val
    else:
        try:
            if np.isnan(val):
                result = fillval
            else:
                result = val
        except TypeError:
            result = val
    return result


def reverse_nanmap(val, tofill=0.):
    if val == tofill:
        return np.nan
    else:
        return val


def nonzero_map(val):
    if val == 0.:
        return PRECISION
    else:
        return val


def othermap(val, keys, other_key='Other'):
    if val in keys:
        return val
    else:
        return other_key


def safe_dict(x, dictionary):
    try:
        y = dictionary[x]
    except KeyError:
        y = x
    return y


def map_or_other(x, dictionary, other_key='Other'):
    if x in dictionary.keys():
        return dictionary[x]
    else:
        return other_key


def shade(ax, group_size, num_bars):
    for i in np.arange(-0.5, -0.5 + num_bars, group_size):
        if (i + 0.5) / group_size % 2 == 0:
            ax.fill_betweenx(np.arange(ax.get_ylim()[0], ax.get_ylim()[1]), i, i + group_size, zorder=0,
                             facecolor='gainsboro', alpha=1)
        else:
            pass
    return ax


def fillnan(x, fill=0.):
    if np.isnan(x):
        return fill
    else:
        return x


def generic_plot(data, kind='bar', unstacked=False, color=None, title='', ylabel='', xlabel='',
                 fontsize=12, filename=None, output_directory='', fmt='png', rot=0, ylim=None, style=None, legend=True,
                 long_labels=False, linestyle=None):
    if (kind == 'bar' or kind == 'area' or kind == 'barh') and unstacked == False:
        stacked = True
    else:
        stacked = False
    if linestyle:
        ax = data.plot(kind=kind, fontsize=fontsize, stacked=stacked, color=color, rot=rot, style=style, legend=legend,
    	    linestyle=linestyle)
    else:
	    ax = data.plot(kind=kind, fontsize=fontsize, stacked=stacked, color=color, rot=rot, style=style, legend=legend)
    ax.set_title(title, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_xlabel(xlabel, fontsize=fontsize)

    if rot == 0 and kind == 'bar' and not long_labels:
        # xtick_labels = ax.get_xticklabels()
        xtick_labels = [re.sub(' ', '\n', str(x)) for x in data.index]
        ax.set_xticklabels(xtick_labels, fontsize=fontsize - 2)

    if legend:
        handles, labels = ax.get_legend_handles_labels()
        ldg = [ax.legend(handles=handles[::-1], labels=labels[::-1], fontsize=fontsize, bbox_to_anchor=[1, 1])]
    else:
        ldg = []

    if ylim is not None:
        ax.set_ylim(ylim)

    if filename is None:
        if title == '':
            raise RuntimeError('Either title or filename must be specified')
        else:
            filename = title
    plt.savefig(os.path.join(output_directory, filename + '.' + fmt),
                format=fmt, bbox_extra_artists=ldg,
                bbox_inches='tight', dpi=600)
    return ax
