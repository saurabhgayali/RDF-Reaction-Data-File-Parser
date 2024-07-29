import os
import json

def readFile(filePath):

    if not os.path.exists(filePath):
        return "File not found."
    
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except IOError:
        return "Error reading file."
filePath="sample.rdf"
sampleData=readFile(filePath)

def extractRDFElements(content,filePath):

    if content == "File not found.":
        return "File not found."

    if content == "Error reading file.":
        return "Error reading file."
    
    content = content.split('\n')
    dateTime=content[1].split(',')[1].strip()
    output={}
    output["date"] = f"Date: {dateTime}"
    output["time"] = f"Time: {dateTime}"
    output["rdfName"] = filePath
    return output

def extractReactionElements(reactionData):
    content=reactionData.split('\n')
    reactantsProductsdata=content[4]
    out={}
    out["numberOfReactants"]=captureDigits(reactantsProductsdata)[0]
    out["numberOfProducts"]=captureDigits(reactantsProductsdata)[1]
    return out

sampleReactionData='''$RXN

      RDKit

  2  1
$MOL

     RDKit          2D

  9  9  0  0  0  0  0  0  0  0999 V2000
   -2.8953    2.1637    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.0283    1.6655    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.1613    1.1671    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.1593    0.1673    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.2923   -0.3311    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.2903   -1.3311    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.1553   -1.8327    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.0223   -1.3345    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.0243   -0.3345    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  3  0
  2  3  1  0
  3  4  1  0
  4  5  1  0
  5  6  1  0
  6  7  1  0
  7  8  1  0
  8  9  1  0
  9  4  1  0
M  END
$MOL

     RDKit          2D

 11 11  0  0  0  0  0  0  0  0999 V2000
   -2.4638    0.8577    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
   -2.4602   -0.1423    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.3244   -0.6453    0.0000 Cl  0  0  0  0  0  0  0  0  0  0  0  0
   -1.5924   -0.6391    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.7282   -0.1361    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.7316    0.8639    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.1324    1.3671    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.0004    0.8701    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.0038   -0.1297    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.1396   -0.6331    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.1432   -1.6329    0.0000 Br  0  0  0  0  0  0  0  0  0  0  0  0
  1  2  2  0
  2  3  1  0
  2  4  1  0
  4  5  1  0
  5  6  4  0
  6  7  4  0
  7  8  4  0
  8  9  4  0
  9 10  4  0
 10 11  1  0
 10  5  4  0
M  END
$MOL

     RDKit          2D

 19 21  0  0  0  0  0  0  0  0999 V2000
    1.9529   -1.8960    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
    1.0873   -1.3954    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.0881   -0.3954    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.2225    0.1054    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.2233    1.1054    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.0897    1.6046    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.0905    2.6046    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.9569    3.1040    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.8225    2.6034    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.8217    1.6034    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.9553    1.1040    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.6439   -0.3940    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.5095    0.1068    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.3759   -0.3926    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.3767   -1.3926    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.5111   -1.8932    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.5119   -2.8932    0.0000 Br  0  0  0  0  0  0  0  0  0  0  0  0
   -0.6447   -1.3940    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.2209   -1.8946    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0
  2  3  4  0
  3  4  4  0
  4  5  1  0
  5  6  1  0
  6  7  1  0
  7  8  1  0
  8  9  1  0
  9 10  1  0
 10 11  1  0
  4 12  4  0
 12 13  4  0
 13 14  4  0
 14 15  4  0
 15 16  4  0
 16 17  1  0
 16 18  4  0
 18 19  4  0
 19  2  4  0
 11  6  1  0
 18 12  4  0
M  END

$DTYPE Name
$DATUM Synthesis of 2-naphtols from alkynes
$DTYPE Reference
$DATUM [10.1021/ol502951v]: https://doi.org/10.1021/ol502951v
$DTYPE Reaction Conditions
$DATUM AlCl3.DCM.rt
$DTYPE SMILES
$DATUM C#CCC1CCCCC1.O=C(Cl)Cc1ccccc1Br>>Oc1cc(CC2CCCCC2)c2cccc(Br)c2c1
$DTYPE Protections
$DATUM Not available
$DTYPE Inventory
$DATUM Not available
$RFMT'''

def captureDigits(textWithintegars):
    # Strip any leading/trailing whitespace and split the data string by any whitespace
    digits = textWithintegars.strip().split()
    
    # Convert the split string elements to integers
    firstNumber = int(digits[0])
    secondNumber = int(digits[1])
    
    return firstNumber, secondNumber

def extractRepeatElements(text,breakString,typeOfBreak,start,numberOfElements):
    data=text.split(breakString)[start:start+numberOfElements]
    data = [x.strip() for x in data]
    if typeOfBreak=="header":
        data = [breakString+"\n"+x for x in data]
    if typeOfBreak=="footer":
        data = [x+"\n"+breakString for x in data]

    return data



#print (extractRepeatElements(testdata,"break","header",2,14))
#print(json.dumps(extractRDFElements(sampleData,filePath),indent=4))


