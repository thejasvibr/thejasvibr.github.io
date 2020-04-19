Title: To package or not to package?
Date: 2020-04-01 08:30
Category: scientific computing


After having worked in a field for over a few years, and gotten comfortable with programming in the language of your  choice, you slowly begin to realise
that your work essentially always consists of a set of analyses/tasks which are used again and again. For me, experimentally this means, having scripts ready 
that will initiate recordings, playbacks, and saving of audio files for the experiments I do. In terms of simulations, it means writing a lot of code, typically
based on a bunch of acoustics paradigms that are described by a bunch of equations/assumptions. 

I have of course read over and over again, that it's good practise to bundle all of your goodies into one place, and keep them as a package somewhere [REFS].
But why don't I do it yet? Right now, as an end-phase graduate student, I guess it's mainly because  each time I do this task, I'm not sure when I'll actually
have to do it again. The effort of trying to create a common framework and plan all the basic experimenta/computational tasks to be implemented doesn't pay  off. 
Writing a package, I realise  is as much about the single tiny  functions, as it is about the broad common concept and the sufficiently detailed documentation 
aroud it. If  I'm the only  one who's  going to use  it,  and am not even sure when - it's not worth the time :P. 

Butt, there are cases when I think the code  I've been using regularly is worth putting a decent amount of  thought into and pushing it all the way to a publicly 
available package. Initially  I used to think it's worth putting the effort of making a whole  package and releasing it for public use only if there was a whole community of researchers interested in them. However, this thinking changed when I had the opportunity to  meet Kalle A{dot}stroem, professor at the University of Lund. His group has been developing a package  to automatically calculate microphone positions from sound playbacks. I had approached him in order to check if the package they'd developed could  be used to infer the positions of my microphone arrays I was using to track bats. The package worked for my data, and we thus began of developing an integrated experimental + software workflow for field biologists to  use. While talking about who might be interested in something like this, Kalle mentioned it'd be very cool  even if just two-three labs would  be genuinely  interested in using this whole workflow. This sounded like a very small number to me, two-three labs could basically just consist of four-six people (one PI + one grad student), and back  then I began wondering if this was too niche?

Nowadays, however, I've realised how niche academic research can be. While we may work on a day-to-day basis with a common set of assummptions and follow the same conceptual principles, each of us has slightly different use cases. Even when one other person benefits from the use of a released package, it should  be considered a success. 

In some sense, the effect of publishing a package is a bit  more tangible  than publishing a paper in a journal. A package  is something that can be used on a day-to-day basis, unlike a paper which is a string of ideas put together. So should you publish your package or  not? Well, the rule of thumb I'm beginning to develop is essentially, if  you  think there's at least one more person who might find it interesting - do it. And remember, the most likely person who  will  find it interesting to use is this familiar-yet-unfamiliar stranger - future  you. 
 

REFS

 


