Refractive index of air
=======================

.. _NIST online refractive index of air calculator: 
    http://emtoolbox.nist.gov/Wavelength/Documentation.asp
.. _pip: http://pypi.python.org/pypi/pip
.. _easy_install: packages.python.org/distribute/easy_install.html

Code for calculating refractive index of air, under varying atmospheric
conditions, is provided in this module. Functions for conversion of
wave length of light in vacuum to that in air, and vice-versa are also
defined.

The code is based on the documentation for the `NIST online refractive
index of air calculator`_.

Examples
--------

Refractive index can be calculated using two different equations: one
due to Edlén and another due to Ciddor.

::

  >>> ref_index.ciddor(wave=633.0, t=20, p=101325, rh=20)
  1.0002716285340578
  >>> ref_index.edlen(wave=633.0, t=20, p=101325, rh=20)
  1.0002716291691649
  >>> ref_index.edlen(wave=633.0, t=20, p=101325, rh=80)
  1.0002711197635226
  >>> ref_index.ciddor(wave=633.0, t=20, p=101325, rh=80)
  1.0002711183472626
  >>> ref_index.edlen(wave=633.0, t=60, p=101325, rh=80)
  1.0002339748542823
  >>> ref_index.ciddor(wave=633.0, t=60, p=101325, rh=80)
  1.0002340241754055

Conversion of wave length of light in vacuum to that in air, and
vice-versa. Both of these functions use the Ciddor equation, as
implemented in ``ciddor_ri()`` and ``ciddor()``.

::

  >>> ref_index.vac2air(633.0)
  632.82500476826874
  >>> ref_index.air2vac(632.82500476826874)
  633.00000139949032

  >>> ref_index.vac2air(np.array([633.0, 550.0, 400.0]))
  array([ 632.82500477,  549.84723175,  399.88692724])
  >>> x = ref_index.vac2air(np.array([633.0, 550.0, 400.0]))
  >>> ref_index.air2vac(x)
  array([ 633.0000014 ,  550.00000164,  400.00000243])


Note that the reversibility of ``air2vac()`` is ~1e-5nm.

Default temperature is 15∘C, pressure is 101325Pa, relative humidity is
0, and CO2 concentration is 450µmole/mole. All these can be changed.

::

  >>> ref_index.vac2air(633.0, t=20, p=100000.0, rh=50)
  632.83051710791892
  >>> ref_index.air2vac(632.83051710791892, t=20, p=100000.0, rh=50)
  633.00000131884678


For more details please see the docstring for the module. Detailed
description of the equations can be found in the `NIST documentation`__.

__ `NIST online refractive index of air calculator`_

Installation
------------

The module can be installed using `pip`_ and `easy_install`.

::

  $ pip install ref_index

or, 

::

  $ easy_install ref_index


Credits
-------

All equations used in this module come from the documentation for the
`NIST online refractive index calculator`__, written by Jack A. Stone
and Jay H. Zimmerman. 

__ `NIST online refractive index of air calculator`_

Please send comments and suggestions to the email id `prasanthhn` in
the ``gmail.com`` domain.
