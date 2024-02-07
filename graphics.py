import matplotlib.pyplot as plt
import pandas as pd
import inspect
class Graphics:
    def __init__(self):
        self.fig = plt.figure()  # Initialize a figure object for plotting

    def sales_x_day_graphics(self, sales_data):
        """
        Function to plot sales data over time.

        Parameters:
            sales_data (DataFrame): DataFrame containing sales data with columns 'Date' and 'Price'.
        """
        plt.figure(figsize=(12, 6))  # Set figure size
        plt.plot(sales_data['Date'], sales_data['Price'], label='Total Sales')  # Plot sales data
        # Customize the plot
        plt.title('Total Sales Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.legend()  # Show legend
        plt.grid(True)  # Show grid
        plt.show()  # Display the plot

    def store_top5_graphics(self, sales_data, xlabel):
        """
        Function to plot top 5 dealer names.

        Parameters:
            sales_data (DataFrame): DataFrame containing sales data with column 'Dealer_Name'.
            xlabel (str): Label for the x-axis.
        """
        plt.figure(figsize=(10, 6))  # Set figure size
        sales_data.plot(kind='bar', color='skyblue')  # Plot top 5 dealer names
        # Customize the plot
        plt.title('Top 5 Most Common Dealer Names')
        plt.xlabel(xlabel)
        plt.ylabel('Number of Occurrences')
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
        plt.grid(axis='y', linestyle='--', alpha=0.7)  # Show grid
        plt.show()  # Display the plot

    def top_10_company_graphics(self, data, xlabel):
        """
        Function to plot top 10 companies by income.

        Parameters:
            data (DataFrame): DataFrame containing company data with column 'Count'.
            xlabel (str): Label for the x-axis.
        """
        plt.figure(figsize=(12, 6))  # Set figure size
        letra = data["Count"]
        nuevo_valor = str(letra.values)
        nuevo_valor = pd.Series(nuevo_valor).str.extract(r':(.*)')
        nuevo_valor = nuevo_valor[0].str.split(',').str[0]
        print(nuevo_valor.head())
        letra_str = str(letra.values)
        mi_serie_limpiada = pd.Series(letra_str).str.extract('(\d+)')
        index_df = mi_serie_limpiada.reset_index()
        index_df.plot(kind='bar', color='skyblue')  # Plot top 10 companies by income

        # Customize the plot
        plt.title('Top 10 Companies by Income')
        plt.xlabel('Income')
        plt.ylabel(xlabel)
        # Show the plot
        plt.show()

    def get_funcion_by_name(self, nombre):
        """
        Function to get a method by its name.

        Parameters:
            nombre (str): Name of the method to retrieve.

        Returns:
            method: The method with the given name.
        """
        for name in dir(self):
            attr = getattr(self, name)
            if inspect.ismethod(attr) and name == nombre:
                return attr

    def cars_sold_per_month_graphics(self, data, month):
        """
        Function to plot the number of cars sold per month.

        Parameters:
            data (Series): Series containing the number of cars sold per month.
            month (str): Label for the month.
        """
        data.plot(kind='bar', color='skyblue')  # Plot number of cars sold per month
        plt.title('Number of Cars Sold per Month')
        plt.xlabel(f"{month}")
        plt.ylabel('Number of Cars Sold')
        plt.show()  # Display the plot

    def top_10_car_graphics(self, data, car_name):
        """
        Function to plot the top 10 most popular car brands.

        Parameters:
            data (DataFrame): DataFrame containing the top 10 car brands with column 'Count'.
            car_name (str): Label for the car brand.
        """
        plt.figure(figsize=(10, 6))  # Set figure size
        data.plot(kind='bar', color='skyblue')  # Plot top 10 most popular car brands
        plt.title('Top 10 Popular Brands in 2022 and 2023')
        plt.xlabel(f"{car_name}")
        plt.ylabel('Frequency')
        plt.show()  # Display the plot

    def growing_companies_graphics(self, data, companies):
        """
        Function to plot the distribution of market share by manufacturer.

        Parameters:
            data (DataFrame): DataFrame containing the market share distribution with columns 'Dealer_Name' and 'Count'.
            companies (str): Label for the companies.
        """
        # First plot: pie chart
        labels = data['Dealer_Name']
        values = data['Count']
        letra_str = str(values)
        mi_serie_limpiada = pd.Series(letra_str).str.extract('(\d+\.\d+)')
        index_df = mi_serie_limpiada.reset_index()
        values_float = index_df.iloc[0].astype(float)
        serie_sin_cero = values_float[0]
        sizes = [serie_sin_cero]
        label = labels.iloc[0]
        label = label.split()
        # Second plot: bar chart
        plt.subplot(1, 2, 2)
        plt.bar(label, sizes)  # Provide data for bar chart
        plt.title('Market Share Distribution by Manufacturer')
        plt.xlabel('Manufacturer')
        plt.ylabel('Count')
        # Show the plots
        plt.show()  # Display the plots