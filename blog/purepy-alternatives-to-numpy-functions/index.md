<!--
.. title: Pu(re)Py alternatives to Numpy functions
.. slug: purepy-alternatives-to-numpy-functions
.. date: 2020-05-25 09:56:40 UTC+02:00
.. tags: python
.. category: 
.. link: 
.. description: 
.. type: text
.. status: private
-->

I've recently been working on an Android app with the [Kivy]() package. While Kivy allows you to 
do many cool things in a multi-platform way, the fact that your app could be run on a phone 
excludes certain things right now. Especially when the app needs to do some numerically related
operations, my  first go to is to ```import numpy as np ``` and then ```import scipy``` and then 
proceed with writing the rest of the module. But, uh-uh, this doesn't work so well while 
packaging the app into an Android app. I've noticed the app size itself bloats up a lot. This makes
sense because the NumPy and SciPy provide the amazing functions only because of their comprehensive
and solid range of capabilities. Handling more things definitely means a larger codebase. The second 
reason is that many  of the powerful thingss you get used to while running code on a laptop aren't
(yet?) there on a phone (or other computing) type system. For instance, a lot of the Numpy numerical
functions rely on various lower-level libraries *not* written in Python, but instead on packages written 
in  C++ (OpenBLAS) and/or C (Intel Math Kernel Library). 


0--- OOOOPS NOPE - YOU CAN DISTRIBUTE NUMPY ON ANDROID! 
