Title: So, you do *everything* in Python?
Date: 2020-03-29 00:15
Category: Python, coding, scientific computing

*"..and that was when Mowgli knew he would forever be safe in the comforting coils of Saamp, the Python"*
-- *Not Rudyard Kipling, 1892*

*"Open your eyes, look up to the skies and see" *
*--Queen, Not Rudyard Kipling, 1975 *

Every now and then at a conference, someone might ask me what programming language all this stuff was done in. 
When I say Python, there's typically two reactions. One typical response is 'That's cool, I too use Python, which libraries...'
, and as you  can imagine, the conversation takes a very detailed trajectory. The other typical response is 'I see, yeah, everyone's using Python nowadays. My supervisor/whole lab uses *<insert sixletterword>*, and so I'm kind of stuck at the moment'. My response to this statement is to strongly  urge the person to switch. Now is the best time to switch, and save yourself  time later etc. I  probably(definitely) end up sounding like a weird mix of concerned parent and preacher. 

Before I begin talking about the benefits of swithching to Python, I will make it clear upfront that the computer language maketh not the science. Good code remains good code irrespective of the language of choice (and the  bad code..).
The language of choice, however, strongly facilitates the kinds of techniques and attitudes to coding (which is a post for another time). 

So, why should you switch to Python/*<open-source language of your choise>* as early as possible?  
Three strong reasons:

##### *  1) It's free for me, my collaborators, and anyone else in the world to download and use
##### *  2) The supporting packages I  need to do your science are typically also free to download and use
##### *  3) I can write a piece of code, share it, and *anyone* can use  it!

#### It's free (a la MJ, for me, and for you and the entire human race)
The fact that installing an open-source computing platform makes it extremely portable. 
I can download Python on my personal laptop, go to a field site in another part of the world and download it on a Raspberry Pi there! Working with commercially licensed platforms can be a genuine pain. You do not want to waste precious research hours going online and trying to get a license validated and authorised each time you switch locations, devices or labs. Moreover, most licenses are given through the research institution/lab using them - and not to individuals. What happens when you leave, what if you'd actually like to work with the latest release of the language, does that need an extra license?
(Here I complain from personal experience)

### Open your eyes, and see - there's a  *rich* scientific package ecosystem around you!
One common comment I've heard is 'oh, but there's no good packages for *<insert technique X>*'. Whenever someone says that, it must taken with a big handful of salt. 
Statements like  'oh, but *<insertsixletterword>* has such cool packages for audio input-output and signal processing' are IMHO a result of misunderstanding what to expect from a language's package ecosystem. Even established scientists have said to me,  'Ah, Python, yeah - there aren't any good packages to do X'. Since all of us work in niche topics, we will have niche requirements. 
Not even proprietary computing languages have niche packages do to specific things like processing black-hole data, or detecting bat calls in recordings.
What any computing platform can provide, is an ecosystem to handle the variety of tasks needed on a day-to-day basis (data I/O, instrument interfacing, data pipelines, statistics, visualisation). 
I do not realistically expect or require my computing language to have inbuilt packages to solve my *niche* scientific needs. I can only expect that the bricks are 
available! 

So..be warned, Python's ecosystem is pretty damn good, and it's only getting better with time. In the recent past, I've been using *only* Python, even for experimental work involving speaker playbacks, microphone recordings, signal analysis, visualisation, statistics $^{1}$ and the cherry on the cake - writing it all in pretty [Jupyter]() noteboooks. 
The open package ecosystem means I essentially have a wide variety of packages to learn and try new techniques with time.
Contrast this to constantly thinking about which packages you can actually afford ('..I'd love to try out machine learning, but it costs *<insert X digit number>, but would also need the *other cool package* along with that*'). 


### Write, share, repeat 
I write rather niche code most of the time. There are times when I will take the effort of putting it up online 
and sharing it : 1) as part of a paper submission (as a DOI on a public repository) 2) when I think the code might be of interest to others, then I make it into a Python package and release it. 
I can confidently put up my code somewhere knowing fully well that *anyone* who would like to try it can step into it without thinking twice about the costs - and keep up withh any required upgrades or language version changes. 
This may not be such an issue when you work in a rather established institute/university. I'm constantly thus surprised when I see introductory scientific computing courses
being done with proprietary computing languages.

 

 




$^{1}$ *The packages I use for these tasks are: [scipy](), [sounddevice](), [pandas](), [matplotlib](), [statsmodels]()*
