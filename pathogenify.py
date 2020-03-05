#define function for use
def pathogenify(marketdf, virusdf):
#due to gaps in dates between virus measures, restrict market data to the overall range between min and max dates
	marketdf = marketdf.loc[virusdf.index[0]:virusdf.index[-1]]
#perform outer join of market data
	market_virus_df = pd.merge(marketdf,virusdf,left_index=True, right_index=True, how='outer')
#rename columns 
	market_virus_df.columns = ['Market','Deaths']
#forward fill NAs between dates (as applicable)
	market_virus_df.fillna(method='ffill', inplace=True)
#lambda function for percentage change in 1) market price and 2) death count

	market_virus_df['Pct_Chng_Market'] = lambda x: percent_change()
#Visualization

def percent_change(NEW,OLD):
	((NEW - OLD)/ OLD)*100