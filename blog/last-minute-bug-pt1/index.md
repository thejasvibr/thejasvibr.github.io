Title: Last-minute bug : part 1
slug: last-minute-bug-pt1
date: 2020-04-25 08:50:58 UTC+02:00
tags: scientific computing
category: 
link: 
status: private
description: 
type: text

The first paper I'll be  submitting as a PhD student  is due in a couple of days.
 We've managed to get past the first round of reviews, the reviewers have suggested a bunch of 
things. I've managed to implement the hardest parts over the past six months,
 and now I'm preparing the figures. As usual they go through multiple rounds 
of comments and changes. The results match pretty well with previous expectations
and common sense, until I begin to look closely at the zero probabiliy values, and also discovered
the presence of sounds that were infinitely loud. There should be *no* zero probabilities, not yet at least, and absolutely no infinitely loud sounds.
What was happening?<!--TEASER END-->

My supervisor had suggested I change a single plot's layout a bit to clarify the 
presentation of the results. In addition, there were some general changes 
he'd suggested too. Keep the font sizes constant across all plots and such things. 
It's not like I hadn't looked at the data carefully, or at least had seen them 
and thought, yeah this makes sense. I had of course looked at the data as it came, but I just hadn't looked
at *this* particular batch of simulation data as carefully because I'd assumed if simulations work for X, they'd also work for 10X. 

You can take computers for granted, not so much the code they run. The code they
run tells you a lot about the human side of things! Broadly speaking, the data I had 
to plot was a series of echo detection probabilities over group size. The 
probability value is expected to be between 0 and 1, and in the simulations 
I was running, there was good reason to almost never expect either a 0 or a 1.
The values had to be very close, but not be exactly either of these two values. 
On a graph of course, 0.000000001 and 0 look the same, and while looking at the
values in a screen display, I'd of course also assumed there was a one somewhere
there. However, to my shock I realised, the number of echoes detected in the 400 bat group size simulations
were all 0. Moreover, there were sounds being heard in these simulations were impossibly loud. They literally
had a received level of infinity. Yes, not kid I you, infinity.

Typically, after I've discovered a bug and fixed it, I can always run the simulation 
again and get the corrected results, but not this time. With increasing group  sizes, 
the calculation time increased very quickly, and this essentially meant waiting for 
another few days or so to get the results for a few hundred runs. I had been using parallelised runs on 
multi-core computers through a cloud service, but there weren't enough credits (the moneyz) left
to do another such run. The results from the 400 and 800 group sizes were the most 'expensive' results as
they were run on multi-core virtual machines costing about 3-4$ an hour. While this doesn't 
sound like much per hour, stuff adds up when you have to leave it running even for a day (~70-100$).
Even if the bug was fixed, I could not do any more runs. The bug in the code had to be found, fixed and verified, but
I would'nt be able to include the actual data in the paper itself.

Looking into the code I saw that for some reason, all the simulation runs
in the 400 bat group showed ZERO detected echoes in EVERY single run. The simultations themselves
had randomness in many parts of the workflow, there should have been at least one or two runs with non-zero values. This
was already a sign that there was something *very* weird happening. Moreover, it turned out on closer inspection that 
only one type of sound, the secondary echoes were being heard at an infinite received level. The other sounds' values
were matching expected levels. Why was it happening? It turns out there's
a very human mistake behind this bug. And if you're wondering what happened
to the paper, and whether the rest of the code base is riddled with similar
bugs? I'll end part I by saying the findings of the paper were nonetheless 
not affected by this bug. I was __very__ $^\infty$ lucky in this particular
case I'd say. The reason I'd initially thought the bug-riddled data was okay 
was indeed because it followed the trends from previous runs, and didn't stand out
in any obvious manner. We removed the faulty data and could go ahead with the presentation
and discussion of the results. What caused the bug? Read on !
