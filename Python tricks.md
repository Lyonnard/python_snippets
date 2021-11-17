# Python tricks

### Naming

programname.py (eventually program_name.py) tutto minuscolo.

variable, variablename, variable_name

function, functionname, function_name

Class, ClassName

CONSTANT, MAX_CONSTANT

### Plotting

- A good way to insert figures in Latex with no white borders. Good both for pdf and png saving:

  ```python
  .savefig(...,pad_inches=0)
  ```

- To reverse a logscale just use: `ax1.set_xlim((max,min))` with max and min in the reverse order. This also flips the tickmarks!

- A very useful instruction 

  ```python
  plt.setup()
  ```

- `fig.suptitle('Create figure title')`
- `array[::2]` takes every other element in an array.

### To Learn

- [ ] `try` statement
- [x] Classes
- [ ] multiprocessing