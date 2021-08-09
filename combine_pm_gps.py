import pandas as pd

def combine_pm_gps_csvs():
    pm_df = pd.read_csv("data/processed/airquality_data_to_use.csv")
    gps_df = pd.read_csv("data/raw/position.csv")

    # remove microseconds as a factor, we don't need that level of precision
    gps_df['timestamp'] = gps_df['timestamp'].apply(lambda x: x[:-7])
    pm_df['timestamp'] = pm_df['timestamp'].apply(lambda x: x[:-7])

    # set this new column to be the index of both dfs and join them
    gps_and_pm_df = gps_df.set_index('timestamp').join(
                        pm_df.set_index('timestamp'),
                            on='timestamp', how='right',
                            lsuffix='_gps', rsuffix='_pm').dropna()

    print(gps_and_pm_df)

    gps_and_pm_df.to_csv('data/processed/pm_with_gps.csv')

if __name__ == "__main__":
    combine_pm_gps_csvs()