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
        plt.figure(figsize=(12, 6))  # Tamaño del gráfico
        plt.plot(sales_data['Date'], sales_data['Price'], marker='o', label='Total Sales')  # Graficar la serie de datos
        # Personalizar el gráfico
        plt.title('Total Sales Over Time')
        plt.xlabel('Date')
        plt.ylabel('money from daily sales')
        plt.legend()
        plt.grid(True)
        legend_labels = ['Total Sales by Day']
        plt.legend(legend_labels)
        plt.show()

    def store_top5_graphics(self, sales_data, xlabel):
        """
        Function to plot top 5 dealer names.

        Parameters:
            sales_data (DataFrame): DataFrame containing sales data with column 'Dealer_Name'.
            xlabel (str): Label for the x-axis.
        """
        if len(sales_data) == 1:
          plt.figure(figsize=(10, 6))  # Set figure size
          sales_data = sales_data.set_index('Dealer_Name')
          sales_data.plot(kind='bar', color='skyblue')  # Plot top 5 dealer names
          # Customize the plot
          plt.title('Top 5 Most Common Dealer Names')
          plt.xlabel('Dealer_Name')
          plt.ylabel('Cars sold')
          plt.xticks(rotation=0, ha='center')  # Rotate x-axis labels for readability
          plt.grid(axis='y', linestyle='--', alpha=0.7)  # Show grid
          legend_labels = ['Number of cars sold']
          plt.legend(legend_labels)
          plt.show()  # Display the plot
        else:
            sales_data.plot(kind='bar', color='skyblue')  # Plot top 5 dealer names
            # Customize the plot
            plt.title('Top 5 Most Common Dealer Names')
            plt.xlabel('Dealer_Name')
            plt.ylabel('Cars sold')
            plt.xticks(rotation=45, ha='center')  # Rotate x-axis labels for readability
            plt.grid(axis='y', linestyle='--', alpha=0.7)  # Show grid
            legend_labels = ['Number of cars sold']
            plt.legend(legend_labels)
            plt.show()  # Display the plo

    def top_10_company_graphics(self, data, xlabel):
        """
        Function to plot top 10 companies by income.

        Parameters:
            data (DataFrame): DataFrame containing company data with column 'Count'.
            xlabel (str): Label for the x-axis.
        """
        if len(data) ==1:
          plt.figure(figsize=(12, 6))  # Set figure size
          letra = data["Count"]
          nuevo_valor = str(letra.values)
          nuevo_valor = pd.Series(nuevo_valor).str.extract('(\d+)')
          nuevo_valor = nuevo_valor[0].str.split(',').str[0] #serie
          letra_str = data['Dealer_Name']
          index_df = pd.concat([letra_str, nuevo_valor], ignore_index=True)
          nueva_serie = pd.Series(index_df[1], index=[index_df[0]])
          nueva_serie = nueva_serie.astype(int)
          nueva_serie.plot(kind='bar', color='skyblue')
          # Customize the plot
          plt.title('Top 10 Companies by Income')
          plt.xlabel("Companies")
          plt.ylabel("Money in sales 2022-23")
          plt.ticklabel_format(style='plain', axis='y')
          plt.xticks(rotation=45, ha='right')  # Rotar y alinear las etiquetas del eje x
          legend_labels = ['Money in sales']
          plt.legend(legend_labels)
        # Show the plot
          plt.show()
        else:
            data.plot(kind='bar', color='skyblue')
            # Customize the plot
            plt.title('Top 10 Companies by Income')
            plt.xlabel("Companies")
            plt.ylabel("Sales 2022-23")
            plt.ticklabel_format(style='plain', axis='y')
            plt.xticks(rotation=45, ha='right')  # Rotar y alinear las etiquetas del eje x
            legend_labels = ['Money in sales']
            plt.legend(legend_labels)
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
        if len(data) ==1:
          data = data.set_index('Dealer_Name')
          data.plot(kind='bar', color='skyblue')  # Plot number of cars sold per month
          plt.title('Number of Cars Sold per Month')
          plt.xlabel("Month and year")
          plt.ylabel('Number of Cars Sold')
          plt.xticks(rotation=0, ha='center')  #
          legend_labels = ['number of cars sold']
          plt.legend(legend_labels)
          plt.show()  # Display the plot
        else:
            data.plot(kind='bar', color='skyblue')  # Plot number of cars sold per month
            plt.title('Number of Cars Sold per Month')
            plt.xlabel("Month and year")
            plt.ylabel('Number of Cars Sold')
            plt.xticks(rotation=35, ha='center')  #
            legend_labels = ['number of cars sold']
            plt.legend(legend_labels)
            plt.show()  # Display the plo

    def top_10_car_graphics(self, data, car_name):
        """
        Function to plot the top 10 most popular car brands.

        Parameters:
            data (DataFrame): DataFrame containing the top 10 car brands with column 'Count'.
            car_name (str): Label for the car brand.
        """
        if len(data) == 1:
          data = data.set_index('Dealer_Name')
          plt.figure(figsize=(10, 6))  # Set figure size
          data.plot(kind='bar', color='skyblue')  # Plot top 10 most popular car brands
          plt.title('Top 10 best-selling cars in 2022-2023')
          plt.xticks(rotation=0, ha='center')  #
          plt.xlabel(f"Car")
          legend_labels = ['number of cars sold']
          plt.legend(legend_labels)
          plt.ylabel('Count')
          plt.show()  # Display the plot
        else:
            plt.figure(figsize=(10, 6))  # Set figure size
            data.plot(kind='bar', color='skyblue')  # Plot top 10 most popular car brands
            plt.title('Top 10 best-selling cars in 2022-2023')
            plt.xticks(rotation=0, ha='center')  #
            plt.xlabel(f"Car")
            legend_labels = ['number of cars sold']
            plt.legend(legend_labels)
            plt.ylabel('Count')
            plt.show()  # Displ
    def growing_companies_graphics(self, data, companies):
        """
        Function to plot the distribution of market share by manufacturer.

        Parameters:
            data (DataFrame): DataFrame containing the market share distribution with columns 'Dealer_Name' and 'Count'.
            companies (str): Label for the companies.
        """
        if len(data.index) == 1:
            label = data['Tasa_Crecimiento']
            name = data.index
            plt.figure(figsize=(10, 6))
            plt.bar(name,label)  # Provide data for bar chart
            plt.title('Market Share Distribution by Manufacturer')
            plt.xlabel('Company')
            plt.ylabel('growth in %')
            legend_labels = ['growth in %']
            plt.legend(legend_labels)
            plt.xticks(rotation=45, ha='right')  # Rotar y alinear las etiquetas del eje x
            plt.tight_layout()
            # Show the plots
            plt.show()  # Display the pl
        else:
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
         plt.subplot(1, 2, 2)
         plt.bar(label, sizes)  # Provide data for bar chart
         legend_labels = ['growth in %']
         plt.legend(legend_labels)
         plt.title('Market Share Distribution by Manufacturer')
         plt.xlabel('Manufacturer')
         plt.ylabel('growth in %')
         # Show the plots
         plt.show()  # Display the plots

    def prferencia_modelo_graphics(self,data,model):
        if len(data.index) == 1:
          filtre = data['Count'].to_string()
          filtre = filtre.split('\n')
          gener = filtre[0].split('  ')[2]
          female = filtre[1].split('  ')[2]
          male = filtre[2].split('   ')[2]
          data = {
            'Model': data['Dealer_Name'],
            'Male': int(male),  # Valores ficticios para los hombres
            'Female': int(female)  # Valores ficticios para las mujeres
          }
          df = pd.DataFrame(data)
          df.set_index('Model', inplace=True)
          df.plot(kind='bar', stacked=True)
          legend_labels = ['number of cars sold']
          plt.legend(legend_labels)
          plt.xticks(rotation=0, ha='center')
          # Personalizar el gráfico
          plt.title('Number of cars sold by model by gender 2022-2023')
          plt.xlabel('Model')
          plt.ylabel('number of cars sold')
          # Mostrar el gráfico
          plt.show()
        else:
            data.plot(kind='bar', stacked=True)
            legend_labels = ['number of cars sold']
            plt.legend(legend_labels)
            # Personalizar el gráfico
            plt.title('Number of cars sold by model by gender 2022-2023')
            plt.xlabel('Model')
            plt.ylabel('number of cars sold')
            plt.xticks(rotation=0, ha='center')
            # Mostrar el gráfico
            plt.show()
    def transmission_type_graphics(self,data, name):
        if len(data.index) == 1:
          filtre = data['Count'].to_string()
          filtre = filtre.split('\n')
          number = filtre[0].split('  ')[4]
          data = {
            'Transmission': data['Dealer_Name'],
            'Count': float(number),  # Valores ficticios para los hombres
          }
          df_data = pd.DataFrame(data)
          df_data.set_index('Transmission', inplace=True)
          df_data.plot(kind='bar', stacked=True)
          legend_labels = ['Number of people %']
          plt.legend(legend_labels)
          # Personalizar el gráfico
          plt.title('Number of cars sold by model by gender 2022-2023')
          plt.xlabel('Transmission')
          plt.ylabel('Number of people %')
          plt.xticks(rotation=0, ha='center')
          # Mostrar el gráfico
          plt.show()
        else:
            data.plot(kind='bar', stacked=True)
            legend_labels = ['Number of people %']
            plt.legend(legend_labels)
            # Personalizar el gráfico
            plt.title('Number of cars sold by model by gender 2022-2023')
            plt.xlabel('Transmission')
            plt.ylabel('Number of people %')
            plt.xticks(rotation=0, ha='center')
            plt.show()
