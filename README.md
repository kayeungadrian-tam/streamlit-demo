<div align="center">

<h1> Streamlit demo<br>
<img src="https://img.shields.io/badge/made%20with-LOVE-red?style=plastic">
<img src="https://img.shields.io/badge/license-MIT-blue?style=plastic">
<img src="https://img.shields.io/badge/streamlit-live-green?style=plastic&logo=streamlit&">
</h1>
</div>

# ✨ What
This repo aims to summarize the basic functionalities of streamlit and provide a demonstration.

# 🎉 Streamlit

Check below for the offical docs for Streamlit.

Easy. Intuitive. Straightforward. Python.

Amazing stuff by the developers.

https://streamlit.io/

# 👷 Functionalities


1. Write
1. Input Type
    1. Boolean
    1. Select
    1. Text
    1. Numerical
1. Image
1. Layout
1. Display data
1. Charts
---
## Write

```python
st.markdown("# Head1")
st.markdown("## Head2")
st.markdown("### Head2")

st.markdown("* List 1")
st.markdown("* List 2")
st.markdown("* List 3")

st.markdown("1. Item 1")
st.markdown("1. Item 2")
st.markdown("1. Item 3")

st.write("write")
```

## Input Type

Boolean

```python
my_list = ['A1', 'A2', 'A3']

check = st.checkbox("Checkbox")
button = st.button("button (snow)")
radio = st.radio("Radio", my_list)
```

Select

```python
selectbox = st.selectbox("Select-box", my_list)
multiselect = st.multiselect("Multi-select", my_list)
select_slider = st.select_slider("Select Slider", my_list)
```

Text

```python
text = st.text_input("Input")
text_area = st.text_area("Text Area")
```
Numerical

```python
slider = st.slider("Slider", 0, 100)
number_input = st.number_input("Number input", 0, 100)

```



## Image
```python
image_array = st.image(
    np.random.randint(0, 255, size=(128, 128, 3)), caption="Numpy array"
)

image_url = st.image(
    "https://randomwordgenerator.com/img/picture-generator/57e7d4414d51a814f1dc8460962e33791c3ad6e04e50744172287cd09e49cd_640.jpg",
    caption="Caption",
)
```


## Layout
```python
st.markdown("### 1. Sidebar")
st.sidebar.text_input("text input")
st.sidebar.text_area("text area")

st.markdown("### 2. Columns")
col1, col2 = st.columns(2)

with col1:
    st.write("Columns 1")
    st.radio("Radio2", make_list("E"))

with col2:
    multiselect2 = st.multiselect("Multi-select 2", make_list("F"))
    text_2 = st.text_input("Input 2")

```

## Display data

```python
def make_json():
    return {
        "foo": "bar",
        "baz": "boz",
        "stuff": [
            "stuff 1",
            "stuff 2",
            "stuff 3",
            "stuff 5",
        ],
    }


st.markdown("### json")
st.json(make_json(), expanded=False)

col1, col2 = st.columns(2)
with col1:
    st.markdown("### map_data (table)")
    st.table(make_map())
with col2:
    st.markdown("### chart_data (dataframe)")
    data = make_data()
    st.dataframe(data.style.highlight_max(), use_container_width=True)

col11, col12 = st.columns(2)
col11.metric(label="Latitude", value="35.67 °N", delta="0")
col12.metric(label="Longitude", value="139.65 °E", delta="-0")

```


## Charts

```python

def make_data():
    return pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])


def make_map():
    return pd.DataFrame(
        np.random.randn(20, 2) / [50, 50] + [35.67, 139.65], columns=["lat", "lon"]
    )

chart_data = make_data()
map_data = make_map()

st.markdown("### line_chart")
st.line_chart(chart_data)

st.markdown("### area_chart")
st.area_chart(chart_data)

st.markdown("### bar_chart")
st.bar_chart(chart_data)

st.map(map_data)


```