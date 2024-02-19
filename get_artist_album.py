import argparse
from api_request import ArtistsAlbumsAPI
from functions import Export, Requirements


def main():
    # Automatic installation of requirements
    requirements = Requirements()
    requirements.install_requirements()
    # Adding arguments
    parser = argparse.ArgumentParser(description='This app downloads album info for defined Artists')
    parser.add_argument('artist_name', type=str, help='Artist name')
    parser.add_argument('file_format', type=str, choices=['JSON', 'EXCEL', 'CSV', 'RAW'],
                        help='File format (JSON, EXCEL, CSV, RAW)')
    parser.add_argument('file_name', nargs='?', type=str, help='File name (optional)')
    args = parser.parse_args()
    # Creating instances for ArtistsAlbumsAPI and Export (functions)
    export = Export()
    artist_albums_api = ArtistsAlbumsAPI()
    # Downloading albums from Spotify API
    albums = artist_albums_api.run_request(args.artist_name)
    if not albums:
        return print('No albums found')
    # Checking file names depending on file formats
    if args.file_name is None:
        if args.file_format == 'EXCEL':
            args.file_name = args.artist_name + '.xlsx'
        else:
            args.file_name = f"{args.artist_name}.{args.file_format.lower()}"
    # If file format is RAW then list albums in console
    if args.file_format == 'RAW':
        for album in albums:
            print(album)
        return
    # If file format is JSON export albums to .json file
    if args.file_format == 'JSON':
        export.to_json(albums, args.file_name)
        return
    # If file format is EXCEL export albums to .xlsx file
    if args.file_format == 'EXCEL':
        export.to_excel(albums, args.file_name)
        return
    # If file format is CSV export albums to .csv file
    if args.file_format == 'CSV':
        export.to_csv(albums, args.file_name)
        return


if __name__ == "__main__":
    main()
