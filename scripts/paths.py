"""
Pastas do Projeto
nov.22
"""


from pathlib import Path


project_path = Path(__file__).parents[1]

# Data
data_path = project_path / 'data'
data_path.mkdir(exist_ok=True)

input_path = data_path / 'input'
input_path.mkdir(exist_ok=True)

input_path_temp = input_path / 'temp'
input_path_temp.mkdir(exist_ok=True)

output_path = data_path / 'output'
output_path.mkdir(exist_ok=True)

# Scrapy
scrapy_path = project_path / 'scrapy'
scrapy_path.mkdir(exist_ok=True)

logs_path = scrapy_path / 'logs'
logs_path.mkdir(exist_ok=True)

adds_path = scrapy_path / 'adds'
adds_path.mkdir(exist_ok=True)

driver_path = scrapy_path / 'driver'
driver_path.mkdir(exist_ok=True)


if __name__ == '__main__':
    print(project_path)
