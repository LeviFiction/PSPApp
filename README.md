# PSPApp
A library template for PaintShop Pro scripts to remove errors from VSCode when using PyLance

## Nothing special or advanced
These two files are little more than placeholders to remove linting errors when editing a PaintShop Pro Script inside of VSCode.  By default all PSPScripts must import the PSPApp or JascApp library as the first import in the file.  But this is an embedded library and doesn't actually exist for us to point to.

By adding these two files to the site-packages folder of your Python installation you can remove the errors presented by the PyLance linter.

Does not provide code completion for constants or any settings for commands.  Just gets rid of the nagging that the variable "App" doesn't exist that the library "PSPApp" cannot be resolved.

## HowTo: Install
Download these two files and put them into the Lib/Site-Packages folder of your Python Installation.  Preferrably Python 2.7 as that's the embedded version of Python that PSP uses.

## Recommended Next Steps:
It is recommended that you also copy JascUtils and PSPUtils from their location in PSP's installation directory to the same location as the PSPApp and JascApp libraries.
They can be used alongside these libraries to create scripts that work with code completion.  

You can usually find these libraries here: C:\Program Files\Corel\Version Folder\Languages\YourLanguage\Python Libraries\

