Title: What you *could* do, but you shouldn't 
Date: 2020-03-28 8:20
Category: Python, coding, writing

*"What gets you into trouble ain't what you don't know, but what you think you do, but ain't so"*

This post is about how good software should be like an honest person - who knows their area of competence before taking up a task *REPHRASE THISS-- IT'S TOO STRONG*. 
We (myself included) often receive or write code to get things working, and then proceed to keep using it or share it eventually with our lab mates. 
Like anything in the course of life,  use-cases for the software may change. A new project comes up,  or someone (Person X) legitimately decides it'll be cool to try out this new experiment
and process the data with this awesome codebase.  Person X now triumphantly  sits in front of the computer...and waits for the code to  run through with anticipation .... and after a few seconds of anticipation,  out come the plots!!

Of course, there's a twist to the story in that the results actually seem okay in the beginning, until Person X notices a bunch of weird details. Factor Z, a universal constant, is about 1.5 times more than it should - and this is too much. 
But the diagnostic plots look fine, and the  code ran!! What is happening??

Many agonising hours later, Person X finally figures out that the Awesome Codebase has been a somewhat dishonest person. 
How is Awesome Codebase like a dishonest person you ask? Well, Person X figured out finally that Awesome Codebase was basically written to handle the analysis of Cool Experiments done to understand Factor Z using four Z-probes. What are Z-probes? They are the devices that measure the value of the Z-factor. Awesome Codebase can handle a wide variety of Z-probes, and that's why it's quite famous in its community. However, it  turns out Person X wanted to replicate  the experiments under the simplest possible conditions. Person X's experiment involves measurements with *three* Z-probes, instead of the standard five, six, or seven. 
In principle,  Person X, thinks - the only reason people haven't done it before is because they were being exta careful  in the early days, who needs __four__ Z-probes anyway??!!
But no, days later, Person X finds out that Awesome Codebase really wasn't built to handle three Z-probes at all! It is a logical impossibility given the equations and Science in the field of Z-factor studies. It turns out all Z-factor experiments have been done only with a prime number of Z-probes, ranging from 5 to 29, but no-one had  really thought of going below 5.
 If it is so  impossible, why didn't Awesome Codebase throw an error and stop everything dead in its tracks?

Yes, the analogy isn't clear yet. Awesome Codebase has been like someone  who nods silently but enthusiastically  to the question 'Can you speak German, the people at the dinner we're going to don't speak much English ?'.
And then, when you meet with Awesome Codebase for dinner, Awesome Codebase says 'Gruesse Sie', 'Danke', 'Salz' in a burst, and then settles down quietly for the rest of  the evening. Yes, you  could argue, this person does know *some* German - but the question is can they handle a conversation?
Do they understand what is happening around them? Why are they not saying anything, do  they know saying these three things in a continuous string may be grammatically correct but socially unusual. 

The biggest question remains of course, that is - why  didn't my  acquaintancce just say they don't speak German well enough. You could have then made other plans.
And so, in analogy, if Awesome Codebase was not built to handle less than five Z-probes - it should have said it out loud, thrown a warning, or even better - thrown a nasty error saying exaclty that *Z-probe error, this codebase cannot handle <5 Z-probes!*
Person X would have been happy, and moved on to find another equally awesome codebase, and  Awesome Codebase wouldn't have been dishonest. 

This is not a rant about how codebases are limited in their nature, it is a rant about the lack of documentation and clear communication to the user. 
All codebases are limited in their capabilities and are constrained by the historically envisioned use-cases. 
The use-cases will naturally change, but if the codebases capabilities don't match the requirements of the use-case -- this must be easily detectable!
The capabilities and limitations of a code base must be clearly highlighted in the form of a README or user manuals. If even these are not heeded or clear,  the true weapon to prevent misuse is throwing a clear error. 



