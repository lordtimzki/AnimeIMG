Timothy Dacalos
47821565
tdacalos@uci.edu

-need pdoc, pycodestyle, pylint

Essentially uses the waifu.im api and prompts the user to select between 2 tags
and will display a random anime girl as a jpeg image. When ran, it will prompt
the user to enter a tag, then it will save the random image's json file
given by the API. Using the json format, it uses urllib's request
to take the url in the json file and download it to the local folder. Finally,
it uses matplotlib to display the image on a graph.
