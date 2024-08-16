'''

    @Author: Ayush Prajapati
    @Date: 24-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 24-07-2024 
    @Title : Python program to Convert the temperature from Fahrenheit to Celsius or vice versa

'''


class Temperature:
    @staticmethod
    def temperatureConversion(temp, unit):
        """
        Description:
            This function converts temperature between Fahrenheit and Celsius.
        Parameters:
            temp: Temperature value to convert
            unit: Current unit of temperature ('F' for Fahrenheit, 'C' for Celsius)
        Return:
            float: Converted temperature value
        """
        if unit.upper() == 'F':
            return (temp - 32) * 5/9
        elif unit.upper() == 'C':
            return (temp * 9/5) + 32
        else:
            return None


def main():

      temp = float(input("Enter temperature value: "))
      unit = input("Enter unit (F for Fahrenheit, C for Celsius): ")

      if unit.upper() in ['F', 'C']:
          converted_temp = Temperature.temperatureConversion(temp, unit)
          if converted_temp is not None:
              new_unit = 'Celsius' if unit.upper() == 'F' else 'Fahrenheit'
              print(f"{temp}°{unit.upper()} is equal to {converted_temp:.2f}°{new_unit[0]}")
          else:
              print("Conversion failed. Please check your input.")
      else:
          print("Invalid unit. Please enter 'F' for Fahrenheit or 'C' for Celsius.")


if __name__ == "__main__":
    main()
