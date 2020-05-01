Title: Simultaneous code and docs: a safety net for your project
Date: 2020-04-04 08:20
Category: scientific computing

In the past I always used to either badly document my code properly or ignore it completely. The focus was to get the job done and 
to get out. Nowadays, however, things have changed a *lot*, and I really only have the [Sphinx](http://www.sphinx-doc.org/en/stable/) project to blame :P. Documenting
your code as it's being written helps in a bunch of ways, and the person who benefits from it the most is *futureyou*. I've thanked 
*pastme* a zillion times by now because the current project I'm working on has grown to be a more than a few files, and I was 
quite afraid of not being able to keep track of stuff. However, this time I really decided to write [NumPy](https://numpydoc.readthedocs.io/en/latest/format.html) style docstrings on all functions that are more than a two lines, and with a little bit of Sphinx magic, and some [ReadTheDocs](https://docs.readthedocs.io/en/stable/) hosting, the result is a beautiful webpage that  I keep visiting myself just because it's rewarding seeing something nice.<!-- TEASER_END-->

The problem I tend to have with a code base that gets large enough is that I forget which functions do what and their input and output formats. 
There is a limit to the number of things you can keep in your head over the span of a week or a month. Writing detailed documentation with 
the code is useful because it helps you keep track of how things are implemented, what is required for each function, and even keep notes 
on the limitations of different functions/objects. 

Is it worth it? Even though in the beginning there may be only five functions used repeatedly, it slows grows to seven, ten, fifteen, and that's 
way too many to keep in mind, even though I'm working with the code on a daily basis. It's only once you get knee-deep into a project that you begin 
to realise all the details that weren't so obvious from a distance.


#### Writing documentation:
In the console/command line: So you've begun your coding session, and now you  want to do <<*coolthing*>>, with <<*amazefunction*>>, but, aargh, 
do you have to specify the ```amazelevel=10``` or is it a default value? And don't you vaguely remember that the value for *amazelevel* is actually an input for <<*create_amazingness*>>? So, if past you had done a good job of it, when you  type in ```help(amazefunction)```, you'd get some information hopefully?

```
help(amazefunction)
Help on function amazefunction in module __main__:

amazefunction(amaze_type, **kwargs)
```

Disappointing?..yeah. Now however, imagine you'd actually invested a minute extra while actually writing this function, and thus saved *futureyou* a few minutes. 
This is what the output from ```help(amazefunction)``` could have looked like!

```
Help on function amazefunction in module __main__:

amazefunction(amaze_type, **kwargs)
    Creates an amazing thing. 
    
    Parameters
    ----------
    amaze_type : str
        The type of amazing object to be created.
        Needs to be one of these values ['unicorn', 'rakshasa', 'wolpertinger'] 

    Returns
    -------
    amazingness : dictionary
        The amazingness dictionary has keys
        'height', 'weight', 'powers' and other  optional
        descriptive features controlled by optional 
        arguments.

    See Also
    --------
    make_amazing_object
    check_amaze_type
```

