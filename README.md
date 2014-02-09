MD2PDF-Batch Project
====

A tool to translate markdown files to PDF in batch, using fixed latex templates and descriptive input arguments. Best used in course assignments!

This project aims to make the workflow to write a batch of manuscripts / reports with a same template easier.

- Write in markdowns, get papers. Help maintaining a clean paper
  repository.

- It will make a latex project easy to read: 
  - separate templates and contents
  - itemize, emph, headers... expressed in Markdown!
  - future work: easier figures / subfigures, and tables.

- Compatibility to latex:
  - You can use any latex environments in our markdown file.

- Support batch workflow easier by input arguments in a list:
  - You can specify input arguments in the configuration file, either applied to all, or to a single document. These arguments are passed into your LaTeX compiler --- this gives flexibility in the batch process!


Workflow description
----

1. Prepare template file in ```src/```. It should always only include a temp.tex file in the document:

    \begin{document}
    \input{temp}
    \end{document}

  For any arguments you want to specify in configuration file rather
  than fixed in template, just write ```\SomeName``` inside template,
  and specify ```Somename``` in configuration list.

2. Specify your configuration list in ```list.yml```, within Yaml format.
    - For arguments that apply globally (to all sub-documents), specify it in ```default``` object.
    - For arguments that apply to a single document, specify it in the document id object, e.g. ```hw0```.
    - You can add a cover page by specifying *coverpage* argument.


3. Put all your source files in ```src/```. The filename should be always ```DocID.md``` for system to recognize, e.g. ```hw0.md```.
4. Run ```python configure.py``` to compile a Makefile.
5. Run ```make all``` to make all documents into ```build``` directory, or make a single document regarding to the ID in list.yml, e.g. ```make hw0``` to make ```build/hw0.pdf```
    

Dependencies
----
- [pandoc](http://johnmacfarlane.net/pandoc/installing.html) is a must. 
  - If you are using Mac, we recommend you to download the package from [Here](https://code.google.com/p/pandoc/downloads/list), rather than using port / brew.
- makefile
- a latex compiler
- **Recommended**: Sublime Text and its plugin *LaTeXTools*.

Quick Guide
----

For more information, download the quick guide or find it in project file: https://github.com/zifeishan/md2pdf-batch/blob/master/guide.pdf
