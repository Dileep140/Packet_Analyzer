import os #this module used for interacting with operating system.
from datetime import date,datetime #
import pandas as pd # Pandas is a powerful data manipulation and analysis library for Python.
import matplotlib.pyplot as plt
import webbrowser
from jinja2 import Template

class PCAPAnalyzer:
    def __init__(self, csv_file):
        try:
            self.df = pd.read_csv(csv_file) #read csv file to dataframe
            self.df.fillna('', inplace=True) #This line fills any missing (NaN) values in the DataFrame with an empty string. The inplace=True argument modifies the DataFrame in place.
            self.num_packets = len(self.df) # Count number of packets
            self.filename=os.path.basename(csv_file)
        #This block of code catches the FileNotFoundError exception, which occurs when the specified CSV file is not found at the provided file path.
        except FileNotFoundError:
            print(f"Error: File '{csv_file}' not found.")
            raise
        #This block of code catches the EmptyDataError from pandas, which happens when the CSV file is empty or contains no data.
        except pd.errors.EmptyDataError:
            print(f"Error: File '{csv_file}' is empty.")
            raise
        #This block handles the more generic ParserError from pandas, which occurs when there is an issue parsing the CSV file. 
        except pd.errors.ParserError:
            print(f"Error: Unable to parse file '{csv_file}'. Check the file format.")
            raise

    def top_dest_ip_percentages(self):
        top_dest_ip = self.df['Destination'].value_counts().head(5) #The value_counts method in pandas is used to count the occurrences of unique values in a Series (a single column of a DataFrame). 
        return (top_dest_ip / self.num_packets) * 100

    def top_src_ip_percentages(self):
        top_src_ip = self.df['Source'].value_counts().head(5) #top_src_ip.values print packet count
        return (top_src_ip / self.num_packets) * 100

    def top_protocol_percentages(self):
        top_protocols = self.df['Protocol'].value_counts().head(5)
        return (top_protocols / self.num_packets) * 100

    def bar_graph(self,name,title,path):
        x=name.index
        y=name.values
        t=title.split()
        plt.xlabel(t[0])
        plt.ylabel(t[-1])
        plt.title(title)
        plt.figure(figsize=(8, 4))
        plt.xticks(rotation=30)
        plt.bar(x,y)
        plt.savefig(path,bbox_inches='tight')
        plt.close()  # Close the plot to avoid displaying it
        return path

    def generate_html(self):
        self.template_file=r'c:/Users/swath/OneDrive/Desktop/python/Projects/Pcap_Analyzer/template.html'
        self.output_file = f'c:/Users/swath/OneDrive/Desktop/python/Projects/Pcap_Analyzer/output_{datetime.now().strftime("%Y%m%d%H%M%S")}.html'

        with open(self.template_file, 'r') as f:
            content = f.read()
    
        template = Template(content)
        self.rendered_form = template.render(
            filename=self.filename,
            date=date.today(),
            packets=self.num_packets,
            top_dest_ip_percentages=self.top_dest_ip_percentages().items(),
            top_src_ip_percentages=self.top_src_ip_percentages().items(),
            top_protocol_percentages=self.top_protocol_percentages().items(),
            dest_ip_graph_path=self.bar_graph(self.top_dest_ip_percentages(),"dest_ip vs percentage",r"C:\Users\swath\OneDrive\Desktop\python\Projects\Pcap_Analyzer\dest_ip.png"),
            src_ip_graph_path=self.bar_graph(self.top_src_ip_percentages(),"src_ip vs percentage",r"C:\Users\swath\OneDrive\Desktop\python\Projects\Pcap_Analyzer\src_ip.png"),
            protocol_ip_graph_path=self.bar_graph(self.top_protocol_percentages(),"protocol vs percentage",r"C:\Users\swath\OneDrive\Desktop\python\Projects\Pcap_Analyzer\protocol.png")
        )
    
        with open(self.output_file, 'w') as f:
            f.write(self.rendered_form)

    
    def open_in_browser(self):
        webbrowser.open(self.output_file)
    
    def print_results(self):
        self.generate_html()
        self.open_in_browser()

    

if __name__ == "__main__":
    # Replace 'your_file.csv' with the actual file path
    csv_file_path = r"C:\Users\swath\OneDrive\Desktop\python\Projects\Pcap_Analyzer\sample_capture.csv"

    analyzer = PCAPAnalyzer(csv_file_path)
    analyzer.print_results()
