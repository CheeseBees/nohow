# nohow

**General Python functions you may find useful**

----------

## Contents
### 1. Math Operation Functions
#### Importing it
	from nohow.MOF import *

#### Data type conversion
**ii(integer,index)** - *Integer Index* - Get single digit substring of integer - (returns int)

	from nohow.MOF import ii
	ii(331,2)
	
	>>>
	1

**iis(integer,index)** - *Integer Index to String* - Get single digit substring of integer - (returns str)

	from nohow.MOF import iis
	iis(


### 2. Text Editing Functions

#### Importing it
	from nohow.MOF import *

#### Formatting Strings
**cfp(text)** - *Chopped Format Print* - prints long strings without splitting words with the new line

	from nohow.TEF import cfp
	cfp("rrrrrrreeeeeeeaaaaaaalllllllyyyyyyy lllllllooooooonnnnnnnggggggg ssssssstttttttrrrrrrriiiiiiinnnnnnnggggggg")
	>>>
	rrrrrrreeeeeeeaaaaaaalllllllyyyyyyy lllllllooooooonnnnnnnggggggg
	ssssssstttttttrrrrrrriiiiiiinnnnnnnggggggg

**rls(text)** - *Remove Leading Spaces* - does what the name says

	from nohow.TEF import rls
	print(rls("    ForReference"))
