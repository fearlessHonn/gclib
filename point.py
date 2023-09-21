import re


class Point:
    def __init__(self, latitude, longitude, text: str = ''):
        if type(latitude) == str:
            if re.match(r'(N|S)\s*\d{1,3}\s*°?\s*\d{1,2}\s*\.\s*\d+', latitude):
                self.latitude = self.single_conv_decimal(latitude)
            else:
                raise TypeError('Latitude does not match required format.')
        elif type(latitude) == float:
            if -90 <= latitude <= 90:
                self.latitude = latitude
            else:
                raise ValueError('Latitude is out of bounds.')
        else:
            raise TypeError('Please provide the latitude as string or float.')

        if type(longitude) == str:
            if re.match(r'(E|W)\s*\d{1,3}\s*°?\s*\d{1,2}\s*\.\s*\d+', longitude):
                self.longitude = self.single_conv_decimal(longitude)
            else:
                raise TypeError('Longitude does not match required format.')
        elif type(longitude) == float:
            if -180 <= longitude <= 180:
                self.longitude = longitude
            else:
                raise ValueError('Longitude is out of bounds.')
        else:
            raise TypeError('Please provide the longitude as string or float.')

        self.text = text

    def __str__(self) -> str:
        """
        Return coordinate in dmd format, which is the usual format for geocaching.
        :return: String (coordinate as dmd)
        """
        hemisphere_latitude = 'N' if self.latitude >= 0 else 'S'
        degrees_latitude = int(abs(self.latitude))
        minutes_latitude = round((abs(self.latitude) - int(abs(self.latitude))) * 60, 3)

        dmd_latitude = f'{hemisphere_latitude}{degrees_latitude}° {minutes_latitude}'

        hemisphere_longitude = 'E' if self.longitude >= 0 else 'W'
        degrees_longitude = int(abs(self.longitude))
        minutes_longitude = round((abs(self.longitude) - int(abs(self.longitude))) * 60, 3)

        dmd_longitude = f'{hemisphere_longitude}{degrees_longitude}° {minutes_longitude}'

        return f'{dmd_latitude}\t{dmd_longitude}'

    @staticmethod
    def single_conv_decimal(coordinate: str) -> float:
        degrees, minutes, decimals = re.findall(r'\d+', coordinate)
        decimal_coordinate = int(degrees) + (int(minutes) + int(decimals) * 0.001) / 60

        if 'S' in coordinate or 'W' in coordinate:
            decimal_coordinate *= -1

        return decimal_coordinate

    @staticmethod
    def dmd2dd(latitude, longitude) -> tuple[float, float]:
        decimal_latitude = Point.single_conv_decimal(latitude)
        decimal_longitude = Point.single_conv_decimal(longitude)

        return decimal_latitude, decimal_longitude