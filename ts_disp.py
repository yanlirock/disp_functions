"""
display ts from pandas dateframe
"""
from plotly.offline import init_notebook_mode, plot, iplot
import plotly.graph_objs as go
init_notebook_mode(connected=True)

def plotly_ts_from_df(df, fn=""):
    data = [go.Scattergl(
            x = df.index,
            y = df.values[:,0]
        )]

    layout = dict(showlegend=False, title = fn)
    fig=dict(data=data, layout=layout)
    if __IPYTHON__:
        iplot(data)
    else:
        plot(data)


def plotly_multi_ts_from_df(temp, highlight_idx=[]):
    x = temp.index
    traces = []
    ips = temp.columns
    for j,i in enumerate(ips):
        if str(j) not in highlight_idx:
            trace = go.Scatter(
                x = x,
                y = temp[i],
                mode = 'lines',
                line = dict(
                    width=1.5
                ),
                name = i
            )
            traces.append(trace)
    for j,i in enumerate(ips):
        if str(j) in highlight_idx:
            _c = 'red'
            trace = go.Scatter(
                x = x,
                y = temp[i],
                mode = 'lines',
                line = dict(
                    color = _c,
                    width=1.5
                ),
                name = i
            )
            traces.append(trace)
    iplot(traces)
