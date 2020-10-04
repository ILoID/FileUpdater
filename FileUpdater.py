import shutil
from pathlib import Path
import os

SOURCE_DIR_NAME = 'Source'
TARGET_DIR_NAME = 'Target'
SUB_DIR_1 = '1'
SUB_DIR_2 = '2'
SUB_DIR_3 = '3'
SUB_DIR_4 = '4'
SUB_DIR_5 = '5'

base_path = Path.cwd()

source_path = base_path.joinpath(SOURCE_DIR_NAME)
source_files = os.listdir(source_path)

target_dir = base_path.joinpath(TARGET_DIR_NAME)
target_paths = [target_dir.joinpath(SUB_DIR_1), target_dir.joinpath(SUB_DIR_2), target_dir.joinpath(SUB_DIR_3), target_dir.joinpath(SUB_DIR_4), target_dir.joinpath(SUB_DIR_5)]


for target_path in target_paths:
    for target_file in os.listdir(target_path):
        full_target_name = os.path.join(target_path, target_file)
        for source_file in source_files:
            full_source_name = os.path.join(source_path, source_file)
            if source_file == target_file:
                shutil.copy(full_source_name, full_target_name)
