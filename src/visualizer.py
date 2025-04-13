import matplotlib.pyplot as plt

def plot_missing_data(df):
    missing_data = df.isnull().sum()
    missing_data = missing_data[missing_data > 0]
    if not missing_data.empty:
        missing_data.plot(kind='bar', color='skyblue')
        plt.title('Missing Data per Column')
        plt.xlabel('Columns')
        plt.ylabel('Number of Missing Values')
        plt.show()
    else:
        print("No missing data to visualize.")
