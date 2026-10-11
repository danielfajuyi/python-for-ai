
from pathlib import Path

# Define directory structure
base_dir = Path('sales-analysis')
data_dir = base_dir / 'data'
output_dir = base_dir / 'output'

# Create all required directories at once
for folder in (data_dir, output_dir):
    folder.mkdir(parents=True, exist_ok=True)
    
