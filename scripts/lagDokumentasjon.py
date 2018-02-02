#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import codecs
import warnings
import errno


def extractDoc(filename):

   # Extract text in file that are
   # between /*! and */
   
    macroFile = codecs.open(filename, "r", "latin-1")
    macroFileContent = macroFile.readlines()
    macroFile.close()

    doc = ""
    extract = False
    for i in macroFileContent:
        if len(i.split()) == 2:
            if i.split()[0] == "%macro":
                doc += '''
## {0}

'''.format(i.split()[1])
        if extract and "*/" in i:
            extract = False
        if extract:
            doc += i
        if "/*!" in i:
            extract = True
    return(doc)

def findSASfiles(folder):
   SASfiles = []
   for fn in os.listdir(folder):
      readFile = False
      try:
         if fn.endswith(".sas"):
            readFile = True
         else:
            readFile = False
      except:
         readFile = False

      if readFile:
         SASfiles.append(folder + fn)

   return(SASfiles)

folder = "./"
listofMacros = findSASfiles("./")
listofMacros += findSASfiles("./sas/")

docFolder = "./docs/"

try:
    os.makedirs(docFolder)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

index = ""
for i in listofMacros:
   heading = '''[Ta meg tilbake.](./)

# Oversikt over innholdet i filen *{0}*

'''.format(i)

   doc = extractDoc(i)
   
   filename = i.split("/")[-1]
   if doc != "":
      index += "- [{0}]({1})\n".format(filename,filename.split(".")[0])
      docFile = codecs.open(docFolder+filename.split(".")[0]+".md", "w", "utf-8")
      docFile.write(heading + doc)
      docFile.close()
   else:
      warnings.warn("ADVARSEL: Filen {0} er ikke dokumentert!".format(filename))
      index += "- Filen {} er ikke dokumentert.\n".format(filename)
      
indexHeading = ""
for i in open("./docs/indexHead.md","r").readlines():
   indexHeading += i

indexFile = open(docFolder+"index.md", "w")
indexFile.write(indexHeading+index)
indexFile.close()


