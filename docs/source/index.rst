.. AiiDA-Python documentation master file, created by
   sphinx-quickstart on Fri Nov  3 12:00:27 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to AiiDA-Python's documentation!
========================================

AiiDA is a powerful framework for managing and executing computational workflows. It provides a flexible and scalable platform for automating scientific simulations and data analysis. AiiDA allows you to easily integrate and execute your Python code as ``CalcJob`` on remote computers.

The AiiDA-Python plugin is specifically designed to extend the functionality of the AiiDA framework. It enables you to run Python code on external computers, making it easier to leverage the computational resources available on remote systems.

Usage of the AiiDA-Python plugin is straightforward. To get started, you need to inherit the ``CalcJobPython`` class and override the ``run_python`` method. This allows you to customize the execution of your Python code within the AiiDA framework. Additionally, the plugin automatically generates a parser, eliminating the need for you to write your own.

It's important to note that the AiiDA-Python plugin is currently in the early stages of development. However, it is actively maintained and continuously improved to provide a reliable and efficient solution for executing Python code on remote computers.

To learn more about using the AiiDA-Python plugin and its capabilities, please refer to the ``usage.rst`` file in this documentation.

.. note::

   This project is under active development and it is in early stage.

This plugin is published under MIT license.

.. toctree::
   :maxdepth: 2

   usage.rst
   contribution.rst
   apidoc.rst

Indices and Tables
==================

In addition to the main content, this documentation also provides the following indices and tables for easy navigation:

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

We hope this documentation helps you understand and utilize the AiiDA-Python plugin effectively. If you have any further questions or need assistance, please don't hesitate to ask.


