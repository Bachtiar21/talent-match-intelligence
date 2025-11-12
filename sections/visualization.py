import plotly.express as px
import plotly.graph_objects as go

def bar_match(df):
    fig = px.bar(
        df,
        x="final_match_rate",
        y="employee_id",
        orientation="h",
        color="final_match_rate",
        color_continuous_scale="Blues",
        title="Ranked Talent Match Score"
    )
    fig.update_layout(yaxis=dict(autorange="reversed"))
    return fig

def heatmap(df):
    corr = df.corr(numeric_only=True)
    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="Blues",
        title="Correlation Matrix"
    )
    return fig

def radar(df, features):
    row = df.iloc[0]  # radar for first employee
    values = [row[f] for f in features]

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=features,
        fill='toself'
    ))
    fig.update_layout(title="Radar Chart")
    return fig
