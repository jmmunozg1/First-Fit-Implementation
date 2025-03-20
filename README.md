# (C)ontinuous (M)emory (A)lgorithms (cma)

This is is a simulator of continuous memory algorithms:

   * first fit
   * best fit
   * worst fit

Each algorithm receives three parameters:
   * `mem_avail`: a list of tuples, base and limit.
   * `req`: a size request for memory.
   * `index` position on the `mem_avail`. This is a circular index: `(index % len(mem_avail))`.

Each algorithm returns two possible values: `None` if the
request cannot be fulfilled, or a quadruple:
   * `mem_avail`: a list of tuples of memory that are newly available (could be empty).
   * `base`: new base where the requested process start.
   * `limit`: new limit.
   * `index`: an index on the `mem_avail` where the request was found. If the
     memory were exhausted, the next valid position would be available.

# Test

First, set the `PYTHONPATH` variable replace (`<path-of-your-project`)
with your directory path.

Linux

```shell
$ export PYTHONPATH=$PYTHONPATH:<path-of-your-project>
```

Windows

```shell
> PYTHONPATH=%PYTHONPATH%;<path-of-your-project>
```

Running the test, replace with the name of your algorithm implementation: `first`, `best`, `worst`.

```shell
$ python3 -m unittest test/test_basic_<your_algorithm>_fit.py
```

