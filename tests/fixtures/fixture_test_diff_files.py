import os
import pytest
# from gendiff.diff_files import generate_diff

# Продумать, как фикстуру использовать шаблоном сравнения?
@pytest.fixture()
def expected_output():
  filepath1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
  filepath2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
  expected_output = f"""gendiff {filepath1} {filepath2}
{{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}}"""
  return expected_output
