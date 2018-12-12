## Description

Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.

## Environment

``python-3.6``

## Configure
#### Sublime Text settings for python
* Integrated code analysis
* Automatic completion of code

The above functions are not configured for you like pycharm, but you need to make some settings yourself, but pycharm is very bloated.

So the following configuration will include the following main content:

* Python code syntax and style check
* Code completion beyond other IDEs
* Jump to python standard library, third-party libraries and their own defined functions
* Format your code to comply with the PEP8 specification
* Editor settings let you write Python code that conforms to the PEP8 standard
* Smooth git integration works with git command line tools
* The settings for the sublime command line tool are used

Note: In order to prevent the newly installed plugin from taking effect, restart the sublime after each installation.

---
Open Sublime Text

Keyboard : ``Ctrl + Shift + P``

Choose : Package Control : Install Package

---
#### Setting up Python's code analysis tool: Flake

This tool has the following features:

* Analyze syntax errors
* Analyze code structure issues such as using variables that are not defined
* Analyze code that does not conform to specifications and aesthetics

So when this tool is well integrated in Sublime, it will be very helpful to write code for yourself.

By integrating Flake8 and Sublime, Flake8 is a very good tool. It is very fast in Python and has a low false positive rate. It is very suitable for code analysis and checking.

Flake8 is a command line tool that needs to be installed separately.

After installing Flake8, install the ``SublimeLinter`` 

and ``SublimeLinter-flake8`` plugins for Sublimean.

Open a SSH Window

Note : check ``python`` is in environment variable

``Install Flake8``

``pip install flake8``

If you need to upgrade this plugin later, you only need to pass the command:

``pip install --upgrade flake8``

---
#### Install SublimeLinter

``SublimeLinter`` is the code framework for ``Sublime``, which can be integrated with the ``linter`` engine such as ``Flake8`` to check our code.
And you can convert their messages into Sublime Text and display them next to our code.

``SublimeLinter`` can make ``Flake8`` and ``Sublime Text`` a perfect companion, and you can see the Flake8 message directly in the code editor.
So first we need to install ``SublimeLinter``, then we will install ``SublimeLinter-flake8`` that connects ``Flake8`` and ``SublimeLinter``.

1. Enter ``ctrl+shift+p`` as shown below, and type `` install package``, then press Enter.

2. Enter what we want to install: ``SublimeLinter``

---
#### Install SublimeLinter-flake8

Now you need to integrate SublimeLinter and Flake8, which is done here via the SublimeLinter-flake8 plugin.

Similarly, similar to the previous plugin installation method is also 
through ``ctrl+shift+p`` and enter ``SublimeLinter-flake8``

#### Configuring SublimeLinter-flake8

Open configuration

``Preference>Package Settings>SublimeLinter>Settings``

Change the "mark_style": "outline" in the user configuration to: "mark_style": "squiggly underline"

Find "lint_mode" in the configuration: "background" changed to: "lint_mode": "load_save"

---
#### Install the Anaconda Package

Code auto-completion

Many programmers want IDE tools to be able to use their auto-completion features, and Sublime doesn't have a very useful plug-in at first, until the Anaconda plug-in appears.

It provides the following features:

1. Automatic completion of code
2. Display the use of python classes, methods or functions
3. Check if the import module is valid
4. Automate the format of our code according to the PEP8 specification
5. Can jump to the definition of a function or the definition of a class

Open configuration

``Preference>Package Settings>Anaconda>Setting - User``

```
{
"anaconda_linting": false,
"pep8": false
}
```
The above configuration is because the function of this plugin and the flake8 plugin conflict with each other. It is better to use the configuration of flake8 here.

We can test some of its features:
When we enter print, it will display the parameters and documents.