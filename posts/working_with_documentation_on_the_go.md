Title: On the advantages of simultaneous code and docs
Date: 2020-04-04 08:20
Category: scientific computing

In the past I always used to either neglect documenting my code properly or ignore it completely. The focus was to get the job done and 
to get out. Nowadays, however, things have changed a *lot*, and I really only have the [Sphinx]() project to blame :P. Documenting
your code as it's being written helps in a bunch of ways, and the person who benefits from it the most is future you. I've thanked 
pastme a zillion times by now because the current project I'm working on has grown to be a more than a few modules, and I was 
quite afraid of not being able to keep track of stuff. However, this time I really decided to write [NumPy]() style docstrings 
on all functions that are more than a few lines, and with a little bit of Sphinx magic, and some [ReadTheDocs]() hosting, the
result is a beautiful webpage that  I keep visiting myself just because it's rewarding seeing something beautiful.  It kind of 
reminds me of  the first time I used LaTex to generate a manuscript. 

The problem I tend to have with a code base that gets large enough is that I forget which functions do what and their input formats. 
Even though in the beginning there were only about five functions used commonly, over time, it becomes, seven, ten, fifteen, and that's 
way too many to keep in mind, even though I'm working with the code on a daily basis. This is where having consistent documentation helps 
like crazy at multiple places:

    1. In the console/command line: So you've begun your coding session, and now you  want to do <<*coolthing*>>, with <<*amazefunction*>>, but, aargh, 
do you have to specify the *amazelevel* or is it a default, and don't you vaguely remember that *amazelevel* actually is an input for <<*create_amazingness*>>?
So, if past you had done a good job of it, when you  type in ```help(amazefunction)```, you'd get something like:

```
help(amazefunction)
Help on function amazefunction in module __main__:

amazefunction(amaze_type, **kwargs)
```
Disappointing?..yeah. Now however, imagine you'd actually invested a minute extra while actually writing this function, and thus saved future you a few minutes. 
This is what the output from ```help(amazefunction)``` could have looked like!


```
Help on function amazefunction in module __main__:

amazefunction(amaze_type, **kwargs)
    Creates an amazing thing. 
    
    Parameters
    ----------
    amaze_type : str
        The type of amazing object to be created.
        Possible value ['unicorn', 'rakshasa', 'wolpertinger']
    
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


 


