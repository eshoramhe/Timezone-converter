import streamlit as st
import datetime
import pytz

# --- Page Configuration (must be at the very top) ---
st.set_page_config(
    page_title="Timezone Converter",
    page_icon="🌍",
    layout="centered", # or "wide"
    initial_sidebar_state="expanded" # "auto", "expanded", "collapsed"
)


# Title of the web app
st.title("🌍 Timezone Converter")

st.write(
    """
    This app allows you to convert a specific time from one timezone to another.
    """
)

# --- Advert in Sidebar ---
with st.sidebar:
    # Explicitly stating this is an advert space
    st.markdown("**This is an advert space.**")
    st.header("Sponsor / Advert Space")
    st.image("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png", width=150,
             caption="[Your Company Logo/Ad Banner]") # Replace with your ad image URL
    st.markdown("Visit our [**Partner Website**](https://www.example.com) for amazing services!") # Replace with your link
    st.info("Your ad content goes here! Limited time offer!")
    st.markdown("---") # Separator

# --- Collapsible Advert in Main Page ---
with st.expander("🎉 Special Offer: Get 20% Off Our Premium Service!", expanded=False):
    st.write(
        """
        Don't miss out on our limited-time offer! Upgrade to premium for:
        * Ad-free experience
        * Advanced features
        * Priority support
        """
    )
    st.link_button("Learn More & Claim Offer", "https://www.premiumservice.com", help="Click to get your discount!")
    st.image("https://via.placeholder.com/300x100?text=Premium+Ad", caption="Premium Service Banner")


# Input for date
st.header("1. Enter Date and Time")
col1, col2 = st.columns(2)
with col1:
    date_input = st.date_input("Select a date", value=datetime.date.today())

with col2:
    time_input = st.time_input("Select a time (HH:MM)", value=None)

# --- Handling potential None value for time_input ---
if time_input is None:
    st.warning("Please enter a time.")
    st.stop() # Stop the execution until a time is entered.


# Combine date and time
combined_datetime = datetime.datetime.combine(date_input, time_input)

st.write(f"You selected: **{combined_datetime.strftime('%Y-%m-%d %H:%M:%S')}**")

# Input for source timezone
st.header("2. Select Source Timezone")
all_timezones = pytz.all_timezones
source_timezone_str = st.selectbox("From Timezone", all_timezones, index=all_timezones.index('America/New_York'))

source_tz = pytz.timezone(source_timezone_str)
localized_datetime = source_tz.localize(combined_datetime)

st.write(f"The time in **{source_timezone_str}** is: **{localized_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')}**")

# Input for target timezone
st.header("3. Select Target Timezone")
target_timezone_str = st.selectbox("To Timezone", all_timezones, index=all_timezones.index('Europe/London'))

target_tz = pytz.timezone(target_timezone_str)
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
