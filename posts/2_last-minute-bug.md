Title: Squishing the last-minute bug : part 2
slug: last-minute-bug-pt2
date: 2020-04-26 08:26:00 UTC+02:00
tags: scientific computing
category: 
link: 
status: private 
description: 
type: text

Hello, and welcome back.  If you're arriving here without reading Part 1, you could 
check it out here. It's not really important, but will provide some background for
this particular post. In the previous  post, I'd talked about how I'd discovered a
rather important bug in my code a few days before the submission of the first paper
in my PhD. This post will talk about the how and why of  this bug, and it highlights
a very important aspect of writing code. How to write and test code that will run 
well in the unpredictable future of use-cases? <!--TEASER_END-->If this seems jargony right now, don't worry
I'll delve into it a bit more later!

The simulations in the paper involved some detailed acoustic calculations that took 
a fair amount of time to run. I was simulating how a bat's echolocation call would
propagate th rough space. Much like light, sound can move and reflect in very complex ways. 
In 'standard' echolocation, the call-emitting bat calls and listens for the echoes coming
from its ow emitted call. That is, the call from bat A hits a wall and returns as the
echo of bat A. However, when there are more than one bat, there's another type of echo that 
bat A could hear. This is the 'secondary echo' resulting from the call of bat B, hitting the 
wall, and as it travels back to bat B, it also travels to Bat A. Whether bats use these 
'secondary echoes' to infer object locations is still an unsettled question as far as I know, but the reason we were
simulating these in the paper was somewhat different. (You can read the paper for more details :P). 

The bug appeared in the code  used to generate the set of all possible secondary echoes. The 
paper was investigating how groups of bats managed to echolocate together, and whether they 
could actually hear their own echoes despite all the other loud sounds they would be hearing:
the loud calls of their neighbours, and the secondary echoes. The secondary echoes in a group
context arise from the call of a neighbouring bat, hitting another bat, and then finally 
reaching the 'focal' simulated bat being studied. 

I had decided to represent all the possible secondary echoes the target bat could hear by a set of 'routes'. 
So, if a call emitted by bat A hit bat B and then finally reached bat C, it would be a tuple with these 
entries (emitter, target, focals). Generating this is a quick ```for``` loop. 
Since it was a loop to generate all secondary echoes, and not primary echoes (emitter==receiver), I had
explicitly checked if the emitter and receiver were different in the function. Here is the original implementation

```
echo_routes = []
    for an_emitter in emitters:
        for a_target in targets:
            if not a_target is an_emitter:
                    emitter_target_focal = (an_emitter, a_target, focal_bat)
                    echo_routes.append(emitter_target_focal)
    return(echo_routes) 

```
For context, only the secondary echoes heard by one bat, the 'focal' bat was considered. So, it was a loop
which varied across all the emitting bat, the targets (other bats). In this particular case of course, I'd 
removed the focal bat from the possible set of target and call emitting bats. If you've been doing Python 
for some time, you might now realise where the bug was if I were to tell you that the ```emitters``` and 
```targets``` were lists with integers to represent each of the bats in the group. 

This formulation works pretty well, and I had actually done calculations to check that the output matched what
was expected by a simple calculation. If there are 10 bats in a group, the number of expected secondary echoes is

\\[N-1 \times \:N-2\\]

So, if I'd tested it, and this patch of code still lead to buggy behaviour, why was this? Well it was because things
worked well until a point, and they broke silently. I've written before about things that break silently, and why 
it's (very, very) horrible and unpleasant. This is not a new concept, and has been discussed by the whole industry
of software engineering! Back to the bug though, where did it stop working?

Try this in Python, and you'll see where things go wrong. 
(*if you  don't have Python already installed, you could try out one of the many  online consoles , eg. [here](https://repl.it/languages/Python3))
```
one_value = 20
another_value = 20

def report_comparison(X,Y):
    '''
    Checks if X and Y are the same, and prints out 
    the result.
    '''
    
    if one_value is another_value:
        print('The two values are the same')
    else:
        print('Different values!')

report_comparison(one_value, another_value)
```

This makes sense right? Okay, now try, this

```
one_value = 200
another_value = 200

report_comparison(one_value, another_value)

```
Works as expected right? And then try this,

```
one_value = 300
another_value = 300

report_comparison(one_value, another_value)
```

This *doesn't* make any sense right? Yeah, much to my  shock I realised this seemingly straightforward comparison had caused this 
giant bug. 










