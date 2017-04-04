# Movie Trailer Website:

  A movie list website generated from a python script customized with my
  favorite movies. In this website you can each movie's poster. Clicking on them
  will open a window showing its respective trailer.

## Pre-requisites

  Python should be installed in your system. To check open a terminal and run the following command:

  $ python -V

  or

  $ python --version

  It should output you current python version if you have it installed.

## Installation

  To install Download the files and extract them on the desired folder.


## Usage


  In your terminal go to the folder where you extracted the files and run this command:

  $ python entertainment_c.py

  (Make sure you are on the folder where the entertainment_c.py file is located).

  A browser window will open with the website containing the list of my favorite movie trailers.
  In the same folder a file called "fresh_tomatoes.html" will be generated holding the HTML code
  for the website in it.

## Customization

  If you would like to customize the site with your own favorite movies then you have to
  edit the code in entertainment_c.py changing the variables to your own. Each variable must
  be an instance of the Movie Class (module already included at the beginning). The Movie class
  takes 4 arguments. In order they are the Movie's :

  - Title.
  - Synopsis.
  - Trailer.
  - Poster.

  After you are done with the instances make sure you add or delete each and everyone
  on the array "movies". Afterwards you can run the script as mentioned in the "Installation"
  section.

## Copyright

  - fresh_tomatoes.py supplied by Udacity. 
