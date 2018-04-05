Read the Docs Advertising Exception List
========================================

This repository builds a filter list compatible with many ad blockers such
as AdblockPlus and uBlock Origin that whitelists advertising on Read the Docs.

Advertising on Read the Docs:

- respects your privacy (no advertiser JavaScript, no data dumps)
- only shows advertising of interest to developers
- supports open source software

Read more about `ethical advertising`_.

.. _ethical advertising: https://docs.readthedocs.io/en/latest/ethical-advertising.html


Generate the filter list
------------------------

::

    % pip install -r requirements.txt
    % ./generate.py    # output written to output/readthedocs-ads.txt
