import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
mean = st.mean(data)
stdev = st.stdev(data)
stdev1 = stdev/10

def calc_rand_mean(counter):
    mean_dataSet = []
    for i in range(0,counter):
        index = random.randint(0,len(data)-1)
        value = data[index]
        mean_dataSet.append(value)
    mean = st.mean(mean_dataSet)
    return mean

meanList = []
for i in range(0,1000):
    set_of_means = calc_rand_mean(100)
    meanList.append(set_of_means)
mean1 = st.mean(meanList)
print("Mean is:",mean1)

d_1_start,d_1_end = mean1-stdev/10,mean+stdev/10
d_2_start,d_2_end = mean1-(stdev/10)*2,mean+(stdev/10)*2
d_3_start,d_3_end = mean1-(stdev/10)*3,mean+(stdev/10)*3

zTest = (mean-mean1)/stdev1

fig = ff.create_distplot([meanList],["reading_time"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,1],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[d_1_start,d_1_start],y=[0,1.2],mode="lines",name="D1 start"))
fig.add_trace(go.Scatter(x=[d_1_end,d_1_end],y=[0,1.2],mode="lines",name="D1 end"))
fig.add_trace(go.Scatter(x=[d_2_start,d_2_start],y=[0,1.2],mode="lines",name="D2 start"))
fig.add_trace(go.Scatter(x=[d_2_end,d_2_end],y=[0,1.2],mode="lines",name="D2 end"))
fig.add_trace(go.Scatter(x=[d_3_start,d_3_start],y=[0,1.2],mode="lines",name="D3 start"))
fig.add_trace(go.Scatter(x=[d_3_end,d_3_end],y=[0,1.2],mode="lines",name="D3 end"))

fig.show()
