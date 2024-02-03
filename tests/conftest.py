import pytest
import os
import zipfile
from path import RESOURCES_DIR, FILES_LIST, ARCHIVE_DIR, TMP_DIR


@pytest.fixture
def create_new_archive():
    if not os.path.exists(RESOURCES_DIR):
        os.mkdir(RESOURCES_DIR)
    with zipfile.ZipFile(ARCHIVE_DIR, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in FILES_LIST:
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))
    with zipfile.ZipFile(ARCHIVE_DIR, 'r') as zip_ref:
        zip_ref.extractall(TMP_DIR)
    yield TMP_DIR
    os.remove(ARCHIVE_DIR)