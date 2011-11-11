.. contents::

Introduction
============

This package wraps the various bibliograph parsers from `bibliograph.parsing <http://pypi.python.org/pypi/bibliograph.parsing>`_,
and replaces the registered named utilities with their wrapped version.

The wrappers copy the imported keywords to the subject field, so that keywords from an imported citation end up in the CMFBibliography keywords field and in Plone`s standard ``tags`` field.

Installation
============

Just add the package to your Plone instance. The configuration and setup is done via `z3c.autoinclude <http://pypi.python.org/pypi/z3c.autoinclude>`_.
 
