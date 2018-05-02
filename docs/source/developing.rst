Developing these lists
======================


Generate these docs
-------------------

This is the command to generate the documentation you are reading now.
The first step of generating the docs is to generate the lists so they
are included in the docs build output.

::

    % pip install -r requirements.txt
    % cd docs && make html


Generate the lists
------------------

To generate the lists only locally, you can run the following:

::

    % pip install -r requirements.txt
    % ./generate-lists.py    # output written to docs/source_static/lists/


Writing list filters
--------------------

See the `AdblockPlus documentation on writing filters <https://adblockplus.org/en/filters>`_.
