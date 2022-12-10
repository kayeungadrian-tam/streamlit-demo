import pandas as pd
import numpy as np
import streamlit as st

# Helper functions
def show_func_name(func):
    def wrapper(*arg, **kwargs):
        st.markdown(f"# {func.__name__}\n---")
        return func(*arg, **kwargs)

    return wrapper


def make_list(letter):
    return [f"{letter}{x}" for x in range(1, 4)]


def make_data():
    return pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])


def make_map():
    return pd.DataFrame(
        np.random.randn(20, 2) / [50, 50] + [35.67, 139.65], columns=["lat", "lon"]
    )


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


def set_page_config():
    st.set_page_config(
        page_title="Streamlit demo",
        page_icon=":shark:",
        initial_sidebar_state="expanded",
        layout="centered",
        menu_items={
            "Get Help": "https://www.extremelycoolapp.com/help",
            "Report a bug": "https://www.extremelycoolapp.com/bug",
            "About": "# This is a header. This is an *extremely* cool app!",
        },
    )


@show_func_name
def basic_write():
    with st.echo():

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


@show_func_name
def input_type():

    with st.echo():
        check = st.checkbox("Checkbox")

        if check:
            st.warning("warning! checked", icon="⚠️")

        button = st.button("button (snow)")
        if button:
            st.snow()

        selectbox = st.selectbox("Select-box", make_list("A"))
        if selectbox:
            st.success(f"Selected! {selectbox}", icon="✅")

        multiselect = st.multiselect("Multi-select", make_list("B"))
        if multiselect:
            st.error(f"You selected: {multiselect}", icon="🚨")

        radio = st.radio("Radio", make_list("C"))

        text = st.text_input("Input")
        if text:
            st.info(f"input: {text}", icon="ℹ️")

        text_area = st.text_area("Text Area")
        slider = st.slider("Slider", 0, 100)
        select_slider = st.select_slider("Select Slider", make_list("D"))
        number_input = st.number_input("Number input", 0, 100)


@show_func_name
def media():
    with st.echo():
        image_array = st.image(
            np.random.randint(0, 255, size=(128, 128, 3)), caption="Numpy array"
        )

        image_url = st.image(
            "https://randomwordgenerator.com/img/picture-generator/57e7d4414d51a814f1dc8460962e33791c3ad6e04e50744172287cd09e49cd_640.jpg",
            caption="Caption",
        )


@show_func_name
def layout():
    with st.echo():
        st.markdown("### 1. Sidebar")
        st.sidebar.text_input("text input")  # 引数に入力内容を渡せる
        st.sidebar.text_area("text area")

        st.markdown("### 2. Columns")
        col1, col2 = st.columns(2)

        with col1:
            st.write("Columns 1")
            st.radio("Radio2", make_list("E"))

        with col2:
            multiselect2 = st.multiselect("Multi-select 2", make_list("F"))
            text_2 = st.text_input("Input 2")


@show_func_name
def charts():
    chart_data = make_data()

    st.markdown("### line_chart")
    st.line_chart(chart_data)

    st.markdown("### area_chart")
    st.area_chart(chart_data)

    st.markdown("### bar_chart")
    st.bar_chart(chart_data)

    map_data = make_map()
    st.map(map_data)


@show_func_name
def display_data():
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


def main():
    set_page_config()
    basic_write()
    input_type()
    media()
    layout()
    display_data()
    charts()


if __name__ == "__main__":
    main()
