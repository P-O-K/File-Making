
from sys import argv as sArgv
from os import path as osPath
from os import getcwd as CWD
from subprocess import run


class ENV_F:

    @staticmethod
    def userHelp( ) -> None:
        print( 'USER-HELP:' )
        print( '\t-> Directory argument: Requires either a full path( C:\\foldernameA\\foldernameB ) or an extension on the CWD( .\\foldernameA\\foldernameB )' )
        print( '\t-> File argument:      Requires an extension tpye( .txt | .py | .cpp | ect.. )  eg.. myNewNote.txt' )
        print( '\t-> Software argument:   Requires only the name if the program Knows it exists or else it requires .exe extension\n' )
        raise SystemExit



    @staticmethod
    def openFileIn( software:str, directory:str, file:str ) -> None:
        run( f'{software} {directory}\\{file}', shell=True )



    @staticmethod
    def fileExists( directory:str, file:str ) -> bool:
        return osPath.exists( f'{directory}\\{file}' )



    @staticmethod
    def dirExists( directory:str ) -> bool:
        return osPath.exists( f'{directory}' )



    @staticmethod
    def MKFILE( directory:str, file:str ) -> None:
        run( f'echo.>{directory}\\{file}', shell=True );



    @staticmethod
    def MKDIR( directory:str ) -> None:                     # For all missing DIR extensions create as new path
        DIR = directory.split( '\\' )
        for ix in range( len( DIR ) ):
            cPath = '\\'.join( DIR[ :ix +1 ] )
            if( not osPath.exists( cPath ) ):
                run( f'mkdir {cPath}', shell=True )

        print( f'New Folder Directory Created:\t-> {cPath}\n' );





class DirectoryProcesser( object ):
    
    _ROOTDIR        :str    = sArgv.pop( 0 );
    _directory      :str    = None


    def __init__( self ):
        super( DirectoryProcesser, self ).__init__( )
        self.establishDirectory( )



    def establishDirectory( self ) -> None:
        self.loadCWD( )
        self.setDirectory( );
        if( not ENV_F.dirExists( self._directory ) ):
            self.missingDirectoryHandle( );

        print( f'[-]\tDirectory established -> {self._directory}\n' )



    def loadCWD( self ) -> None:
        self._directory = CWD( );



    def setDirectory( self ) -> None:
        for arg in sArgv:
            if( arg[:2] == '.\\' ):                             # Check for extended path
                self._directory += arg[ 1: ];
                sArgv.pop( sArgv.index( arg ) );
                return;

            if( arg[:3] == 'C:\\' ):                            # Check for explicit path
                self._directory = arg;
                sArgv.pop( sArgv.index( arg ) );
                return



    def missingDirectoryHandle( self ) -> None:
        E_MSG = f'\n[+] No existing location for: {self._directory}\n\t-> Create Location?(Y/N): ';
        if( input( E_MSG ).upper( ) =='Y' ):
            ENV_F.MKDIR( self._directory );
        else:
            raise SystemExit





class FileProcesser( object ):

    _filename       :str    = 'QuickNote.txt';
    _extension      :str    = '.txt';


    def __init__( self ):
        super( FileProcesser, self ).__init__( )
        self.establishFilename( )



    def establishFilename( self ) -> None:
        for arg in sArgv:
            if( '.' in arg[ 1: ] ) & ( '.exe' not in arg ):
                self._extension = '.' +arg.split( '.' )[ -1 ];
                self._filename = sArgv.pop( sArgv.index( arg ) );





class SoftwareProcesser( object ):

    _KNOWNSOFTWARE  :dict   = { 'notepad':'Notepad.exe', 'sublime':'Sublime_text.exe' };
    _software       :str    = 'Notepad.exe';


    def __init__( self ):
        super( SoftwareProcesser, self ).__init__( )
        self.establishSoftware( )



    def establishSoftware( self ) -> None:
        self.setSoftware( );



    def setSoftware( self ) -> None:
        for arg in sArgv:
            if( '.exe' in arg ):
                self._software = sArgv.pop( sArgv.index( arg ) );
                break;

            if( arg.lower( ) in self._KNOWNSOFTWARE ):
                self._software = self._KNOWNSOFTWARE[ sArgv.pop( sArgv.index( arg ) ).lower( ) ];
                break; 





# IMPORTANT! Multiple inheritance ordering matters :: Running ( LAST -> FIRST ) :: super( ).__init__( ) 
class ArgumentParser( SoftwareProcesser, FileProcesser, DirectoryProcesser ):

    _statusCode     :bool   =True;


    def __init__( self ):
        for arg in sArgv:
            if arg.lower( ) in [ 'help', '-help', '-h', '?' ]:
                ENV_F.userHelp( )

        super( ArgumentParser, self ).__init__( )
        if( sArgv ): self._statusCode = self.errorContinue( )



    def errorContinue( self ) -> bool:    # If error: Prompt user to continue
        print( '\n[!] One or more inputs cannot be processed or interpreted and are being replaced with the default values!' );
        print( f'\n\tPATH: -> {self._directory}\n\tFILE: -> {self._filename}\n\tPROG: -> {self._software}' );
        if( input( '\n[+] Continue with properties?( Y/N )' ).lower( ) != 'y' ):
            return False;
        return True;





def main( ):
    argParser = ArgumentParser(  )
    if argParser._statusCode:

        if( not ENV_F.fileExists( argParser._directory, argParser._filename ) ):
            ENV_F.MKFILE( argParser._directory, argParser._filename );

        ENV_F.openFileIn( argParser._software, argParser._directory, argParser._filename )


if __name__ == '__main__':
    main()
