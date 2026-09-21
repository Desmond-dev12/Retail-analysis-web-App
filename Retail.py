# Libraries

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Retail Sales Analysis Dashboard")


@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path, encoding= "latin1")
    data = data.rename(columns={"Store": "Branch"})
    data["Date"] = pd.to_datetime(data["Date"])
    data["Date"] = pd.to_datetime(data["Date"], format="mixed")


    return data
file_path = pd.read_excel("retail_store_clean.csv")
data = load_data(file_path)

st.dataframe(data.head())

# sidebars 
st.sidebar.header("Filters")
selected_branch = st.sidebar.multiselect("Select_Branch", options=data["Branch"].unique(), default=data["Branch"].unique())
selected_category = st.sidebar.multiselect("Select_Category", options=data["Category"].unique(), default=data["Category"].unique())
selected_customer = st.sidebar.multiselect("Select_Customer_Type", options=data["Customer Type"].unique(), default=data["Customer Type"].unique())
selected_gender = st.sidebar.multiselect("Select_Gender", options=data["Gender"].unique(), default=data["Gender"].unique())


min_date = data["Date"].min()
max_date = data["Date"].max()

selected_date = st.sidebar.date_input("Select_Date_Range", value=(min_date, max_date),
                                      min_value=min_date, max_value=max_date)

if not selected_date or len(selected_date) != 2:
    st.write("Kindly Select a valid date")
    st.stop()
                                      
# filters 

branch_filter = data["Branch"].isin(selected_branch)
category_filter = data["Category"].isin(selected_category)
customer_filter = data["Customer Type"].isin(selected_customer)
gender_filter = data["Gender"].isin(selected_gender)
data["Date"] = pd.to_datetime(data["Date"])
start_date = pd.to_datetime(selected_date[0])
end_date = pd.to_datetime(selected_date[1])
date_filter = (data["Date"]>=start_date) & (data["Date"]>=end_date)
filtered_data = data[branch_filter & category_filter & customer_filter & gender_filter &
                     date_filter]
if filtered_data.empty:
    st.warning("No data found for the filters")
    st.stop()
    st.dataframe(filtered_data.head())
                 
# Rounding columns to two decimal places

data["Branch"] = data["Branch"].round(2)
data["Category"] = data["Branch"].round(2)
data["Customer Type"] = data["Customer"].round(2)
data["Gender"] = data["Gender"].round(2)
data["Transaction ID"] = data["Transaction ID"].round(2)
data["Unit Price"] = data["Unit Price"].round(2)

# Key Performance indicators 

total_sales = data["Total Amount"].sum()
total_quantity = data["Quantity"].sum()
avg_rating_by_price = data["Unit Price"].mean()
avg_cus_rating = data["Rating"].mean()
total_transac = data["Total Transaction ID"].nunique()

st.subheader('Key Performance Indicators(KPIs)')
col1, col2, col3, col4 = st.columns(4)
with col1:  
    st.metric(label="Total Sales", value=f"${total_sales:,.2f}" )
with col2:
    st.metric(label="Total Quantity", value=f"s{total_quantity:,.2f}")
with col3:
    st.metric("Average Unit Price", value=f"${avg_rating_by_price:,.0f}")
with col4:
    st.metric(label="Total Transaction", value=f"${total_transac:,.0f}")

# Visualization
branch_revenue = data.groupby("Branch").sum().reset_index()
fig_branch = px.bar(branch_revenue, title="Revenue Sales by Branch",
                    x="Branch", y="Total Amount", text="Total Amount",
                    color="Branch", color_discrete_sequence=px.colors.sequential.Viridis)
st.plotly_chart(fig_branch, use_container_width=True)

sales_by_product = data.groupby("Category")["Total Amount"].sum().reset_index()
fig_by_product = px.bar(sales_by_product, title="Sales by Category/Product", 
                        y='Total Amount', x="Category", text="Total Amount",
                        color="Category", color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig_by_product, use_container_width=True)

scatter_data = data[["Branch", "Category", "Unit Price", "Quantity", "Total Amount"]].copy()
data["Unit Price"] = pd.to_numeric(data["Unit Price"], errors="coerce")
data["Total Amount"] = pd.to_numeric(data["Total Amount"], errors="coerce")
data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce")

fig_scatter = px.scatter(
    scatter_data,
    x="Unit Price",
    y="Total Amount",
    size="Quantity",
    color="Branch",
    hover_name="Category",
    title="Sales vs Unit Price analysis",
    labels={"Unit Price": "Unit Price", "Total Amount": "Total Amount"},
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig_scatter.update_traces(marker=dict(line=dict(width=0.5, color="DarkSlateGrey")))
st.plotly_chart(fig_scatter, use_container_width=True)

customer_high_transac = data.groupby("Customer Type")["Transactions ID"].sum().reset_index()
fig_cus_high_transac = px.pie(customer_high_transac, title="Customer Type with the highest Transaction",
                                names="Customer Type",
                              values="Transaction ID",
                              hole=0.4)
st.plotly_chart(use_container_width=True)

data["Date"]= pd.to_datetime(data["Date"])
daily_sales_trend = data.groupby("Date")["Total Amount"].sum().reset_index()
fig_sales_trend = px.line(daily_sales_trend, title="Daily Sales Trend", x='date',
                          y="Total Amount", markers=True, color_discrete_sequence=["#2C3E50"])
st.plotly_chart(use_container_width=True)


# tabs
tab1, tab2, tab3, tab4 = st.tabs([])
with tab1:
    st.subheader("Data overview")
    st.write(st.dataframe(data.head()))
with tab2:
    st.subheader("Sales Analytics")
    

