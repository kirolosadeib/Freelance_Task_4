#importing streamlit library
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt


#opening the image
image = Image.open('Logo.png')

#displaying the image on streamlit app
st.image(image)
#Display Title
st.title('Year 2023 - Analysis')
#
dataframe=pd.read_csv("Sample_Output_Visualization.csv")

#Market Share
st.title('Market Share')
st.write("Market Share Growth is a linear Relationship -- Kind of Impractical but great work happened this year:)")
fig = go.Figure()
fig.add_trace(go.Scatter(x=dataframe["Start Date"], y=dataframe["Market_Share"]))
fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Market Share")
st.plotly_chart(fig, use_container_width=True)


#Number of Sold Productrs
st.title('Number of Sold Products')
st.write("Number of Sold Products have increasing linear Trend with fluctuating values varying from one month to another")
fig = go.Figure()
fig.add_trace(go.Scatter(x=dataframe["Start Date"], y=dataframe["Units_Sold_Trend"],mode='lines',name='Overall Selling Trend'))
fig.add_trace(go.Scatter(x=dataframe["Start Date"], y=dataframe["Units Sold"],mode='lines',name='Number of Sold Units'))
fig.update_layout(
    title=dict(text="Sold Units")
)
fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Sold Units")
st.plotly_chart(fig, use_container_width=True)

#Revenue
st.title('Revenue')
st.write("Revenue decreased towards end of year taking into consideration that it is fluctuating from one month to another")
fig = go.Figure()
fig.add_trace(go.Scatter(x=dataframe["Start Date"], y=dataframe["Revenue"],mode='lines',name='Overall Selling Trend'))
fig.update_layout(
    title=dict(text="Revenue")
)
fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Revenue in Percentage %")
st.plotly_chart(fig, use_container_width=True)

#All Pie Charts
#
visitors_type=dataframe["Visitor Type"].value_counts().reset_index()
satisfaction=dataframe["Satisfaction"].value_counts().reset_index()
Spending_Score=dataframe["Spending Score"].value_counts().reset_index()
shipping_cost=dataframe["Shipping Cost"].value_counts().reset_index()
Discount_Rate=dataframe["Discount Rate"].value_counts().reset_index()

st.title("Pie Chart of all Categorical Metrics accross Year 2023")
st.write("A list of pie Charts showing percentage distribution of all categorical variables throughout the year")
chart_data = {
    "Visitors_Type": px.pie(visitors_type, values='Visitor Type', names='index',title="Visitor Type"),
    "Satisfaction": px.pie(satisfaction, values='Satisfaction', names='index',title="Satisfaction"),
    "Spending_Score": px.pie(Spending_Score, values='Spending Score', names='index',title="Spending Score"),
    "shipping_cost":  px.pie(shipping_cost, values='Shipping Cost', names='index',title="Shipping Cost"),
    "Discount_Rate": px.pie(Discount_Rate, values='Discount Rate', names='index',title="Discount Rate"),
}
selected_chart = st.selectbox("Select a chart", list(chart_data.keys()))
chart = chart_data[selected_chart]
st.plotly_chart(chart)

#Normalized Line Chart of three Metrics Revenue , Ad Cost and Cost of Goods
st.title('Time Plot of Normalized Values of Revenue , Ad Cost and Cost of Goods')
dataframe_website=dataframe[["Revenue","Ad Cost","COGS"]]
normalized_df=(dataframe_website-dataframe_website.min())/(dataframe_website.max()-dataframe_website.min())
normalized_df.head()
fig = go.Figure()
fig.add_trace(go.Scatter(x=dataframe["Start Date"], y=normalized_df["Revenue"],name="Revenue"))
fig.add_trace(go.Scatter(x=dataframe["Start Date"], y=normalized_df["Ad Cost"],name="Ad Cost"))
fig.add_trace(go.Scatter(x=dataframe["Start Date"], y=normalized_df["COGS"],name="Cost of Goods"))
fig.update_xaxes(title_text="Date")
st.plotly_chart(fig, use_container_width=True)


#Website Interactions
st.title('Site Interactions')
dataframe_website_traffic_data=dataframe[["Site Visits","Site Conversion","Impressions","Clicks","Click-through Rate","Bounce Rate"]]
fig, ax = plt.subplots()
sns.heatmap(dataframe_website_traffic_data.corr(),  annot=True)
st.write(fig)

#Categorical Features


#Visitor Type
visitors_local_minimum=[]
visitors_local_maximum=[]
for x in range (0,len(dataframe)):
    if(x%2==0):
        visitors_type=dataframe.loc[x,"Visitor Type"]
        visitors_local_minimum.append(visitors_type)
    else:
        visitors_type=dataframe.loc[x,"Visitor Type"]
        visitors_local_maximum.append(visitors_type)
#Visitors Type Minimum
result_1=pd.DataFrame(visitors_local_minimum).value_counts()
result_1=result_1.to_frame(name="Count").reset_index()
result_1.rename(columns={0:"Visitors_Type"},inplace=True)
result_1["Type"]="Minimum"
#Visitors Type Maximum
result_2=pd.DataFrame(visitors_local_maximum).value_counts()
result_2=result_2.to_frame(name="Count").reset_index()
result_2.rename(columns={0:"Visitors_Type"},inplace=True)
result_2["Type"]="Maximum"
#Total
total_visitors=pd.concat([result_1,result_2],axis=0)

#Discount Rate
discounts_local_minimum=[]
discounts_local_maximum=[]
for x in range (0,len(dataframe)):
    if(x%2==0):
        discount_rate=dataframe.loc[x,"Discount Rate"]
        discounts_local_minimum.append(discount_rate)
    else:
        discount_rate=dataframe.loc[x,"Discount Rate"]
        discounts_local_maximum.append(discount_rate)
#Discounts Minimum
result_1=pd.DataFrame(discounts_local_minimum).value_counts()
result_1=result_1.to_frame(name="Count").reset_index()
result_1.rename(columns={0:"Discounts"},inplace=True)
result_1["Type"]="Minimum"
#Discounts Maximum
result_2=pd.DataFrame(discounts_local_maximum).value_counts()
result_2=result_2.to_frame(name="Count").reset_index()
result_2.rename(columns={0:"Discounts"},inplace=True)
result_2["Type"]="Maximum"
#Total
total_discount=pd.concat([result_1,result_2],axis=0)

#Shipping Cost
shipping_local_minimum=[]
shipping_local_maximum=[]
for x in range (0,len(dataframe)):
    if(x%2==0):
        shipping=dataframe.loc[x,"Shipping Cost"]
        shipping_local_minimum.append(shipping)
    else:
        shipping=dataframe.loc[x,"Shipping Cost"]
        shipping_local_maximum.append(shipping)
#Shipping Cost Minimum
result_1=pd.DataFrame(shipping_local_minimum).value_counts()
result_1=result_1.to_frame(name="Count").reset_index()
result_1.rename(columns={0:"Shipping"},inplace=True)
result_1["Type"]="Minimum"
#Shipping Cost Maximum
result_2=pd.DataFrame(shipping_local_maximum).value_counts()
result_2=result_2.to_frame(name="Count").reset_index()
result_2.rename(columns={0:"Shipping"},inplace=True)
result_2["Type"]="Maximum"
#Total
total_shipping_Cost=pd.concat([result_1,result_2],axis=0)



st.title('Categorical Features')
st.write("A list of Bar Graphs showing categorical features associated with Local Maximum point and Local Minimum point among different number of sold units.")
chart_data = {
    "Visitors_Type":  px.bar(total_visitors, x="Visitors_Type", y="Count",color='Type', barmode='group',height=400),
    "Discount Rate": px.bar(total_discount, x="Discounts", y="Count",color='Type', barmode='group',height=400),
    "Shipping_Cost": px.bar(total_shipping_Cost, x="Shipping", y="Count",color='Type', barmode='group',height=400)
}
selected_chart = st.selectbox("Select a chart", list(chart_data.keys()))
chart = chart_data[selected_chart]
st.plotly_chart(chart)

st.title('Summary of Data Analysis and Recommendations')
#Part 1
st.write('Part 1 : Trends and Pattern in Sales Performance - Website Traffic Data')
st.markdown(
""" 
1. Number of Units Sold follow a general increasing Trend from Start to end of Year with higher Trend Starting from around week 17.
2. From the detailed data analysis, there is a clear seasonailty in the data every period of 3 Weeks
3. Although, Number of units sold follow increasing pattern while overall Revenue follows decreasing pattern and this is worth further investigation
4. There is a strong positive linear relationship between (Click Through Rate & Site Conversion) and (Site Visits and Site Conversion). It indicates that the website is highly appealing and it is likely that a customer performs action on website once he
reaches it whether by direction visit or through Ad Campains
5. There is a strong positive linear relationship between (Impressions & Clicks). It shows that Ad Channels have a good custome Targeting
6. The Rate of Site visits and bounce rate can give clear understanding of customer behaviour. At the beginning of year, bounce rate compared to site visitsis the same or little les. By Mid-Year, Bounce Rate exceeds Site Visits(Probably, a change happened
in this period and needs to be  investigated).By end of Year, Site Visits Rate, returned back to be higher than Bounce Rate
7. Impressions Start at a lower Rate than Site visits , then started to become aligned towards end of year which indicates aa change in the marketing campain at this time that is worth Investigating
 """
)
#Part 2
st.write('Part 2 : Hypothesis Testing')
st.markdown(
""" 
1. There is no statistical evidence of association between Cost of Goods and Revenues. So it isn't recommended to invest more in the cost of Goods.
2. There is no statistical evidence of association of Ad Cost with Revenue so Ad Cost needs to be rechecked or directed towards other channels in order to increase signifance associaton.
 """
)
st.write("Comment: As observed above in the original data, there is fluctuation in number of sold units so in the part an analysis was made on the associated features with the local maximum points and local minimum points to identify parameters that are more likely to focus on to sales increase")
st.markdown(
""" 
1. Audience Type is equally distributed among local maximum and minimum points so there is no statistical evidence of focusing 
2. Local Maximum points are likely to have common feature of : Buy One Get One while on the other side local minimum points are likely to have common feature of Free Shipping while discounts lie in the second place with the same number among both groups. Therefore it is more preferred to give Buy One get One discount 
to customers.
3. There is no  evidence on setting the shipping category in affecting the sales. Both Groups of Minimum and maximum local points are associated with moderate shipping price at the samoe count while local maximum points have relatively a higher portion among shipping category set to high.
 """
)
