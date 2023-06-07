# author: Tang Tiong Yew
# email: tiongyewt@sunway.edu.my
# Project Title: Deep Bilio: A Python Tool for Deep Learning Biliometric Analysis
# Copyright 2023
#

# import shinyswatch
import shiny
from shiny import *
from shiny.types import *
from shinywidgets import output_widget, render_widget

import plotly.graph_objs as go
import plotly.express as px
# import qgrid
# from shinywidgets import *

from pathlib import Path
import pandas as pd
# import textwrap
import traceback
# from pyBibX.base import pbx_probe
# from google.colab import data_table
from userinterface import *
from deepbiblio import *
from utils import *

# Widgets
# from ipydatagrid import DataGrid

import os
import copy
import openpyxl
import grid

import numpy as np

import zipfile

import warnings

# def messageItem2(from_, message, icon=shiny.icon("user"), time=None, href=None, inputId=None):
#     if href is None:
#         href = "#"
#     return shiny.tags.li(shiny.tags.a(id=inputId, class_="action-button" if inputId else None,
#                                       href=href, target="_blank", children=[icon,
#                                       shiny.tags.h4(from_, shiny.tags.small(shiny.icon("clock-o"), time)) if time else None,
#                                       shiny.tags.p(message)]))

def initial(values):
    values["results"] = ["NA"]
    values["log"] = "working..."
    values["load"] = "FALSE"
    values["field"] = values["cocngrams"] = "NA"
    values["citField"] = values["colField"] = values["citSep"] = "NA"
    values["NetWords"] = values["NetRefs"] = values["ColNetRefs"] = [[float('nan')]]
    values["Title"] = "Network"
    values["Histfield"] = "NA"
    values["histlog"] = "working..."
    values["kk"] = 0
    values["histsearch"] = "NA"
    values["citShortlabel"] = "NA"
    values["S"] = ["NA"]
    values["GR"] = "NA"


    return values