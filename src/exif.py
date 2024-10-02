import exiftool


class Exif(object):
    def __init__(self, filename):
        self.filename = filename

    def data(self):
        with exiftool.ExifToolHelper() as et:
            exif = et.get_metadata(self.filename)[0]
        return exif
