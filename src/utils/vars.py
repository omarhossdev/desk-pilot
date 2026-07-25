from platformdirs import user_config_dir, user_data_dir
from pathlib import Path

# For your config files (settings, preferences)
CONFIG_DIR = Path(user_config_dir("mycli"))
CONFIG_DIR.mkdir(parents=True, exist_ok=True)

# For your data files (cache, databases, downloads)
DATA_DIR = Path(user_data_dir("mycli"))
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Use it!
DB_FILE = DATA_DIR / "database.db"
 
