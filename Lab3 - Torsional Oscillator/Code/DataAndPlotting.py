# imports 
import numpy as np
import matplotlib as mpl
import matplotlib.colors as mc
import matplotlib.pyplot as plt 
import colorsys


def darken_color(color, amount=1.4) :
    """darkens a color"""
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])

# color palett # https://coolors.co/4d9de0-e15554-e1bc29-3bb273-7768ae
color5 = ['#4D9DE0','#E15554','#E1BC29','#3BB273','#7768AE'] 
color5_dark = [darken_color(c) for c in color5]

def SetStyle() :    
    """# redefine the defaults for plots"""
    # text sizes
    BIG = 16
    MID = 12
    SML = 8
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

def Save(filename) :
    """Save plot"""
    plt.savefig(    filename,
                    bbox_inches ="tight",
                    pad_inches=0.05,
                    facecolor='w',
                    edgecolor='w'
    )

def UnpackTable(fname: str) -> dict[str,np.array] :
    """Get a table dictionary like {x: xdata, y: ydata} from a CSV file containing data""" 
    # get data from the csv file
    arr = np.genfromtxt(fname, delimiter=",", dtype=str)
    # separate column names and data arrays 
    cols = np.array(arr[0 ], dtype=str)
    data = np.array(arr[1:], dtype=float).T # transpose to get x and y
    # build dictionary to hold the table {x: xdata, y: ydata}
    table = {}
    for col, dat in zip(cols,data) : 
        table[col] = dat
    return table

def UnpackAllTables(filenames: dict[str,str]) -> dict[str, dict[str, np.array]] : 
    """Unpack all tables in the filenames dictionary."""
    tables: dict[str, dict[str, np.array]] = {}
    for experiment, file in filenames.items() :
        # extract data from file 
        tables[experiment] = UnpackTable(file)
        # print some helpful info 
        print(experiment, 'columns:\t', list(tables[experiment].keys() ))
    return tables

def AxText(ax,txt,x,y,fontsize=8) : 
    ax.text(x,y, # x,y 
            txt, # string
            transform=ax.transAxes,         # use axis coordinants
            horizontalalignment='left',    # alignment 
            fontsize=fontsize               # font size
    )

def AxTextBL(ax, txt, fontsize=8): # BL bottom left 
    AxText(ax,txt,0.02,0.05,fontsize=fontsize)

def AxTextTL(ax, txt, fontsize=8): # TL top left 
    AxText(ax,txt,0.02,0.90,fontsize=fontsize)

def AxTextBBL(ax,txt,fontsize=8):
    AxText(ax,txt,0.02,0.15,fontsize=fontsize)

def AxTextTTL(ax, txt, fontsize=8):
    AxText(ax,txt,0.02,0.80,fontsize=fontsize)