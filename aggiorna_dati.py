#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Scarica da dropbox un file zip con la cartella html/data di compare-to-osm
# per l'Italia

import os
import shutil
from subprocess import call


# Inizializzazione
DROPBOX_URL = ("https://dl.dropboxusercontent.com/u/41550819/OSM/"
               "compare-to-osm_italy_data/projects/italy.zip")
# compare-to-osm_italy_data/projects
projects_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  "projects")
ZIP_FILE = os.path.join(projects_directory, DROPBOX_URL.split("/")[-1])
# compare-to-osm_italy_data/projects/italy
project_directory = os.path.join(projects_directory,
                                 ZIP_FILE.split("/")[-1][:-4])
html_directory = os.path.join(project_directory, "html")
data_directory = os.path.join(html_directory, "data")

# Cancella dati vecchi, scarica file compresso e crea la directory con le tile
if os.path.isfile(ZIP_FILE):
    print "\n- Cancella vecchio file compresso: \n{0}".format(ZIP_FILE)
    os.remove(ZIP_FILE)
if os.path.isdir(data_directory):
    print "\n- Cancella vecchia directory: \n{0}".format(data_directory)
    shutil.rmtree(data_directory)

print "\n- Scarica il file compresso"
call("wget {0} -O {1}".format(DROPBOX_URL, ZIP_FILE), shell=True)

print "\n- Decomprimi file zip e crea projects/italy/html/data"
call("unzip {0} -d {1}".format(ZIP_FILE, html_directory), shell=True)
