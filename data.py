import pandas as pd
import matplotlib.pyplot as plt
from graphics import Graphics

class Data():
    """
    Class for managing and cleaning car sales data.
    """

    def __init__(self):
        """
        Constructor of the Data class.
        """
        # Path to the CSV file containing car sales data
        self.csv_path = 'data/car_data.csv'

    def clean_data(self):
        """
        Method to clean car sales data.
        """
        # Read the CSV file and load the data into a DataFrame
        df = pd.read_csv(self.csv_path)
        # Drop unwanted columns from the DataFrame
        df = df.drop(columns=['Car_id', 'Customer Name', 'Dealer_No ', 'Phone'], axis=1)
        # Rename some columns for clarity
        df = df.rename(columns={'Body Style': 'Style', 'Dealer_Region': 'AG_Loc'})
        return df

    def sales_x_day(self):
        """
        Method to analyze car sales per day.
        """
        # Clean car sales data
        df = self.clean_data()
        # Convert the 'Date' column to datetime type
        df['Date'] = pd.to_datetime(df['Date'])
        # Get the unique years present in the DataFrame
        years_unique = df['Date'].dt.year.unique()
        # Iterate over the unique years and display them to the user
        print("Select the year:")
        for index, year in enumerate(years_unique, start=1):
            print(f"{index}: {year}")
        # Prompt the user to choose a specific year or all years
        answer = input("3: all years\n")
        if answer.isdigit():
            answer = int(answer)
            # If a specific year is chosen
            if answer == 1 or answer == 2:
                filtered_data = df[df['Date'].dt.year == years_unique[answer -1]]
                confirmation = self.print_graph()
                if confirmation.isdigit():
                    confirmation = int(confirmation)
                    if confirmation == 1:
                        graphics = Graphics()
                        graphics.sales_x_day_graphics(filtered_data)
                    elif confirmation == 2:
                        filtered_data = filtered_data[['Date', 'Price']]
                        print(filtered_data)
                else:
                    print("It can't be a letter")
            # If all years are chosen
            elif answer == 3:
                time_series_data = df.groupby('Date').agg({'Price': 'sum'}).reset_index()
                confirmation = self.print_graph()
                if confirmation.isdigit():
                    confirmation = int(confirmation)
                    if confirmation == 1:
                        graphics = Graphics()
                        graphics.sales_x_day_graphics(time_series_data)
                    elif confirmation == 2:
                        time_series_data = df.groupby('Date').agg({'Price': 'sum'}).reset_index()
                        time_series_data = time_series_data[['Date', 'Price']]
                        print(time_series_data)
                else:
                    print("It can't be a letter")
        else:
            print("Enter a valid number")

    def store_top5(self):
        """
        Method to select and display the top 5 stores based on car sales.
        """
        # Clean the data
        df = self.clean_data()
        # Get the top 5 stores based on car sales
        compani_top5 = df["Dealer_Name"].value_counts()[:5]
        compani = compani_top5.index
        # Display the top 5 stores to the user
        print("Select the store:")
        for index, name in enumerate(compani_top5.index, start=1):
            print(f"{index}: {name}")
        # Prompt the user to choose a store or all stores
        answer = input(f"{len(compani_top5) + 1}: all the stores\n")
        if answer.isdigit():
            answer = int(answer)
            # If a specific store is chosen
            if 1 <= answer <= 5:
                store = compani_top5.loc[compani[answer - 1]]
                data_name = compani[answer - 1]
                data_value = store
                selected_data = {'Dealer_Name': [data_name], 'Count': [data_value]}
                selected_df = pd.DataFrame(selected_data)
                confirmation = self.print_graph()
                if confirmation.isdigit():
                    confirmation = int(confirmation)
                    if confirmation == 1:
                        graphics = Graphics()
                        graphics.store_top5_graphics(selected_df, data_name)
                    elif confirmation == 2:
                        print(selected_df)
                else:
                    print("It can't be a letter")
            # If all stores are chosen
            elif answer == 6:
                confirmation = self.print_graph()
                if confirmation.isdigit():
                    confirmation = int(confirmation)
                    if confirmation == 1:
                        graphics = Graphics()
                        graphics.store_top5_graphics(compani_top5, compani)
                    elif confirmation == 2:
                        print(compani_top5)
                else:
                    print("It can't be a letter")
        else:
            print("It can't be a letter")

    def top_10_company(self):
        """
        Method to display the top 10 companies based on car sales.
        """
        # Clean the data
        df = self.clean_data()
        # Group by company and aggregate sales
        Com_p = df.groupby(by=['Company']).agg({'Price': 'sum'})
        # Get the top 10 companies based on sales
        top_10 = Com_p.sort_values(by='Price', ascending=False)[:10]
        name_compani = top_10.index
        # Call the repetition function to handle common logic
        self.repetition(top_10, name_compani, "top_10_company_graphics")

    def cars_sold_per_month(self):
        """
        Method to analyze car sales per month.
        """
        # Clean the data
        df = self.clean_data()
        # Convert the 'Date' column to datetime and extract month
        df['Date'] = pd.to_datetime(df['Date'])
        df['Date'] = df['Date'].dt.to_period('M')
        # Drop duplicate months
        df_sin_repeticiones = df.drop_duplicates(subset=['Date'])
        df_sin_repeticiones = df_sin_repeticiones['Date']
        months = df_sin_repeticiones.values
        # Count cars sold per month
        carros_por_mes = df['Date'].value_counts()
        carros_por_mes = carros_por_mes.sort_index(ascending=True)
        # Call the repetition function to handle common logic
        self.repetition(carros_por_mes, months, "cars_sold_per_month_graphics")

    def top_10_car(self):
        """
        Method to display the top 10 car models based on sales from 2022 to 2023.
        """
        # Clean the data
        df = self.clean_data()
        # Convert the 'Date' column to datetime and filter data for years 2022 and 2023
        df['Date'] = pd.to_datetime(df['Date'])
        carros_2020_2023 = df[df['Date'].dt.year.isin([2022, 2023])]
        # Get the top 10 car models based on sales
        car_name = carros_2020_2023['Model'].value_counts().head(10)
        car_name = car_name.index
        carros_mas_populares = carros_2020_2023['Model'].value_counts().head(10)
        # Call the repetition function to handle common logic
        self.repetition(carros_mas_populares, car_name, "top_10_car_graphics")

    def growing_companies(self):
        """
        Method to analyze the growth rate of car companies.
        """
        # Clean the data
        df = self.clean_data()
        # Convert the 'Date' column to datetime and extract year
        df["Date"] = pd.to_datetime(df["Date"])
        df["Date"] = df["Date"].dt.year
        # Group by company and year, calculate annual income, and calculate growth rate
        ventas_por_fabricante_y_anio = df.groupby(['Company', 'Date'])['Annual Income'].sum().reset_index()
        ventas_por_fabricante_y_anio['Tasa_Crecimiento'] = ventas_por_fabricante_y_anio.groupby('Company')[
            'Annual Income'].pct_change()
        ventas_por_fabricante_y_anio = ventas_por_fabricante_y_anio.dropna()
        ventas_por_fabricante_y = ventas_por_fabricante_y_anio[['Company', 'Tasa_Crecimiento']]
        ventas_por_fabricante_y.set_index('Company', inplace=True)
        # Display the data
        print(ventas_por_fabricante_y)
        company_names = ventas_por_fabricante_y.index
        print(company_names)
        # Call the repetition function to handle common logic
        self.repetition(ventas_por_fabricante_y, company_names, "growing_companies_graphics")

    def repetition(self, data_informacion, data_name, funcion_name):
        """
        Method to handle repeated logic for displaying data and graphs.
        """
        print("Select the store:")
        for index, name in enumerate(data_informacion.index, start=1):
            print(f"{index}: {name}")
        # Prompt the user to choose a data point or all data points
        answer = input(f"{len(data_informacion) + 1}: all the stores\n")
        if answer.isdigit():
            answer = int(answer)
            # If a specific data point is chosen
            if answer <= len(data_informacion):
                store = data_informacion.loc[data_name[answer - 1]]
                data_name = data_name[answer - 1]
                data_value = store
                selected_data = {'Dealer_Name': [data_name], 'Count': [data_value]}
                selected_df = pd.DataFrame(selected_data)
                confirmation = self.print_graph()
                if confirmation.isdigit():
                    confirmation = int(confirmation)
                    if confirmation == 1:
                        graphics = Graphics()
                        function = graphics.get_funcion_by_name(funcion_name)
                        function(selected_df, data_name)
                    elif confirmation == 2:
                        print(selected_df)
                else:
                    print("It can't be a letter")
            # If all data points are chosen
            elif answer == (len(data_informacion) + 1):
                confirmation = self.print_graph()
                if confirmation.isdigit():
                    confirmation = int(confirmation)
                    if confirmation == 1:
                        graphics = Graphics()
                        function = graphics.get_funcion_by_name(funcion_name)
                        function(data_informacion, data_name)
                    elif confirmation == 2:
                        print(data_informacion)
                else:
                    print("It can't be a letter")
        else:
            print("It can't be a letter")

    def print_graph(self):
        """
        Method to prompt the user for graph display preference.
        """
        answer = input("Do you want to see the graph? \n"
                       "1: Yes\n"
                       "2: No\n"
                       )
        return answer

#a = Data()
#a.growing_companies()