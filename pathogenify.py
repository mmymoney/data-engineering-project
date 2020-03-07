#define function to create dataframe from market data and virus datsets post-clean

def pathogenify(marketdf, virusdf):
    #restrict market data date range to date range virus data applies to
    marketdf = marketdf.loc[virusdf.index[0]:virusdf.index[-1]]
    #merge data on outer join after date range restricted
    market_virus_df = pd.merge(marketdf,virusdf,left_index=True, right_index=True, how='outer')
    #rename columns
    market_virus_df.columns = ['Market','Deaths']
    #forward-fill NAs using prior day data if not NaN
    market_virus_df.fillna(method='ffill', inplace=True)
    #calculate daily percent change in market value
    market_virus_df['Pct_Chng_Market'] = market_virus_df['Market'].pct_change()*100
    #calculate daily percent change in deaths
    market_virus_df['Pct_Chng_Death'] = market_virus_df['Deaths'].pct_change()*100
    return market_virus_df