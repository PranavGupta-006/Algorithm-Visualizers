import streamlit as st
import time
import os
import numpy
import pandas
from binaryLogic import bins, steps


st.title("Binary Search Visualizer")
st.header("This App will help you visualize Binary Search")

text = st.text_input("Enter a Sorted Array : ")
array = [int(x.strip()) for x in text.split(",") if x.strip() != ""]

value = st.number_input("Enter The Key : ", step=1)
search = st.button("Start Binary Search")

if "curr_step" not in st.session_state:
    st.session_state.curr_step = 0

if "steps_list" not in st.session_state:
    st.session_state.steps_list = []

if "index" not in st.session_state:
    st.session_state.index = -1

if search:
    if len(array) == 0:
        st.error("Please enter a valid sorted array.")
    else:
        st.session_state.index = bins(array, value)
        st.session_state.steps_list = list(steps(array, value))
        st.session_state.curr_step = 0

if st.session_state.index != -1 and st.session_state.steps_list:

    st.subheader("Binary Search Steps")

    curr = st.session_state.curr_step
    low, mid, high = st.session_state.steps_list[curr]

    st.markdown(f"### Step {curr + 1}")
    st.write(f"Low: {low}, Mid: {mid}, High: {high}")

    cols = st.columns(len(array))
    for j, col in enumerate(cols):
        if j == mid:
            col.markdown(f"🔵 Mid → {array[j]}")
        elif j == low:
            col.markdown(f"🟢 Low → {array[j]}")
        elif j == high:
            col.markdown(f"🔴 High → {array[j]}")
        else:
            col.markdown(str(array[j]))

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("⏪ Back") and curr > 0:
            st.session_state.curr_step -= 1

    with col2:
        if st.button("Next ⏭️") and curr < len(st.session_state.steps_list) - 1:
            st.session_state.curr_step += 1

    with col3:
        if st.button("🔄 Reset"):
            st.session_state.curr_step = 0

    if curr == len(st.session_state.steps_list) - 1:
        st.success(f"Key Found at Index (0-indexed): {st.session_state.index}")
        st.success(f"Key Found at Index (1-indexed): {st.session_state.index + 1}")

elif search:
    st.error("Key Does Not exist in this array.")
