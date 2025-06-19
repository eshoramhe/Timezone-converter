import streamlit as st
import datetime
import pytz

# Title of the web app
st.title("🌍 Timezone Converter")

st.write(
    """
    This app allows you to convert a specific time from one timezone to another.
    """
)

# Input for date
st.header("1. Enter Date and Time")
col1, col2 = st.columns(2)
with col1:
    date_input = st.date_input("Select a date", datetime.date.today())
with col2:
    time_input = st.time_input("Select a time", datetime.datetime.now().time())

# Combine date and time
# It's good practice to ensure the user has actually selected something before proceeding,
# though the widgets always return a value.
combined_datetime = datetime.datetime.combine(date_input, time_input)

st.write(f"You selected: **{combined_datetime.strftime('%Y-%m-%d %H:%M:%S')}**")

# Input for source timezone
st.header("2. Select Source Timezone")
# Get a list of all available timezones
all_timezones = pytz.all_timezones
source_timezone_str = st.selectbox("From Timezone", all_timezones, index=all_timezones.index('America/New_York'))

# Create a timezone object
source_tz = pytz.timezone(source_timezone_str)

# Localize the combined datetime to the source timezone
localized_datetime = source_tz.localize(combined_datetime)

st.write(f"The time in **{source_timezone_str}** is: **{localized_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')}**")

# Input for target timezone
st.header("3. Select Target Timezone")
target_timezone_str = st.selectbox("To Timezone", all_timezones, index=all_timezones.index('Europe/London'))

# Create a timezone object for the target
target_tz = pytz.timezone(target_timezone_str)

# Convert the localized datetime to the target timezone
converted_datetime = localized_datetime.astimezone(target_tz)

st.header("4. Converted Time")
st.success(
    f"**{localized_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')}** "
    f"in **{source_timezone_str}** is "
    f"**{converted_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')}** "
    f"in **{target_timezone_str}**."
)

st.write("---")
st.info("Developed with ❤️ using Streamlit and pytz")
