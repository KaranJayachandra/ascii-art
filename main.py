# Importing pillow libary to read images
from PIL import Image

def generateArt(inputFile, greyScaleFile, outputFile, scale):
    """
    Takes input as 'inputFile' name and location, 'greyscaleFile' name and location,
    'outputFile' name and location and the amount of scaling for the pixels as 'scale'
    and provides the ASCII art for the input image in a text file. The greyscale file
    should be in txt format with a string of ASCII characters sorted from darkest to
    lightest.

    USAGE:

    generateArt('test.png', 'greyscale.txt', 'output.txt', 6)

    OUTPUT:

    00000000000000000000000000000000000000000000000000000000000000000000000000
    000000000000000000000000000000zzxxnnXX000000000000000000000000000000000000
    00000000000000000000000000YY!!>>II;;II::ii\\000000000000000000000000000000
    0000000000000000000000000000QQ||<<::IIIIIIII;;ff00000000000000000000000000
    00000000000000000000000000ttll!!IIIIIIIIIIIIIIII--000000000000000000000000
    000000000000000000000000??iillIIIIIIIIIIIIIIIIIIII++0000000000000000000000
    0000000000000000000000??>>IIIIIIIIIIIIIIIIIIIIIIIIII1100000000000000000000
    000000000000000000CC))??~~;;IIIIIIII;;~~__llIIIIIIII;;zz000000000000000000
    0000000000000000ffcc000000QQ{{IIII((00000000uu!!IIIIIIii000000000000000000
    00000000000000jjQQ0000000000QQ||jj000000000000YYllIIIIIIvv0000000000000000
    000000000000QQvv00000000000000rr00000000000000QQffIIIIII__0000000000000000
    000000000000jj0000000000000000uu0000000000000000XX;;IIII::0000000000000000
    000000000000jj000000ff00000000vv000000((00000000XXiiIIIIIIjj00000000000000
    000000000000ff000000JJ00000000vv000000zz000000QQXXIIIIIIII;;QQ000000000000
    000000000000UUCC00000000xx\\11//00000000000000JJvvIIIIIIIIII??000000000000
    00000000000000[[00QQff((tttttt||UU0000000000QQXX++IIIIIIIIII;;cc0000000000
    000000000000YYll[[((tttttttttttt((XX000000CCXX??IIIIIIIIIIIIII!!0000000000
    000000000000IIii??{{{{{{))11\\tt//--__||\\}}llIIIIIIIIIIIIIIIIIIjj00000000
    0000000000((::>>;;__||//\\||(())11>>IIIIIIIIIIIIIIIIIIIIIIIIIIII;;00000000
    00000000CC,,;;iiIIII;;!!--))tttt))IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIItt000000
    00000000__II;;iiIIIIIIIIIIII;;<<11//tt((--IIIIIIIIIIIIIIIIIIIIIIII<<000000
    000000YY::II;;iiIIIIIIIIII>>rrXXUUJJJJUUzznn++IIIIIIII;;;;IIIIIIII""000000
    000000--;;::,,!!IIIIIIII<<zzJJCCCCCCCCCCJJJJzz??IIIIIIII::,,IIIIII::CC0000
    000000::,,]]cc::__;;IIllccCCCCCCCCCCCCCCCCCCJJXX>>::>>ll,,^^!!;;II;;cc0000
    000000000000vv))tt//++{{JJCCCCCCCCCCCCCCCCCCCCJJ(({{tt\\;;;;00--::::vv0000
    00000000UU((]]\\tttttt[[nnCCCCCCCCCCCCCCCCCCCCYY]]tttttt||11??nn__""UU0000
    000000LL]]//tttttttttttt??ccCCCCCCCCCCCCCCCCCC]]//tttttttttttt??00{{000000
    000000vv((tttttttttttttt//??YYCCCCCCCCCCCCCCzz))tttttttttttt//__0000000000
    000000zz))tttttttttttttttt}}xxCCCCCCCCCCCCCC))//tttttttttttt//11nn00000000
    000000[[\\tttttttttttttttt\\[[YYCCCCCCCCCCCC??tttttttttttttttttt11||000000
    000011\\tttttttttttttttttttt__vvCCCCCCCCCCCC[[tttttttttttttttttt//[[000000
    0000||((//tttttttttttttttttt{{nnUUCCCCCCCCYY))tttttttttttttt//||}}zz000000
    000000??))))||//tttttttttt//))}}\\//(())))}}))//tttttttt//(()){{tt00000000
    000000QQ11]]))))))((||||||))))<<11ffxxff))__{{))((||(())))))--nn0000000000
    0000000000LL\\??[[))))))))))--QQ000000000000--)))))))){{??tt00000000000000
    0000000000000000QQxx\\))))//LL00000000000000uu]]]]}}\\UU000000000000000000
    00000000000000000000000000000000000000000000000000000000000000000000000000
    """
    # Open the greyscale file and reverse the order to follow pixel values
    gsFile = open(greyScaleFile, "r")
    greyScale = gsFile.read()
    gsFile.close()
    greyScale = greyScale[::-1]

    # Open input image and read meta data
    img = Image.open(inputFile).convert('L')
    heightTiles = int(img.height/scale)
    widthTiles = int(img.width/scale)

    # Dianostic information
    # print("Number of pixels in image: {0}".format(img.size))
    # print("Scale number: {0}".format(scale))
    # print("Number of tiles in height: {0}".format(heightTiles))
    # print("Number of tiles in width: {0}".format(widthTiles))

    # Open output file for processing
    output = open(outputFile, "w")
    # Process tile by tile
    # Clump of scale x scale pixels are one tile
    for i in range(heightTiles):
        row = ""
        for j in range(widthTiles):
            brightness = 0
            for k in range(i*scale, i*scale+scale-1):
                for l in range(j*scale, j*scale+scale-1):
                    brightness = brightness + img.getpixel((l, k))
            # Find average brightness in a tile and use that to find the appropriate
            # character in the greyscale string
            brightness = brightness / (scale**2)
            brightness = int((brightness * len(greyScale))/255) - 1
            row = row + greyScale[brightness] + greyScale[brightness]
        # Write output row by row into txt file
        output.write(row)
        output.write("\n")
    output.close()

# Test using the sample file
inputFile = 'images\\test.png'
greyScaleFile = 'greyscale.txt'
outputFile = 'output.txt'
scale = 6

# Running the function
generateArt(inputFile, greyScaleFile, outputFile, scale)