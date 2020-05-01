Title: Universal data formats
Date: 2020-04-09 09:27
Updated: 2020-04-23 08:53
Category: data analysis

I'm still trying to get through an old but (*I think*) cool analysis for a manuscript 
that's over five years in the making now. The code in the manuscript
itself reflects the need for mutiple coding platforms and how each of them 
bring its own superpowers with it. All of the image analysis results in the project
has been done in MATLAB. The stats and analyses have been executed and documented
in R with Markdown notebooks. A collaborator did some additional analyses in 
MATLAB recently and sent over some new results. 

It would have all been fine, and I probably  wouldn't have even written the post if <!-- TEASER_END-->
I was still using the same laptop I had when the project started. Now, however, 
even though the laptop is  the same, it's gone through a couple of OS changes 
and currenly has  R and Python installed in it -  same cover different contents. Getting some .mat files and having to open
them to analyse them is not impossible. I'm very thankful for cross-language packages like 
[R.matlab](https://cran.r-project.org/web/packages/R.matlab/index.html) and the inbuilt [scipy.io.loadmat](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.loadmat.html), and was able to load the data without problem. 

However, even the act of having to find a specialised package to load a dataset
saved in a platform-specific format made me re-think how I would save my data in the
future. The problem of language specific data files is not a computing platform based issue.
Even as a Python/R used it seems only natural to 
end the day by saving the results  into  one .Rda or .pkl file. The problem only arises after all  
when the same files have to be read by  someone else who's not invested
in the platform of your choice. Simple question, what if I'd decided to send a collaborator
a .Rda/.pkl file, and they use a completely different computing platform which
is called say... Kidneybeans? Kidneybeans is an established platform in the 
field of MagicMaking and has a small but established community of researchers
using it. Should your collaborator bend to the pressure of a larger established 
community and spend 45 minutes of their time just to load and re-format the data?
Not fair right?s

The solution to overcoming cross-language barriers is of course to use 'standard' formats (csv, json, hdf5). 
This has been suggested multiple times [ref1,ref2]() and despite having read the literature it's only beginning to 
dawn on me. It does require some effort, to plan and re-organise all the data
into standard formats instead of being able to 'naturally' dump that list, 
data frame and image data into one file (or maybe multiple files?..). I guess, the main advantage of 
saving stuff into universal formats is the data will still remain accessible 
to future collaborators using *any* computational platform, and of course 
the most likely future collaborator as always is __futureyou__!
