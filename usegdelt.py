def usegdelt(download_file_directory,output_file_directory):
    import pandas as pd
    import glob

    csv_list = glob.glob(download_file_directory + '/*.CSV')
    print('get %s CSV files' % len(csv_list))
    for i in csv_list:
        fr = open(i, 'r').read()
        with open(output_file_directory + '/gdelt.csv', 'a') as f:
            f.write(fr)
        print('sucess！')
    print('Done！')

    gdelt = gdelt = pd.read_csv(output_file_directory + '/gdelt.csv', '\t', error_bad_lines=False, header = None)
    gdelt.columns = ['GLOBALEVENTID', 'SQLDATE', 'MonthYear', 'Year', 'FractionDate', 'Actor1Code', 'Actor1Name',\
                     'Actor1CountryCode', 'Actor1KnownGroupCode', 'Actor1EthnicCode', 'Actor1Religion1Code',\
                     'Actor1Religion2Code',	'Actor1Type1Code', 'Actor1Type2Code', 'Actor1Type3Code', 'Actor2Code',\
                     'Actor2Name', 'Actor2CountryCode', 'Actor2KnownGroupCode', 'Actor2EthnicCode',\
                     'Actor2Religion1Code', 'Actor2Religion2Code', 'Actor2Type1Code', 'Actor2Type2Code',\
                     'Actor2Type3Code', 'IsRootEvent', 'EventCode', 'EventBaseCode', 'EventRootCode', 'QuadClass',\
                     'GoldsteinScale', 'NumMentions', 'NumSources', 'NumArticles', 'AvgTone', 'Actor1Geo_Type',\
                     'Actor1Geo_FullName', 'Actor1Geo_CountryCode', 'Actor1Geo_ADM1Code', 'Actor1Geo_Lat',\
                     'Actor1Geo_Long', 'Actor1Geo_FeatureID', 'Actor2Geo_Type', 'Actor2Geo_FullName',\
                     'Actor2Geo_CountryCode', 'Actor2Geo_ADM1Code', 'Actor2Geo_Lat', 'Actor2Geo_Long',\
                     'Actor2Geo_FeatureID', 'ActionGeo_Type', 'ActionGeo_FullName', 'ActionGeo_CountryCode',\
                     'ActionGeo_ADM1Code', 'ActionGeo_Lat', 'ActionGeo_Long', 'ActionGeo_FeatureID', 'DATEADDED',\
                     'SOURCEURL']
    gdelt['AvgTone'] = gdelt['AvgTone'].astype(float)
    return gdelt
