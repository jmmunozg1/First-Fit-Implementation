# (C)ontinuos (M)emory (A)lgorithms (cma)

This is is a simulator of continuos memory algorithms:

   * first fit
   * best fit
   * worst fit

Each algorithm receives three paramaters:
   * `mem_avail` a list of tuples base and limit
   * `req` a request of memory
   * `index` a index, this is a circular index

Each algorithm returns two possible values: `None` if the
request cannot fullfil, or a cuadruple:
   * `mem_avail` a list of tuples of memory new available (could be empty).
   * `base` new base where the process start to
   * `limit` new limit
   * `index` index on the `mem_avail` where the request was found, if the
     memory was exhausted the next possition available.
