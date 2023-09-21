# all imports
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np

# text sizes
BIG = 16
MID = 12
SML = 8

# redefine the defaults for plots
def SetStyle() :     
    # figure
    mpl.rcParams['figure.figsize']  = 6, 4  # figure size in inches
    mpl.rcParams['figure.dpi']      = 150   # dots-per-inch
    # axes
    mpl.rcParams['axes.titlesize']  = BIG   # size of title
    mpl.rcParams['axes.titlepad']   = BIG   # space between title and plot 
    mpl.rcParams['axes.labelsize']  = MID   # font size of the x and y labels
    mpl.rcParams['axes.labelpad']   = SML   # space between label and axis
    # ticks
    mpl.rcParams['xtick.labelsize'] = SML   # font size of the tick labels
    mpl.rcParams['ytick.labelsize'] = SML   # font size of the tick labels
    # legend
    mpl.rcParams['legend.fontsize'] = SML   # font size of the legend lables  
    # lines 
    mpl.rcParams['lines.linewidth'] = 1     # line width in points

# save plot 
def Save(filename) :
    plt.savefig(    filename,
                    bbox_inches ="tight",
                    pad_inches=0.05,
                    facecolor='w',
                    edgecolor='w'
    )

def PlotXY(
    x: np.array,        # x axis data points
    y: np.array,        # y axis data points
    xlab: str,          # label on x axis 
    ylab: str,          # label on y axis
    color = 'k',        # color of the line 
    xlim: list = None,  # x axis range 
    ylim: list = None,  # y axis range 
    fileName: str = ''  # filename to save the figure as
) : 
    """Basic plotting function for x and y data arrays."""
    # formatting 
    SetStyle()
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    if(xlim != None) : plt.xlim(xlim)
    if(ylim != None) : plt.ylim(ylim)
    ax = plt.gca()
    ax.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax.grid()
    # data
    plt.plot(x,y,color=color)
    # finish 
    if(fileName != '') : Save(fileName)
    plt.show()
    plt.close()

def PlotMultiXY(
    x: list[np.array],  # x axis data points
    y: list[np.array],  # y axis data points
    xlab: str,          # label on x axis 
    ylab: str,          # label on y axis
    color: list,        # color of the line 
    linestyle: list,    # style of each line 
    legend: list,       # lables for xy pair on legend
    xlim: list = None,  # x axis range
    ylim: list = None,  # y axis range
    hideY: bool = False,
    fileName: str = ''  # filename to save the figure as
) : 
    """Basic plotting function for x and y data arrays."""
    # formatting 
    SetStyle()
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    if(xlim != None) : plt.xlim(xlim)
    if(ylim != None) : plt.ylim(ylim)
    if(hideY) : plt.tick_params(axis='y', which='both', labelleft=False)
    ax = plt.gca()
    ax.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax.grid()
    # data
    for xl,yl,cl,ll,ls in zip(x,y,color,legend,linestyle) : 
        plt.plot(xl, yl,
                 color=cl, alpha=0.7,
                 linestyle=ls, linewidth=1,
                 label=ll)
    plt.legend()
    # finish 
    if(fileName != '') : Save(fileName)
    plt.show()
    plt.close()

def PlotMultiXY_DualY(
    # y axis 1
    x_ax1: list[np.array],  # x axis data points
    y_ax1: list[np.array],  # y axis data points
    ylab_ax1: str,          # label on y axis   
    color_ax1: list,        # color of the line 
    linestyle_ax1: list,    # style of each line 
    legend_ax1: list,       # lables for xy pair on legend
    # y axis 2
    x_ax2: list[np.array],  # x axis data points
    y_ax2: list[np.array],  # y axis data points
    ylab_ax2: str,          # label on y axis
    color_ax2: list,        # color of the line 
    linestyle_ax2: list,    # style of each line 
    legend_ax2: list,       # lables for xy pair on legend
    # shared properties 
    xlab: str,              # label on x axis 
    xlim: list = None,      # x axis range
    ylim: list = None,      # y axis range
    fileName: str = ''      # filename to save the figure as
) : 
    """Basic plotting function for x and y data arrays.""" # Help with two y axis: https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html 
    # make figure 
    fig, ax1 = plt.subplots()
    # plot ax1 lines
    ax1.set_ylabel(ylab_ax1, color=color_ax1[0])
    ax1.tick_params(axis='y', labelcolor=color_ax1[0])
    for xl,yl,cl,ll,ls in zip(x_ax1,y_ax1,color_ax1,legend_ax1,linestyle_ax1) : 
        ax1.plot(xl, yl,
                 color=cl, alpha=0.7,
                 linestyle=ls, linewidth=1,
                 label=ll)
    # plot ax 2 lines 
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel(ylab_ax2, color=color_ax2[0])
    ax2.tick_params(axis='y', labelcolor=color_ax2[0])
    for xl,yl,cl,ll,ls in zip(x_ax2,y_ax2,color_ax2,legend_ax2,linestyle_ax2) : 
        ax2.plot(xl, yl,
                 color=cl, alpha=0.7,
                 linestyle=ls, linewidth=1,
                 label=ll)
    # formatting 
    SetStyle()
    ax1.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax1.grid()
    ax1.set_xlabel(xlab)
    if(xlim != None) : plt.xlim(xlim)
    if(ylim != None) : plt.ylim(ylim)
    fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    # finish 
    if(fileName != '') : Save(fileName)
    plt.show()
    plt.close()