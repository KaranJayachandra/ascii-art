# ASCII Art Generator

Generating ASCII art is a pastime that can be used in messaging boards where ony text is allowed and can be used to add some light hearted humour to the conversation. An image is first converted to greyscale and the average brightness of a clump of pixels is calculated and replaced with an appropriate ASCII character based on the weight of the character. Complex character like '@' can be used for darker areas whereas '.' can used in lighter areas. The standard greyscale ASCII scale is used here.

'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '

But this can be replaced with anything the user deems fit and the input and output files as well the scaling needs to be specified to the function in main.py for the ASCII art to be generated into a text file. The scaling parameters defines the tile size as ASCII art at a pixel level cannot usually be seen clearly due to line length issues.

A simple explanation is shown below.

![ASCII Art](/images/ascii.png)