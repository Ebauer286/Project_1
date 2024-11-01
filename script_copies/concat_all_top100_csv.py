#this function takes no input and just triggers an action. This function aggregates each unique top100 csv (one per year).
#the function concatenates each unique csv into once combined top100 songs by year csv.

def concatenate_all_top100_csv():

    year_list = [2024-x for x in range(0,45)]

    #passing all raw hot 100 csv's into function, generating top 100 lists per csv and dumping into new csv
    for year in year_list:
        path = f"C:\\Users\\kevin\\bootcamp\\Project_1\\resources\\billboard_hot_100_csvs\\{year}_bb_hot_100.csv"
        df = pd.read_csv(path)
        consolidate_top100_fromcsv_add_year(df)



    #reading in all top100 csvs, and concatenating into a single dataframe. dumping new consolidating dataframe into csv file.
    df_csv_append = pd.DataFrame()

    for year in year_list:
        path = f"C:\\Users\\kevin\\bootcamp\\Project_1\\resources\\most_frequent_hot100songs_by_year\\top100_{year}.csv"
        df = pd.read_csv(path)
        df_csv_append = pd.concat([df_csv_append, df], ignore_index=True)




    final_path = r"C:\Users\kevin\bootcamp\Project_1\resources"
    df_csv_append.to_csv(os.path.join(final_path,f"all_top100songs_by_year.csv")) #https://stackoverflow.com/questions/22872952/set-file-path-for-to-csv-in-pandas
