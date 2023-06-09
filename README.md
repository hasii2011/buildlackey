[![CircleCI](https://dl.circleci.com/status-badge/img/gh/hasii2011/buildlackey/tree/master.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/hasii2011/buildlackey/tree/master)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



## Rationale

These utilities are meant to help me with my repositories and their maintenance.

## Dependencies

These utilities work best using the following opinionated dependencies

* Python [virtual environments](https://realpython.com/python-virtual-environments-a-primer/) on a per project/repository basis
*  [direnv](https://direnv.net) to set up the project virtual environment and any necessary environment variables
* Building using setup.py and the [build](https://pypi.org/project/build/) module to create source and binary distributions.  The documentation is [here](https://pypa-build.readthedocs.io/en/stable/)
* Using [pypi](https://pypi.org/) for source and binary distributions
* A correctly setup [$(HOME)/.pypirc](https://packaging.python.org/en/latest/specifications/pypirc/) for easy interaction with [twine](https://pypi.org/project/twine/) and [pypi](https://pypi.org/)

## Required Environment Variables

The above commands depend on the following environment variables.

```bash
PROJECTS_BASE             -  The local directory where the python projects are based
PROJECT                          -  The name of the project;  It should be a directory name
```

 An example, of a PROJECTS_BASE is:

```bash
export PROJECTS_BASE="${HOME}/PycharmProjects" 
```

This should be set in your shell startup script.  For example `.bash_profile`.

The PROJECT environment variable should be set on a project by project basis.  I recommend you use [direnv](https://direnv.net) to manage these.  An example of a .envrc follows:

```bash
export PROJECT=pyutmodel
source pyenv-3.10.6/bin/activate
```


## Python Console Scripts

buildlackey means to handle this problem by providing a set of Python command line scripts to automate updating the first three of the above dependency specification locations

* runtests -- queries repositories for their latest release version
* runmypy -- creates a dependency specification for a project 
* cleanup -- updates the supported dependency locations using the generated specification
* deploy -- 
* prodpush --

## Usage

* runtests
* runmypy
* cleanup
* deploy
* prodpush

___

Written by <a href="mailto:email@humberto.a.sanchez.ii@gmail.com?subject=Hello Humberto">Humberto A. Sanchez II</a>  (C) 2023

---

## Note
For all kind of problems, requests, enhancements, bug reports, etc.,
please drop me an e-mail.


![Humberto's Modified Logo](https://raw.githubusercontent.com/wiki/hasii2011/gittodoistclone/images/SillyGitHub.png)

I am concerned about GitHub's Copilot project



I urge you to read about the
[Give up GitHub](https://GiveUpGitHub.org) campaign from [the Software Freedom Conservancy](https://sfconservancy.org).

While I do not advocate for all the issues listed there I do not like that a company like Microsoft may profit from open source projects.

I continue to use GitHub because it offers the services I need for free.  But, I continue to monitor their terms of service.

Any use of this project's code by GitHub Copilot, past or present, is done without my permission.  I do not consent to GitHub's use of this project's code in Copilot.

A repository owner may opt out of Copilot by changing Settings --> GitHub Copilot.

I have done so.

