This app downloads list of albums for defined artist from Spotify.

Requirements should be install automaticly.

Application require two arguments: Artist and file format 
(possible choices: "RAW", "JSON", "CSV", "EXCEL" - formats must be
written in uppercase letters), to run correctly.
Third argument - file name with correct extension - is optional.

All found albums will be listed in console - 
when you chose file format "RAW" - 
or saved in appropriate files - "EXCEL .xslx", "JSON .json", "CSV .csv"

To run application type (you must be in work directory):

(Windows) python get_artist_album.py "ARTIST" "FILE_FORMAT" "FILE_NAME (optional)"

(Linux) python3 get_artist_album.py "ARTIST" "FILE_FORMAT" "FILE_NAME (optional)"