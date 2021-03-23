import glob
import os
import pygifsicle as pgf
# take GIFS and optimise them 

field_gifs = glob.glob('images/*.gif')
print(field_gifs)

for each in field_gifs:
    folder = os.path.split(each)[:-1][0]
    new_file = os.path.split(each)[-1]
    print('....',new_file)
    pgf.optimize(each, os.path.join(folder, 'optim_'+new_file))

print('done with GIF optimisation')
