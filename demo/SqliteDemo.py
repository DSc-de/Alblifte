import sqlite3

################################################################################
# Simple demo showing how to use sqlite data viva python
# 
# This python3 script reads in the sqlite DB and outputs an md formatted overview.
# It is used to generate the repository's website at https://dsc-de.github.io/Alblifte/
################################################################################


# ------------------------------------------------------------------------------
# Some md print helper functsions
# ------------------------------------------------------------------------------

def printField(field, value1, value2=None):
    """ Print a field with up to 2 values"""
    if (not value1):
        return

    values = f'{value1}'
    if (value2):
        values += f' ; {value2}'

    print(f'* {field}: {values}')

def printLink(txt, url):
    """ Print a link"""
    if (not url):
        return

    print(f'* [{txt}]({url})')

def printSocialMedia(data):
    """ Print social media links but just FB and Twitter"""
    strElements = '';
    if (data[0]):
        strElements += f'[Facebook]({data[0]}) ,'
    if (data[1]):
        strElements += f'[Twitter]({data[1]}) ,'

    if (not strElements):
        return

    print(f'* _Social Media:_ {strElements}')


def printInfrastruktur(data):
    """ Print infrustructure elements """
    strElements = ""
    if (data[0]):
        strElements += "Kunstschnee, "
    if (data[1]):
        strElements += "Flutlicht, "
    if (data[2]):
        strElements += "Funpark, "
    if (data[3]):
        strElements += "Rodelhang, "
    if (data[4]):
        strElements += "Rodellift, "
    if (data[5]):
        strElements += "Tubing, "
    if (data[6]):
        strElements += "Sommerbetrieb, "
    if (data[7]):
        strElements += "Bikepark, "
    if (data[8]):
        strElements += "Bullcart, "
    if (data[9]):
        strElements += "Sommerrodelbahn"

    if (not strElements):
        return

    print(f'_Infrastruktur:_ {strElements}')


def printSkiArea(sa):
    """ Prints one ski area"""

    # ----------------------------------------------------------------
    # Match data base columns to field names

    # Location
    ID                 = sa[0]
    Name               = sa[1]
    WWW                = sa[2]
    GeoBreite          = sa[3]
    GeoLaenge          = sa[4]
    WebcamLink         = sa[5]
    StatusLink         = sa[6]
    Tel1               = sa[7]
    Tel2               = sa[8]
    EMail              = sa[9]
    # Infrastructure
    hatKunstschnee     = sa[10]
    hatFlutlicht       = sa[11]
    hatFunpark         = sa[12]
    hatRodelhang       = sa[13]
    hatRodellift       = sa[14]
    hatTubing          = sa[15]
    hatSommerbetrieb   = sa[16]
    hatBikepark        = sa[17]
    hatBullcart        = sa[18]
    hatSommerrodelbahn = sa[19]
    # Social media
    Facebook           = sa[20]
    Twitter            = sa[21]
    Youtube            = sa[22]
    Feed               = sa[23]
    Meta               = sa[24]

    # ----------------------------------------------------------------
    # Print header
    print(f'### {ID}')

    # ----------------------------------------------------------------
    # Print location
    print('_Lift:_')
    printField('Name',           Name)
    printLink( 'Website',        WWW)
    printField('Position',       GeoBreite, GeoLaenge)
    printLink( 'Webcam Link',    WebcamLink)
    printLink( 'Status Link',    StatusLink)
    printField('Schnee Telefon', Tel1, Tel2)

    # ----------------------------------------------------------------
    # Print infrastructure
    printInfrastruktur(sa[10:20]);

    # ----------------------------------------------------------------
    # Social
    printSocialMedia(sa[20:24]);

    # ----------------------------------------------------------------
    # Print footer
    print('---')


# ------------------------------------------------------------------------------
# The actual script
# ------------------------------------------------------------------------------

# Connect to sqlite DB and create cursor
conn = sqlite3.connect('../alblifte/data/Alblifte.sqlite')
c = conn.cursor()

# Query all areas and print an overview, line by line
for row in c.execute('SELECT * FROM Lifte ORDER BY ID'):
        printSkiArea(row)
