
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

# Load dataset
data = pd.read_csv('SuperMarket Analysis.csv')

# Clean data
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
data.dropna(subset=['Date', 'Sales', 'gross income'], inplace=True)

# Bar Chart
bar_fig = px.bar(data.groupby('Product line')['Sales'].sum().reset_index(),
                 x='Product line', y='Sales',
                 title='Total Sales by Product Line',
                 color='Sales', color_continuous_scale='Blues')
bar_fig.write_image('bar_chart.png')

# Line Chart
line_fig = px.line(data.groupby('Date')['Sales'].sum().reset_index(),
                   x='Date', y='Sales',
                   title='Sales Trend Over Time')
line_fig.write_image('line_chart.png')

# Pie Chart
payment_counts = data['Payment'].value_counts()
pie_fig = px.pie(values=payment_counts.values, names=payment_counts.index,
                 title='Payment Method Distribution')
pie_fig.write_image('pie_chart.png')

# Histogram
hist_fig = px.histogram(data, x='Sales', nbins=20,
                        title='Distribution of Sales', color_discrete_sequence=['purple'])
hist_fig.write_image('histogram.png')

# Scatter Plot
scatter_fig = px.scatter(data, x='Sales', y='gross income', color='Product line',
                         title='Sales vs Gross Income')
scatter_fig.write_image('scatter_plot.png')

# Heatmap
corr = data[['Sales', 'gross income']].corr()
heatmap_fig = ff.create_annotated_heatmap(z=corr.values,
                                          x=corr.columns.tolist(),
                                          y=corr.columns.tolist(),
                                          colorscale='Viridis')
heatmap_fig.update_layout(title_text='Correlation Heatmap')
heatmap_fig.write_image('heatmap.png')
