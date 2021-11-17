
Note Taking Application :: WINDOWS :: run in CMD

To use -> Add file directory to system path and call via command line eg.. NOTE myNote.txt

Note app can take between 0-3 arguments( DIRECTORY, FILENAME, SOFTWARE ) in any given order.

    Directory argument:
            Requires either:
                     An explicit full path( C:\foldernameA\foldernameB ) or,
                     An extension to the CWD( .\foldernameA\foldernameB ).

    File argument:
            Requires:
                    Extension type( .txt | .py | .html | .bat | ect.. )  eg.. myNewNote.txt

    Software argument:
            Requires either:
                    The name if the software alone if the program is aware of it IE( Notepad ), or
                    The name of the desired program with .exe extension IE( otherSoftware.exe )


    Any Argument duplicates will use the 1st given argument.
    Any invalid arguments will result in using the default values. ( runs input('continue with default value') )


Call Examples:

                                                   ARG1            ARG2            ARG3
    NOTE                                      -> ( default,       default,        default )
    NOTE myNote.txt                           -> ( filename,      default,        default )
    NOTE .\aNewPyApp Notepad                  -> ( extended-dir,  software,       default )
    NOTE Sublime.exe pyApp.py C:\DEV\Python   -> ( software,      filename,       explicit-dir )
