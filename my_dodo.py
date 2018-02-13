import wget

from doit.tools import run_once
import zipfile

base_url = 'https://www.spacetelescope.org/static/projects/fits_liberator/datasets/eagle/'

filenames = ['502nmos.zip', '656nmos.zip', '673nmos.zip']



def down():
	
	for filename in filenames:
		abd= wget.download(base_url + filename)



def task_download():
	
	return{'actions': [down],
	       
	       'targets': filenames,
	       'uptodate':[run_once]}
 

base_down = 'C:\\Users\\Echo\\image_blending\\'
fits_filenames = ['502nmos.fits', '656nmos.fits', '673nmos.fits']
def extrac():
	for filename in filenames:
		zip_ref = zipfile.ZipFile(base_down + filename, 'r')
		zip_ref.extractall('C:\\Users\\Echo\\image_blending')


def task_unzip():
  
	return {'actions': [extrac],
          
		'targets': fits_filenames,
          
		'file_dep': filenames,
		'uptodate': [run_once]}