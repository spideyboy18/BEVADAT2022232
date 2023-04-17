import pandas as pd


class NJCleaner:
    def __init__(self, path: str):
        self.data = pd.read_csv(path)

    time_ranges = {
        (0, 3): 'late_night',
        (4, 7): 'early_morning',
        (8, 11): 'morning',
        (12, 15): 'afternoon',
        (16, 19): 'evening',
        (20, 23): 'night'
    }

    def map_time_to_part_of_day(time):

        for time_range, part_of_day in NJCleaner.time_ranges.items():
            if time.hour in range(time_range[0], time_range[1] + 1):
                return part_of_day

    def order_by_scheduled_time(self) -> pd.DataFrame:
        return self.data.sort_values(by=['scheduled_time'])

    def drop_columns_and_nan(self) -> pd.DataFrame:
        self.data.drop(['from', 'to'], axis=1, inplace=True)
        self.data.dropna(how='any', inplace=True)
        return self.data

    def convert_date_to_day(self) -> pd.DataFrame:
        self.data['date'] = pd.to_datetime(self.data['date'])
        self.data['day'] = self.data['date'].dt.strftime('%A')
        self.data.drop(['date'], axis=1, inplace=True)
        return self.data

    def convert_scheduled_time_to_part_of_the_day(self) -> pd.DataFrame:
        self.data['scheduled_time'] = pd.to_datetime(
            self.data['scheduled_time'])

        # Apply map_time_to_part_of_day function to scheduled_time column and create new part_of_the_day column
        self.data['part_of_the_day'] = self.data['scheduled_time'].apply(
            NJCleaner.map_time_to_part_of_day)

        # Drop scheduled_time column
        self.data.drop('scheduled_time', axis=1, inplace=True)
        return self.data

    def convert_delay(self) -> pd.DataFrame:
        self.data['delay'] = (self.data['delay_minutes'] >= 5).astype(int)
        return self.data

    def drop_unnecessary_columns(self) -> pd.DataFrame:
        self.data.drop(['train_id', 'actual_time',
                       'delay_minutes'], axis=1, inplace=True)
        return self.data

    def save_first_60k(self, path):
        self.data[:60000].to_csv(path, index=False)

    def prep_df(self, path):
        self.data = self.order_by_scheduled_time()
        self.data = self.drop_columns_and_nan()
        self.data = self.convert_date_to_day()
        self.data = self.convert_scheduled_time_to_part_of_the_day()
        self.data = self.convert_delay()
        self.data = self.drop_unnecessary_columns()
        self.save_first_60k(path=path)
