import glob
import os
from PIL import Image, ImageSequence

# Output (max) size
size = 320, 240

for each in glob.glob('*.gif'):
    print(f'Processing {each}')   
     # Open source
    im = Image.open(each)

    # Get sequence iterator
    frames = ImageSequence.Iterator(im)

    # Wrap on-the-fly thumbnail generator
    def thumbnails(frames):
        for frame in frames:
            thumbnail = frame.copy()
            thumbnail.thumbnail(size, Image.ANTIALIAS)
            yield thumbnail

    frames = thumbnails(frames)

    # Save output
    om = next(frames) # Handle first frame separately
    om.info = im.info # Copy sequence info
    new_filepath = os.path.join('small_gifs/',"small_"+each)
    om.save(new_filepath, save_all=True, append_images=list(frames))
