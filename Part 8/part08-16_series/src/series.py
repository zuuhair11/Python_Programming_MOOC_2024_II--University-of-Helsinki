# Write your solution here:
class Series(object):
    def __init__(self, title, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)

    def __str__(self):
        title = '{} ({} seasons)'.format(self.title, self.seasons)
        genres = 'genres: ' + ', '.join(self.genres)
        ratings = 'no ratings'
        if len(self.ratings) > 0:
            ratings = '{} ratings, average {:.1f} points'.format(len(self.ratings), sum(self.ratings) / len(self.ratings))

        return '{}\n{}\n{}'.format(title, genres, ratings)


def minimum_grade(rating: float, series: list) -> list:
    new_series = []
    for serie in series:
        for rate in serie.ratings:
            if rate > rating:
                new_series.append(serie)
                break

    return new_series


def includes_genre(genre: str, series: list) -> list:
    new_series = []
    for serie in series:
        if genre in serie.genres:
            new_series.append(serie)

    return new_series


if __name__ == '__main__':
    s1 = Series('Dexter', 8, ['Crime', 'Drama', 'Mystery', 'Thriller'])
    s1.rate(5)

    s2 = Series('South Park', 24, ['Animation', 'Comedy'])
    s2.rate(3)

    s3 = Series('Friends', 10, ['Romance', 'Comedy'])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print('a minimum grade of 4.5:')
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print('genre Comedy:')
    for series in includes_genre('Comedy', series_list):
        print(series.title)
