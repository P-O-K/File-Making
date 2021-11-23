
File Taking Application :: WINDOWS :: run in PowerShell or CMD

To use -> Add file directory to system path and call via command line eg.. File fileName.txt

File app can take between 0-3 arguments( DIRECTORY, FILENAME, SOFTWARE ) in any given order.

    Directory argument:
            Requires either:
                     An explicit full path( C:\foldernameA\foldernameB ) or,
                     An extension to the CWD( .\foldernameA\foldernameB ).
                     
                     If the dir doesn't exist a prompt will be given to make it.


    File argument:
            Requires:
                    Extension type( .txt | .py | .html | .bat | ect.. )  eg.. myNote.txt, application.py


    Software argument:
            Requires either:
                    The name if the software alone if the program is aware of it IE( Notepad ), or
                    The name of the desired program with .exe extension IE( otherSoftware.exe )
                    
                    System knowledge of .exe program required!


    Any Argument duplicates will use the 1st given argument.
    Any invalid arguments will result in using the default values. ( runs input('continue with default value') )


Call Examples:

                                                   ARG1            ARG2            ARG3
    FILE                                      -> ( default,       default,        default )
    FILE myNote.txt                           -> ( filename,      default,        default )
    FILE .\aNewFolder Notepad                 -> ( extended-dir,  software,       default )
    FILE Sublime.exe pyApp.py C:\DEV\Python   -> ( software,      filename,       explicit-dir )
