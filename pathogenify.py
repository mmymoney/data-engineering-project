def percent_change(NEW,OLD):
	((NEW - OLD)/ OLD)*100

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

	#market_virus_df['Pct_Chng_Market'] = market_virus_df['Market'].apply(
	#	lambda x: percent_change(x.shift(1),x)
	#	) 

	# #market_virus_df['Pct_Chng_Death'] = market_virus_df['Death'].apply(
	# 	lambda x: percent_change(x.shift(1),x)
	# 	)
	market_virus_df['Pct_Chng_Market'] = market_virus_df['Market'].pct_change()*100
	market_virus_df['Pct_Chng_Death'] = market_virus_df['Market'].pct_change()*100

	return market_virus_df.head()
#Visualization



def regress_lin(pct_kill_rate,market_price):
    plt.scatter(pct_kill_rate,market_price,edgecolors='black')
    ylim = min(market_price)
    xlim = min(pct_kill_rate)
    title = f'{str(pct_kill_rate.name)} vs. {str(market_price.name)}'
    reg = linregress(pct_kill_rate,market_price)
    plt.plot(pct_kill_rate,pct_kill_rate*reg[0]+reg[1],color='r')
    plt.text(xlim,ylim,f'y={reg[0]}x + {reg[1]}',color='r')
    plt.title(f'{str(pct_kill_rate.name)} vs. {str(market_price.name)}')
    plt.xlabel(f'{str(pct_kill_rate.name)}')
    plt.ylabel(f'{str(market_price.name)}')
    plt.grid()
    plt.savefig(f'{title}.png')
    plt.show()
    print(reg)

#This shows the linear regression function for SARS Percentage Change in Death against Percentage Change in Market Close.
 regress_lin(Sars['Pct_Chng_Death'],Sars['Pct_Chng_Market'])
 regress_lin(Sars['Pct_Chng_Death'],Sars['Market'])

