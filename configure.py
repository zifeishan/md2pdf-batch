#!/usr/bin/python

import os
import yaml

if not os.path.exists("src"):
    os.system("mkdir src")
    print "You have to put all your source file (*.tex) into src/"
    exit
if not os.path.exists("build"):
    os.system("mkdir build")

config_path = "list.yml"

f = open(config_path)
conf = yaml.load(f)
f.close()

# print conf

f = open("Makefile", 'w')
f.write("all :")
for name in conf:
    if name != "default":
        f.write(" " + name)
f.write("\n")
f.write("\n")

# input default options
default = {}
default_general_file_name = ""
if "default" in conf:
    if conf["default"].has_key("general_file_name"):
        default_general_file_name = str(conf["default"]["general_file_name"])
    for each_def in conf["default"]:
        default[each_def] = str(conf["default"][each_def])


for name in conf:
    if name != "default":
        # determine the general file name
        if conf[name].has_key("general_file_name"):
            general_file_name = str(conf[name]["general_file_name"])
        elif default_general_file_name != "":
            general_file_name = default_general_file_name
        else:
            # general_file_name = "diver"
            general_file_name = name

        f.write(name + " : " + "src/" + general_file_name + ".md "+config_path+"\n")
        # f.write("\tpandoc src/" + name + ".md -o "+ name+".tex\n")
        # f.write("\tpandoc src/"+general_file_name+".md -o GENERAL.tex\n")
        f.write("\tpandoc src/"+general_file_name+".md -o temp.tex\n")
        # f.write("\techo '\\n\\n' >>GENERAL.tex\n")
        # f.write("\tcat GENERAL.tex " + name + ".tex > temp.tex\n")

        # pdflatex multiple times for references
        for i in range(0, 2):

            f.write("\tpdflatex -jobname=\"" + name + "\" \"")

            # specific options for each school
            for each_def in conf[name]:
                if each_def != "general_file_name":
                    f.write("\\def\\" + each_def + "{" + str(conf[name][each_def]) + "} ")
            # default options for all schools
            for each_def in default:
                if each_def not in conf[name]:
                    f.write("\\def\\" + each_def + "{" + str(default[each_def]) + "} ")
            
            f.write("\\input{src/template.tex}\"\n")

        # attach cover sheet
        if 'coverpage' in conf[name] or 'coverpage' in conf['default']:
            if 'coverpage' in conf[name]:
                coverpath = conf[name]["coverpage"]
            else:
                coverpath = conf['default']["coverpage"]

            f.write("\tpdftk " + coverpath + ' ' + name + ".pdf output tmp+cover.pdf\n")
            f.write("\tmv -f tmp+cover.pdf " + name + ".pdf\n")

        # move the target to build/
        f.write("\tmv " + name + ".pdf build/"+name+".pdf\n")

        # remove the temperary logging files
        # f.write("\trm temp.tex\n")
        f.write("\trm *.log *.aux *.out\n")
        # f.write("\topen build/" + name + ".pdf\n")
        f.write("\n")

# clean target
f.write(".PHONY: clean\n")
f.write("clean:\n")
f.write("\trm *.log *.out *.aux ./build/*.pdf")

f.close()

print "configure finished"


