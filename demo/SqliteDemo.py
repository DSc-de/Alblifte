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
    istMietbar         = sa[9]
    EMail              = sa[10]
    # Infrastructure
    hatKunstschnee     = sa[11]
    hatFlutlicht       = sa[12]
    hatFunpark         = sa[13]
    hatRodelhang       = sa[14]
    hatRodellift       = sa[15]
    hatTubing          = sa[16]
    hatSommerbetrieb   = sa[17]
    hatBikepark        = sa[18]
    hatBullcart        = sa[19]
    hatSommerrodelbahn = sa[20]
    # Social media
    Facebook           = sa[21]
    Twitter            = sa[22]
    Youtube            = sa[23]
    Feed               = sa[24]
    Meta               = sa[25]

    # ----------------------------------------------------------------
    # Print header
    print(f'### Lift ID: {ID}')

    # ----------------------------------------------------------------
    # Print location
    print('_Lift:_')
    printField('Name',           Name)
    printLink( 'Website',        WWW)
    printField('Position',       GeoBreite, GeoLaenge)
    printLink( 'Webcam Link',    WebcamLink)
    printLink( 'Status Link',    StatusLink)
    printField('Schnee Telefon', Tel1, Tel2)
    if istMietbar == -1:
        printField('Lift is mietbar', 'unbekannt')
    elif istMietbar == 1:
        printField('Lift is mietbar', 'ja')
    elif istMietbar == 0:
        printField('Lift is mietbar', 'nein')
    else:
        printField('Lift is mietbar', '!!!Fehler!!!')
    print('')

    # ----------------------------------------------------------------
    # Print infrastructure
    printInfrastruktur(sa[11:21]);
    print('')

    # ----------------------------------------------------------------
    # Social
    printSocialMedia(sa[21:25]);
    print('')

    # ----------------------------------------------------------------
    # Print footer
    print('---')
    print('')


# ------------------------------------------------------------------------------
# The actual script
# ------------------------------------------------------------------------------

# Connect to sqlite DB and create cursor
conn = sqlite3.connect('../data/Alblifte.sqlite')
c = conn.cursor()

# Query all areas and print an overview, line by line
for row in c.execute('SELECT * FROM Lifte ORDER BY ID'):
        printSkiArea(row)
