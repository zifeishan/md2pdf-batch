Introduction to MD2PDF-Batch Project
====

This project aims to make the workflow to write a batch of manuscripts / reports with a same template easier.

- Write in markdowns, get papers. Help maintaining a clean paper
  repository.

- It will make a latex project easy to read: 
    - separate templates and contents
    - itemize, emph, headers... expressed in Markdown!
    - Support natural representation of tables (as in *pandoc*).
    - future work: easier figures / subfigures.

- Compatibility to latex:
    - You can use any latex environments in our markdown file.

- Support batch workflow easier by input arguments in a list:
    - You can specify input arguments in the configuration file, either applied to all, or to a single document. These arguments are passed into your LaTeX compiler --- this gives flexibility in the batch process!

What to look at
----

If you are looking at the repository to learn, make sure to look at these files:

- Source code of this document is `src/guide.md`. 
- The view is defined in `src/template.tex`.
- Input parameters are defined in `list.yml`

Workflow description
----

1. Prepare template file in `src/`. It should always only include a temp.tex file in the document:


            \begin{document}
            \input{temp}
            \end{document}

    - For any arguments you want to specify in configuration file rather
    than fixed in template, just write `\SomeName` inside template,
    and specify `Somename` in configuration list.

2. Specify your configuration list in `list.yml`, within Yaml format.
    - For arguments that apply globally (to all sub-documents), specify it in `default` object.
    - For arguments that apply to a single document, specify it in the document id object, e.g. `hw0`.
    - You can add a cover page by specifying *coverpage* argument.

3. Put all your source files in `src/`. The filename should be always `DocID.md` for system to recognize, e.g. `hw0.md`.
4. Run `python configure.py` to compile a Makefile.
5. Run `make all` to make all documents into `build` directory, or make a single document regarding to the ID in list.yml, e.g. `make hw0` to make `build/hw0.pdf`
    

Dependencies
----

- Pandoc
- Makefile
- A latex compiler


Source File Format
====

Getting Started
----

Be sure to look into this markdown file to learn use cases of markdown.

Paragraphs are split by an empty line.

Section headers can be specified:

- section: `====` or `#`
- subsection: `----` or `##`
- subsubsection: `###`

A good thing compared to \LaTeX is that you can directly use quotation marks: `"`: "Hello world".

Anything that begins with a `\` will have identical function with in LaTeX.

Other useful formats:

- **Strong**: `**Strong**`
- *Emphasis*: `*Emphasis*`
- \textsc{Small caps}: `\textsc{TextSc}`
- Comment: `<!-- Something you want to comment -->` <!-- Something you want to comment -->

### A sample unordered list

- Fruit
    - Apple <!-- (Be sure to use 4 spaces for each indent!!) -->
    * Orange <!-- (either `*` or `-` is OK) -->
- People
    * Alice
    - Barack

This can be generated from the code:

        <!-- Be sure to have 1 empty line before the list. -->

        - Fruit
            - Apple <!-- (Be sure to use 4 spaces for indents!!) -->
            * Orange <!-- (either `*` or `-` is OK) -->
        - People
            * Alice
            - Barack

### A Sample ordered list

1. Fruit
    (a) Apple
    (b) Orange
2. People
    #. Alice <!-- `#.` also gives ordered list. This is useful when you do not include *enumerate* package. -->
    #. Barack
3. Others
    1. Tim
    2. Bob

This is generated from:

        1. Fruit
            (a) Apple
            (b) Orange
        2. People
            #. Alice <!-- `#.` also gives ordered list. This is 
               useful when you do not include *enumerate* package. -->
            #. Barack
        3. Others
            1. Tim
            2. Bob


### Tables

Natural representation of tables are supported by *Pandoc*. To use them, include package `longtable` and `booktabs`.  For more about pandoc tables, see: [http://johnmacfarlane.net/pandoc/README.html#tables](http://johnmacfarlane.net/pandoc/README.html#tables).

Here is a sample table:


  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1

It is generated from following code in markdown:


          Right     Left     Center     Default
        -------     ------ ----------   -------
             12     12        12            12
            123     123       123          123
              1     1          1             1


To make floating tables with references using `table` environment in \LaTeX, see Section \ref{sec:envir}.


Environments
----
\label{sec:envir}   <!-- specifies a label for references -->

Any \LaTeX environment is supported. You can directly write it in
MarkDown.

e.g. `\begin{someEnvironment}...\end{someEnvironment}`


### Tabular

Just use latex environment 

    \begin{tabular}{lr} ... \end{tabular}

and you will get the tabular.

\vspace{0.5em}  <!-- This is a linebreak -->

\begin{center}
\begin{tabular}{lr}
\hline
(a) Number of nodes in the network & 7115\\
(b) Number of nodes with a self-edge & 0\\
(c) Number of directed edges in the network & 103689\\
\hline
\end{tabular}
\end{center}


### Tables and Figures

You can specify and refer to tables and figures as you do in \LaTeX. For example, you can refer to Table \ref{table:1}, Figure \ref{fig:1}: `Table \ref{table:1}, Figure \ref{fig:1}`.

\begin{table}[!b]
\centering
\caption{Some table}
\label{table:1}
\vspace{0.5em}
\centering
\begin{tabular}{lrr}
\hline
Name & Some number & Some other number\\
\hline
Alice & 5.5307 & 5.5576\\
Bob & 5.5305 & 4.8091\\
Cathy & 5.5284 & 15.8686\\
\hline
\end{tabular}
\end{table}


\begin{figure}[!t]
\centering
\includegraphics[width=0.45\textwidth]{img/sample1.eps}
\caption{Sample Figure}
\label{fig:1}
\end{figure}

You can use and refer to subfigures like following: Figure \ref{fig:sub1}: `Figure \ref{fig:sub1}`.

\begin{figure*}[!t]
\centering
\subfigure[Some Subfigure\label{fig:sub1}]{ 
    \includegraphics[width=0.3\textwidth]{img/sample2.eps}
}
\subfigure[Some Other subfigure]{ 
    \includegraphics[width=0.3\textwidth]{img/sample3.eps}
}
\caption{Sample figure with subfigures}
\label{fig:2}
\end{figure*}

Be sure to include have specific packages.



### Code Blocks with specific language

\begin{lstlisting}[language=python]
#!/usr/bin/python
print 'Hello World!'
lan = 'Python'
print 'This is a sample code block in %s' % lan!
\end{lstlisting}

You can use environment `\begin{lstlisting}[language=python]...`, and craft your python/C++/Matlab code blocks...



Bibliography
----

We believe that it is not common that you include bibs in this batch project. 

Be aware that our generated Makefile does not include a bibtex command. You can try to modify *configure.py* if you want. Note that the proper process should be *pdflatex, bibtex, then pdflatex twice*.

If you really want this, please send me a note.  Actually we will have bib support in the coming non-batch version of our workflow.



\section*{Acknoledgement}

Big thanks to Winnie Liu, for coming out the ideas and initial efforts!

Thanks for Scott Cheng for pushing this project for release.
