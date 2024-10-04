import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

days_df = pd.read_csv("day.csv")
days_df.head()

hours_df = pd.read_csv("hour.csv")
hours_df.head()

st.title("🎈 Bike Sharing")
st.write(
    "."
)

with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

st.subheader('Daily User')

col1, col2 = st.columns(2)
 
with col1:
    hourly_avg_users = hours_df.groupby(['hr', 'weekday'])['cnt'].mean().unstack()

    plt.figure(figsize=(12, 6))
    for weekday in range(7):
    plt.plot(hourly_avg_users.index, hourly_avg_users[weekday], label=f'Weekday {weekday}')

    plt.xlabel('Hour')
    plt.ylabel('Average Number of Users')
    plt.title('Average Number of Users per Hour in a Week')
    plt.legend()
    plt.grid(True)
    plt.show()

with col2:
    plt.figure(figsize=(12, 6))
    plt.plot(days_df['dteday'], days_df['casual'], label='Casual Users')
    plt.plot(days_df['dteday'], days_df['registered'], label='Registered Users')
    plt.xlabel('Date (Start: ' + days_df['dteday'].iloc[0] + ', End: ' + days_df['dteday'].iloc[-1] + ')')
    plt.ylabel('Number of Users')
    plt.title('Daily Casual and Registered Users')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(days_df['casual'], color="skyblue", label="Casual", kde=True)
sns.histplot(days_df['registered'], color="orange", label="Registered", kde=True)
plt.title("Distribution of Casual vs Registered Users (Daily)")
plt.legend()

plt.subplot(1, 2, 2)
sns.histplot(hours_df['casual'], color="skyblue", label="Casual", kde=True)
sns.histplot(hours_df['registered'], color="orange", label="Registered", kde=True)
plt.title("Distribution of Casual vs Registered Users (Hourly)")
plt.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))

sns.boxplot(x="weathersit", y="cnt", data=days_df)
plt.title("Bike Rentals vs Weather Situation (Daily)")
plt.xlabel("Weather Situation")
plt.ylabel("Total Rentals")
plt.show()

plt.figure(figsize=(10, 8))
corr_matrix = days_df[['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']].corr()
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation Matrix for Daily Data")
plt.show()
