Developing these Whitelists
===========================


Generate these docs
-------------------

This is the command to generate the documentation you are reading now.
The first step of generating the docs is to generate the whitelists so they
are included in the docs build output.

::

    % pip install -r requirements.txt
    % cd docs && make html


Generate the whitelists
-----------------------

To generate the whitelists only locally, you can run the following:

::

    % pip install -r requirements.txt
    % ./generate-lists.py    # output written to docs/source_static/lists/


Writing whitelist filters
-------------------------

See the `AdblockPlus documentation on writing filters <https://adblockplus.org/en/filters>`_.
