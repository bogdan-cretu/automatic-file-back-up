# back-up
Requirements: The script must be run on a machine with Python 3.10+;

It will have a source folder that will push all files to a replica (destination) folder. If there are any extra files in the replica folder, they will be deleted.

All changes will be displayed on the console with a time and date stamp and will be logged into a log file;

The script needs four command line arguments in order to run: source folder, replica(destination) folder, log folder and the interval to perform the verification;

There are no hardcoded destination folders for your files so you must specify your own. For more details use "-h" or "--help";

Works universally across platforms: Linux, Windows, MacOs.
